use crate::read_file;

pub fn a(filename: &str) {
    let lines = read_file::read_lines(filename);
    // println!("lines is {:?}", lines);
    let nums: Vec<i32> = lines.
        iter().
        filter_map(|s| s.parse::<i32>().ok()).
        collect();
    println!("nums is {:?}", nums);

    let ans = nums.
        iter().
        enumerate().
        skip(1).
        filter(|&(index, _)| nums[index as usize] > nums[(index-1) as usize]).
        count();
    println!("ans is {:?}", ans);


}


pub fn b(filename: &str) {
    let lines = read_file::read_lines(filename);
    // println!("lines is {:?}", lines);
    let nums: Vec<i32> = lines.
        iter().
        filter_map(|s| s.parse::<i32>().ok()).
        collect();
    println!("nums is {:?}", nums);

    let ans = nums.
        iter().
        enumerate().
        skip(3).
        filter(|&(i, _)| nums[i as usize] > nums[(i-3) as usize]).
        count();
    println!("ans is {:?}", ans);
}
