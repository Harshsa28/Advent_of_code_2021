use crate::read_file;


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

fn is_flash(grid: &Vec<Vec<u8>>) -> bool  {
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] > 9 {
                return true;
            }
        }
    }
    return false;
}

fn get_flash_coor(grid: &Vec<Vec<u8>>) -> (usize, usize) {
    for i in 0..grid.len() {
        for j in 0..grid[i].len() {
            if grid[i][j] > 9 {
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
    if 




}



pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    let mut grid: Vec<Vec<u8>> = create_grid(&lines);
    let num_sim: u8 = 3;
    let mut num_flashes: u32 = 0;
    for i in 0..num_sim {
        inc_all_by_one(&mut grid);
        while is_flash(&grid) {
            let flash_coor: (usize, usize) = get_flash_coor(&grid);
            num_flashes += 1;
            inc_adjacent(&mut grid, flash_coor);

        }
        
    }
    println!("grid is {:?}", grid);
}
