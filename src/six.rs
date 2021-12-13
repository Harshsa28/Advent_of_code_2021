use crate::read_file;
use std::str::FromStr;





pub fn a(filename: &str) {
    let lines: Vec<String> = read_file::read_lines(filename);
    assert!(lines.len() == 1);
    let line: &String = &lines[0];

    let sim: Vec<u8> = line.split(',').map(|s: &str| u8::from_str(s).expect("problem with parsing string to u8")).collect();

    let mut num_fish_in_day: Vec<u64> = vec![0,0,0,0,0,0,0,0,0]; // 0 days, 1 days, 2 days, ..., 8 days

    for i in &sim {
        num_fish_in_day[*i as usize] += 1;
    }


    println!("sim is {:?}", sim);
    println!("num_fish_in_day is {:?}", num_fish_in_day);

    let num_days: usize = 256;

    for day in 0..num_days {


        let temp: u64 = num_fish_in_day[0];
        for i in 0..num_fish_in_day.len()-1 {
            num_fish_in_day[i] = num_fish_in_day[i+1]
        }
        num_fish_in_day[6] += temp;
        num_fish_in_day[8] = temp;
        //num_fish_in_day[num_fish_in_day.len()-1] = temp;
        //*num_fish_in_day.last_mut().unwrap() = temp;


/*



        let mut num_new: u64 = 0;
        sim = sim
            .iter()
            .map(|&x| {
                if x == 0 {
                    num_new += 1;
                    return 6
                }
                return x-1
            })
            .collect();
        for new in 0..num_new {
            sim.push(8);
        }
        //println!("sim is {:?}", sim);
*/
        //println!("day is {:?} and num_fish_in_day is {:?} and sum is {:?}", day, num_fish_in_day, num_fish_in_day.iter().sum::<u64>());

    }

    println!("num of fish is {:?}", num_fish_in_day.iter().sum::<u64>());


}
