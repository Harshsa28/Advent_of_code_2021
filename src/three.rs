use crate::read_file;

pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let length: usize = lines[0].len();
    let mut freq: Vec<(i32,i32)> = vec![(0,0); length as usize];

    for line in lines {
        // e.g. line: String = "00100"
        for (bit_index, bit) in line.chars().enumerate() {
            // e.g. bit = "0" or "1"
            match bit {
                '0' => freq[bit_index].0 += 1,
                '1' => freq[bit_index].1 += 1,
                _ => println!("unexpected bit, bit is {:?}", bit),
            };
        }
        
    }
    let gamma_rate_str: String = freq.
        iter().
        map(|(zero, one)|
            if zero > one{
                "0"
            }
            else if one > zero {
                "1"
            }
            else {
                panic!("unexpected else in map. zero is {:?} and one is {:?}", zero, one);
            }
            ).
        collect::<String>();
    let gamma_rate: i32 = i32::from_str_radix(&gamma_rate_str, 2).expect("problem converting from gamma_rate_str to gamma_rate");
    let epsilon_rate = 2i32.pow(length as u32) - 1 - gamma_rate;
}

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}


fn get_freq(oxy_lines: &Vec<&String>, i: usize) -> (i32, i32) {
    let mut freq: (i32, i32) = (0,0);
    for line in oxy_lines {
        match line.chars().nth(i).unwrap() {
            '0' => freq.0 += 1,
            '1' => freq.1 += 1,
            _ => panic!("unexpected case in map, line is {:?} and i is {:?}", line, i),
        };
    }
    return freq;
}


fn check_common(s: &String, i: usize, freq: (i32, i32), most_or_least: bool) -> bool {
    // most_or_least: true for most_common and false for least_common
    
    match s.chars().nth(i).unwrap() {
        '0' => {
            if freq.0 > freq.1 {
                return most_or_least;
            }
            else {
                return !most_or_least;
            }
        },
        '1' => {
            if freq.0 > freq.1 {
                return !most_or_least;
            }
            else {
                return most_or_least;
            }
        },
        _ => panic!("unexpected case in match. char is {:?}", s.chars().nth(i).unwrap()),
    }
}


pub fn b(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let length: usize = lines[0].len();
    
    let mut oxy_lines: Vec<&String> = lines.iter().map(|s| s).collect();
    //println!("oxy_lines is {:?}", oxy_lines);

    for i in 0..length {
        let freq: (i32, i32) = get_freq(&oxy_lines, i);
        //println!("initial oxy_lines is {:?} and i is {:?}", oxy_lines, i);
        oxy_lines = oxy_lines.
            into_iter().
            filter(|s| check_common(s, i, freq, true)).
            collect();
        //println!("final oxy_lines is {:?} and i is {:?}", oxy_lines, i);
        
        if oxy_lines.len() == 1 {
            break;
        }
    }

    println!("oxy_lines is {:?}", oxy_lines);
    let oxy_rating: i32 = i32::from_str_radix(&oxy_lines[0], 2).expect("problem converting from oxy_lines to oxy_rating");
    println!("oxy_rating is {:?}", oxy_rating);
    
    let mut co2_lines: Vec<&String> = lines.iter().map(|s| s).collect();
    //println!("co2_lines is {:?}", co2_lines);

    for i in 0..length {
        let freq: (i32, i32) = get_freq(&co2_lines, i);
        //println!("ini co2_lins is {:?} and i is {:?}", co2_lines, i);
        co2_lines = co2_lines.
            into_iter().
            filter(|s| check_common(s, i, freq, false)).
            collect();
        //println!("final co2_lines is {:?} and i is {:?}", co2_lines, i);

        if co2_lines.len() == 1 {
            break;
        }
    }
    
    println!("co2_lines is {:?}", co2_lines);
    let co2_rating: i32 = i32::from_str_radix(&co2_lines[0], 2).expect("problem converting from co2_lines to co2_rating");
    println!("co2_rating is {:?}", co2_rating);

    println!("ans is {:?}", oxy_rating * co2_rating);


}

