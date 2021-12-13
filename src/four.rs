use crate::read_file;

#[derive(Debug)]
struct Board {
    nums: Vec<Vec<u32>>,
    marks: Vec<Vec<bool>>,
}

impl Board {
    fn new(lines: &[String]) -> Board {
        let mut nums: Vec<Vec<u32>> = Vec::new();
        assert!(lines.len() == 5);
        for i in 0..lines.len() {
            nums.push(lines[i].
                split_whitespace().
                map(|s| s.
                    parse::<u32>().
                    expect("problem with parsing to u32")).
                collect()
                );
        }
        assert!(nums.len() == 5);
        assert!(nums[0].len() == 5);
        return Board {
            nums : nums,
            marks : vec![vec![false;5];5]
        };
    }

    fn check_num(&mut self, num: u32) -> bool {
        for i in 0..self.nums.len() {
            for j in 0..self.nums[i].len() {
                if self.nums[i][j] == num {
                    self.marks[i][j] = true;
                }
            }
        }

        // check for rows
        for i in 0..self.marks.len() {
            if self.marks[i][0] && self.marks[i][1] && self.marks[i][2] && self.marks[i][3] && self.marks[i][4] {
                return true;
            }
        }

        // check for cols
        for i in 0..self.marks[0].len() {
            if self.marks[0][i] && self.marks[1][i] && self.marks[2][i] && self.marks[3][i] && self.marks[4][i] {
                return true;
            }
        }

        return false;
    }

    fn unmarked_sum(&self) -> u32 {
        let mut sum: u32 = 0;
        for i in 0..self.nums.len() {
            for j in 0..self.nums[0].len() {
                if self.marks[i][j] == false {
                     sum += self.nums[i][j];
                }
            }
        }
        return sum;
    }

}


pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let rnd_nums: Vec<u32> = lines[0].
        split(',').
        map(|s| s.
            parse::<u32>().
            expect("problem with parsing to u32")).
        collect();
    let mut boards: Vec<Board> = lines.
        iter().
        enumerate().
        skip(2).
        step_by(6).
        map(|(i, _)| Board::new(&lines[i..i+5])).
        collect();
    let num_boards = boards.len();
    let mut won: Vec<usize> = Vec::new();

    println!("rnd_nums is {:?}", rnd_nums);
    println!("boards is {:?}", boards);
   
    for rnd_num in rnd_nums {
        for i in 0..boards.len() {
            let board: &mut Board = &mut boards[i];
            let ret: bool = board.check_num(rnd_num);
            if ret {
                if !won.contains(&i) {
                    won.push(i);
                    if won.len() == num_boards {
                        println!("SUCCESS. won is {:?} and rnd_num is {:?} and answer is {:?}", won, rnd_num, boards[*won.last().unwrap()].unmarked_sum() * rnd_num);
                    }
                }
            }
        }
    }
    //println!("won is {:?}", won);

}



