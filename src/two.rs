use crate::read_file;

pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let (mut hor, mut ver, mut aim) = (0i32, 0i32, 0i32);
    
    for line in lines {
        let words: Vec<&str> = line.split(' ').collect();
        let num: i32 = words[1].parse::<i32>().unwrap();
        match words[0] {
            "forward" => {
                hor += num;
                ver += aim*num;
            }
            "up" => aim -= num,
            "down" => aim += num,
            _ => println!("unexpected case in match. Words is {:?}", words),
        }
    }

    println!("hor is {:?} and ver is {:?} and mult is {:?}", hor, ver, hor*ver);    
}
