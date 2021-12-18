use crate::read_file;
use std::collections::HashMap;

fn create_grid(lines: &Vec<String>) -> Vec<Vec<u8>> {
    let mut grid: Vec<Vec<u8>> = Vec::new();
    for line in lines {
        grid.push(line.chars().map(|ch| ch.to_digit(10).expect("couldn't convert char to digit") as u8).collect::<Vec<u8>>());
    }
    return grid;
}

fn inc_all_by_one(grid: &mut Vec<Vec<u8>>) {
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            grid[i][j] += 1;
        }
    }
}

fn is_flash(grid: &Vec<Vec<u8>>, flashed: &HashMap<(usize, usize), bool>) -> bool  {
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] > 9 && !flashed.contains_key(&(i, j)) {
                return true;
            }
        }
    }
    return false;
}

fn get_flash_coor(grid: &Vec<Vec<u8>>, flashed: &HashMap<(usize, usize), bool>) -> (usize, usize) {
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] > 9 && !flashed.contains_key(&(i, j)){
                return (i, j);
            }
        }
    }
    panic!("no flash in grid");
}

fn inc_adjacent(grid: &mut Vec<Vec<u8>>, flash_coor: (usize, usize)) {
    let (i, j) : (usize, usize) = (flash_coor.0, flash_coor.1);
    
    if i > 0 {
        grid[i-1][j] += 1;
    }
    if i > 0 && j < grid[i].len()-1 {
        grid[i-1][j+1] += 1;
    }
    if j < grid[i].len()-1 {
        grid[i][j+1] += 1;
    }
    if i < grid.len()-1 && j < grid[i].len()-1 {
        grid[i+1][j+1] += 1;
    }
    if i < grid.len()-1 {
        grid[i+1][j] += 1;
    }
    if i < grid.len()-1 && j > 0 {
        grid[i+1][j-1] += 1;
    }
    if j > 0 {
        grid[i][j-1] += 1;
    }
    if i > 0 && j > 0 {
        grid[i-1][j-1] += 1;
    }

}

fn do_all_flash(grid: &Vec<Vec<u8>>) -> bool {
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] != 0 {
                return false;
            }
        }
    }
    return true;
}



pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let mut grid: Vec<Vec<u8>> = create_grid(&lines);
    println!("initial grid is {:?}", grid);
    let num_sim: u32 = 1000;
    let mut num_flashes: u32 = 0;
    for i in 0..num_sim {
        inc_all_by_one(&mut grid);
        let mut flash_coors: Vec<(usize, usize)> = Vec::new();
        let mut flashed: HashMap<(usize, usize), bool> = HashMap::new();
        while is_flash(&grid, &flashed) {
            let flash_coor: (usize, usize) = get_flash_coor(&grid, &flashed);
            flashed.insert(flash_coor, true);
            num_flashes += 1;
            inc_adjacent(&mut grid, flash_coor);
            flash_coors.push(flash_coor);
        }
        for flash_coor in &flash_coors {
            grid[flash_coor.0][flash_coor.1] = 0;
        }
        if do_all_flash(&grid) {
            println!("all flashed at step {:?}", i+1);
            break;
        }
        //println!("grid after step {:?} is {:?}", i, grid);
    }
    println!("final grid is {:?}", grid);
    println!("num_flashes is {:?}", num_flashes);
}
