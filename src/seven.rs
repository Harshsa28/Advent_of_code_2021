use crate::read_file;
use std::str::FromStr;

pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    assert!(lines.len() == 1);

    let line: &String = &lines[0];

    let mut subs: Vec<i32> = line.split(',').map(|s: &str| i32::from_str(s).expect("problem with parsing string to i32")).collect::<Vec<i32>>();
    subs.sort();

    println!("subs is {:?}", subs);

    let mut min_ele: i32 = -1;
    let mut min_fuel: i32 = i32::MAX;

    for try_sub in subs[0]..subs[subs.len()-1]+1 {
        let mut c: i32 = 0;
        for sub in &subs {
            let temp: i32 = (*sub - try_sub).abs();
            c += (temp * (temp+1))/2;
        }
        if c < min_fuel {
            min_fuel = c;
            min_ele = try_sub;
        }
    }

    println!("min_fuel is {:?} and min_ele is {:?}", min_fuel, min_ele);

}
