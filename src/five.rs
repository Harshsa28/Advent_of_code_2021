use crate::read_file;
use std::str::FromStr;

#[derive(Debug)]
struct Range{
    left: (u32, u32),
    right: (u32, u32),
}

impl Range{
    fn new(line: &String) -> Range {
        let coords: Vec<String> = line.split("->").map(|coord| coord.trim().to_string()).collect();
        assert!(coords.len() == 2);
        let left: Vec<u32> = coords[0].split(',').map(|v| u32::from_str(v).expect("problem with parsing")).collect();
        assert!(left.len() == 2);
        let right: Vec<u32> = coords[1].split(',').map(|v| u32::from_str(v).expect("problem with parsing")).collect();
        assert!(right.len() == 2);
        return Range {
            left: (left[0], left[1]),
            right: (right[0], right[1]),
        }
    }

    fn is_hor_or_ver(&self) -> bool {
        return (self.left.0 == self.right.0) || (self.left.1 == self.right.1)
    }
    
    fn plot(&self, field: &mut Vec<Vec<u8>>) {
        //println!("in plot, range is {:?}", self);
        //println!("initial field in plit is \n{:?}", field);
        if self.left.0 == self.right.0 {
            // ver line
            for row in (self.left.1)..(self.right.1 + 1) {
                //println!("row is {:?}", row);
                field[row as usize][self.left.0 as usize] += 1;
                //field[self.left.0 as usize][col as usize] += 1;
            }
            for row in (self.right.1)..(self.left.1 + 1) {
                //println!("row is {:?}", row);
                field[row as usize][self.left.0 as usize] += 1;
                //field[self.left.0 as usize][col as usize] += 1;
            }
        }
        else if self.left.1 == self.right.1 {
            // hor line
            for col in (self.left.0)..(self.right.0 + 1) {
                //println!("col is {:?}", col);
                field[self.left.1 as usize][col as usize] += 1;
                //field[row as usize][self.left.1 as usize] += 1;
            }
            for col in (self.right.0)..(self.left.0 + 1) {
                //println!("col is {:?}", col);
                field[self.left.1 as usize][col as usize] += 1;
                //field[row as usize][self.left.1 as usize] += 1;
            }
        }
        else {
            // diagonal
            if self.left.0 <= self.right.0 {
                if self.left.1 <= self.right.1 {
                    for i in 0..(self.right.0 - self.left.0 + 1) {
                        field[(self.left.1 + i) as usize][(self.left.0 + i) as usize] += 1;
                    }
                }
                else {
                    for i in 0..(self.right.0 - self.left.0 + 1) {
                        field[(self.left.1 - i) as usize][(self.left.0 + i) as usize] += 1;
                    }
                }
            }
            else {
                if self.left.1 <= self.right.1 {
                    for i in 0..(self.left.0 - self.right.0 + 1) {
                        field[(self.left.1 + i) as usize][(self.left.0 - i) as usize] += 1;
                    }
                }
                else {
                    for i in 0..(self.left.0 - self.right.0 + 1) {
                        field[(self.left.1 - i) as usize][(self.left.0 - i) as usize] += 1;
                    }
                }
            }
        }
        //println!("updated field in plot is \n{:?}", field);
    }

}

fn get_max(ranges: &Vec<Range>) -> (u32, u32) {
    let (mut max_row, mut max_col): (u32, u32) = (0u32, 0u32);
    for range in ranges {
        if range.left.0 > max_row {
            max_row = range.left.0;
        }
        if range.right.0 > max_row {
            max_row = range.right.0;
        }
        if range.left.1 > max_col {
            max_col = range.left.1;
        }
        if range.right.1 > max_col {
            max_col = range.right.1;
        }
    }
    return (max_row, max_col);
}



fn count_overlap(field: &Vec<Vec<u8>>) -> u32 {
    let mut c: u32 = 0;
    for row in 0..field.len() {
        for col in 0..field[row].len() {
            if field[row][col] > 1 {
                c += 1;
            }
        }
    }
    return c;
}



pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let ranges: Vec<Range> = lines.iter().map(|line: &String| Range::new(line)).collect::<Vec<Range>>();

    //println!("printing ranges");
    //for range in &ranges {
        //println!("range is {:?} and is it hor_or_ver : {:?}", range, range.is_hor_or_ver());
    //}
    
    let (max_row, max_col): (u32, u32) = get_max(&ranges);

    //println!("max_row is {:?} and max_col is {:?}", max_row, max_col);

    let mut field: Vec<Vec<u8>> = vec![vec![0; (max_col+1) as usize]; (max_row+1) as usize];

    //println!("field is {:?}", field);

    for range in &ranges {
        range.plot(&mut field);
    }

    //println!("updated field is \n{:?}", field);

    println!("overlap is {:?}", count_overlap(&field));
}
