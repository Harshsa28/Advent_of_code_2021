use std::fs::File;
use std::io::{self, BufRead};

/* Input is filename
 * Output is a Vector of String
 */
pub fn read_lines(filename: &str) -> Vec<String>{
    // println!("filename is {:?}", filename);
    let f = File::open(filename).expect("couldn't open file");
    let maybe_lines = io::BufReader::new(f).lines();
    let lines: Vec<_> = maybe_lines.
        filter_map(|s| s.ok()).
        collect();
    // println!("lines is {:?}", lines);
    return lines;
}
