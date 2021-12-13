use crate::read_file;
use std::collections::HashSet;

pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);

    let ops: Vec<&str> = lines.iter().map(|s| s.split('|').collect::<Vec<&str>>()[1].trim()).collect::<Vec<&str>>();

    println!("lines is \n{:?}", lines);

    println!("ops is \n{:?}", ops);



    let mut unique = 0;

    for op in &ops {
        let digits: Vec<&str> = op.split(' ').collect::<Vec<&str>>();
        //println!("digits is {:?}", digits);
        for digit in &digits {
            let digit_len: usize = digit.len();
            if digit_len == 2 || digit_len == 3 || digit_len == 4 || digit_len == 7 {
                unique += 1;
            }
        }
    }

    println!("unique is {:?}", unique);

}

fn get_nums(ips: &mut Vec<HashSet<char>>, nums: &mut Vec<HashSet<char>>) {
    // get #1
    let loc: usize = ips.iter().position(|hs| hs.len() == 2).expect("couldn't find #1");
    nums[1] = ips.remove(loc);

    // get #4
    let loc: usize = ips.iter().position(|hs| hs.len() == 4).expect("couldn't find #4");
    nums[4] = ips.remove(loc);

    // get #7
    let loc: usize = ips.iter().position(|hs| hs.len() == 3).expect("couldn't find #7");
    nums[7] = ips.remove(loc);

    // get #8
    let loc: usize = ips.iter().position(|hs| hs.len() == 7).expect("couldn't find #8");
    nums[8] = ips.remove(loc);

    // get #2
    let loc: usize = ips.iter().position(|hs| (hs.len() == 5) && (hs.union(&nums[4]).collect::<HashSet<&char>>() == nums[8].iter().collect::<HashSet<&char>>())).expect("couldn't find #2");
    nums[2] = ips.remove(loc);

    // get #6
    let loc: usize = ips.iter().position(|hs| (hs.len() == 6) && (hs.union(&nums[1]).collect::<HashSet<&char>>() == nums[8].iter().collect::<HashSet<&char>>())).expect("couldn't find #6");
    nums[6] = ips.remove(loc);

    // get #0
    let loc: usize = ips.iter().position(|hs| (hs.len() == 6) && (hs.union(&nums[4]).collect::<HashSet<&char>>() == nums[8].iter().collect::<HashSet<&char>>())).expect("couldn't find #0");
    nums[0] = ips.remove(loc);

    // get #9
    let loc: usize = ips.iter().position(|hs| hs.len() == 6).expect("couldn't find #9");
    nums[9] = ips.remove(loc);

    // get #3
    let loc: usize = ips.iter().position(|hs| (hs.len() == 5) && (hs.union(&nums[6]).collect::<HashSet<&char>>() == nums[8].iter().collect::<HashSet<&char>>())).expect("couldn't find #3");
    nums[3] = ips.remove(loc);

    // get #5
    let loc: usize = ips.iter().position(|hs| hs.len() == 5).expect("couldn't locate #5");
    nums[5] = ips.remove(loc);
}


fn get_op (ops: &Vec<HashSet<char>>, nums: &Vec<HashSet<char>>) -> u32 {
    let mut op: u32 = 0;
    for i in 0..ops.len() {
        op = op*10 + nums.iter().position(|hs| *hs == ops[i]).expect("couldn't locate op_nums") as u32;
    }
    println!("op is {:?}", op);
    return op;
}


pub fn b(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let mut op_sum: u32 = 0;
    
    for line in &lines {
        let ips_ops: Vec<&str> = line.split('|').collect::<Vec<&str>>();
        assert!(ips_ops.len() == 2);
        let mut ips: Vec<HashSet<char>> = ips_ops[0].trim().split(' ').map(|s: &str| HashSet::from_iter(s.chars())).collect::<Vec<HashSet<char>>>();
        let ops: Vec<HashSet<char>> = ips_ops[1].trim().split(' ').map(|s: &str| HashSet::from_iter(s.chars())).collect::<Vec<HashSet<char>>>();
        //println!("ips is {:?} and ops is {:?}", ips, ops);

        let mut nums: Vec<HashSet<char>> = vec![HashSet::new(); 10];

        get_nums(&mut ips, &mut nums);

        let op: u32 = get_op(&ops, &nums);
        op_sum += op;


    }
    
    println!("op_sum is {:?}", op_sum);


}
