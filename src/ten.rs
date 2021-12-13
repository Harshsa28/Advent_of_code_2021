use crate::read_file;

fn is_opening(bracket: char) -> bool {
    if bracket == '(' || bracket == '[' || bracket == '{' || bracket == '<' {
        return true;
    }
    else {
        return false;
    }
}

fn is_closing(bracket: char) -> bool {
    if bracket == ')' || bracket == ']' || bracket == '}' || bracket == '>' {
        return true;
    }
    else {
        return false;
    }
}

fn is_matching(left: char, right: char) -> bool {
    if (left == '(' && right == ')') ||
        (left == '[' && right == ']') || 
        (left == '{' && right == '}') ||
        (left == '<' && right == '>') {
            return true;
        }
    else {
        return false;
    }
}

fn is_corrupted(line: &String) -> Option<char> {
    let mut history: Vec<char> = Vec::new();
    for ch in line.chars() {
        if is_opening(ch) {
            history.push(ch);
        }
        else if is_closing(ch) {
            let last: Option<char> = history.pop();
            match last {
                Some(last_ch) => {
                    if !is_matching(last_ch, ch) {
                        return Some(ch);
                    }
                },
                None => {
                    return Some(ch);
                }
            }
        }
    }
    return None;
}

fn get_pts(ch: char) -> u32 {
    match ch {
        ')' => 3,
        ']' => 57,
        '}' => 1197,
        '>' => 25137,
        _ => panic!("unexpected case in get_pts"),
    }
}

fn get_history(line: &String) -> Vec<char> {
    let mut history: Vec<char> = Vec::new();
    for ch in line.chars() {
        if is_opening(ch) {
            history.push(ch);
        }
        else if is_closing(ch) {
            history.pop();
        }
        else {
            panic!("unexpected case in get_history");
        }
    }
    return history;
}

fn get_completion_pt(ch: char) -> u32 {
    match ch {
        '(' => 1,
        '[' => 2,
        '{' => 3,
        '<' => 4,
        _ => panic!("unexpected case in get_completion_pt"),
    }
}


fn get_completion_score(history: &Vec<char>) -> u64 {
    let mut score: u64 = 0;
    for ch in history.iter().rev() {
        score = score*5 + get_completion_pt(*ch) as u64;
    }
    return score;
}


pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let mut incompletes: Vec<&String> = Vec::new();
    for line in &lines {
        let corrupted_char: Option<char> = is_corrupted(line);
        match corrupted_char {
            Some(ch) => (),
            None => incompletes.push(line),
        }
    }

    let mut completion_scores: Vec<u64> = Vec::new();

    for incomplete in &incompletes {
        let history: Vec<char> = get_history(incomplete);
        completion_scores.push(get_completion_score(&history));
    }

    completion_scores.sort();
    println!("mid ele is {:?}", completion_scores[completion_scores.len()/2 as usize]);


    


}
