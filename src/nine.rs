use crate::read_file;
use std::collections::{HashMap, VecDeque};

fn create_height_map(lines: &Vec<String>) -> Vec<Vec<u8>> {
    let mut height_map: Vec<Vec<u8>> = Vec::new();
    for line in lines {
        height_map.push((&line).chars().map(|c: char| c.to_digit(10).unwrap() as u8).collect::<Vec<u8>>());
    }
    return height_map;
}

fn find_low_pts(height_map: &Vec<Vec<u8>>) -> u32 {
    let mut risk_lvl_sum: u32 = 0;
    for i in 0..height_map.len() {
        for j in 0..height_map[i].len() {
            if ((i == 0) || height_map[i][j] < height_map[i-1][j]) &&
                ((j+1 == height_map[i].len()) || height_map[i][j] < height_map[i][j+1]) &&
                ((i+1 == height_map.len()) || height_map[i][j] < height_map[i+1][j]) &&
                ((j == 0) || height_map[i][j] < height_map[i][j-1]) {
                    risk_lvl_sum += (height_map[i][j] as u32) + 1;
                }
        }
    }
    return risk_lvl_sum;
}

pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let height_map: Vec<Vec<u8>> = create_height_map(&lines);
    let risk_lvl_sum = find_low_pts(&height_map);
    println!("risk_lvl_sum is {:?}", risk_lvl_sum);
    
}

fn get_low_pts(height_map: &Vec<Vec<u8>>) -> Vec<(usize, usize)> {
    let mut low_pts: Vec<(usize, usize)> = Vec::new();

    for i in 0..height_map.len() {
        for j in 0..height_map[i].len() {
            if ((i == 0) || height_map[i][j] < height_map[i-1][j]) &&
                ((j+1 == height_map[i].len()) || height_map[i][j] < height_map[i][j+1]) &&
                ((i+1 == height_map.len()) || height_map[i][j] < height_map[i+1][j]) &&
                ((j == 0) || height_map[i][j] < height_map[i][j-1]) {
                    low_pts.push((i, j));
                }
        }
    }

    return low_pts;
}


fn check_basin_pt (pt: (usize, usize), visited: &mut HashMap<(usize, usize), bool>, to_visit: &mut VecDeque<(usize, usize)>, height_map: &Vec<Vec<u8>>) {
    let (i, j): (usize, usize) = (pt.0, pt.1);
    if (i < height_map.len() && j < height_map[i].len()) && !visited.contains_key(&pt) && height_map[i][j] != 9 {
        to_visit.push_back((i, j));
        visited.insert(pt, true);
    }
}



fn find_basin_size(height_map: &Vec<Vec<u8>>, low_pt: (usize, usize)) -> u8 {
    let mut basin: Vec<(usize, usize)> = Vec::new();
    let mut basin_size: u8 = 0;
    let mut visited: HashMap<(usize, usize), bool> = HashMap::new();
    let mut to_visit: VecDeque<(usize, usize)> = VecDeque::new();
    to_visit.push_back(low_pt);
    visited.insert(low_pt, true);

    while to_visit.len() > 0 {
        let current: (usize, usize) = to_visit.pop_front().expect("error while pop_front from to_visit");
        if current.0 > 0 {
            check_basin_pt((current.0-1, current.1), &mut visited, &mut to_visit, height_map);
        }
        check_basin_pt((current.0, current.1+1), &mut visited, &mut to_visit, height_map);
        check_basin_pt((current.0+1, current.1), &mut visited, &mut to_visit, height_map);
        if current.1 > 0 {
            check_basin_pt((current.0, current.1-1), &mut visited, &mut to_visit, height_map);
        }
        basin_size += 1;
        basin.push(current);
    }
    
    return basin_size;
}





















pub fn b(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let height_map: Vec<Vec<u8>> = create_height_map(&lines);
    let low_pts: Vec<(usize, usize)> = get_low_pts(&height_map);
    let mut basin_sizes: Vec<u8> = Vec::new();
    for low_pt in &low_pts {
        basin_sizes.push(find_basin_size(&height_map, *low_pt));
    }
    basin_sizes.sort();
    basin_sizes.reverse();
    assert!(basin_sizes.len() > 3);
    println!("basin_sizes is {:?}", basin_sizes);
    let mult: u32 = basin_sizes[0] as u32 * basin_sizes[1] as u32 * basin_sizes[2] as u32;
    println!("ans is {:?}", mult);
}
