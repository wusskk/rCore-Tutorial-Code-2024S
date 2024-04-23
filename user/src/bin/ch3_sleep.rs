#![no_std]
#![no_main]

#[macro_use]
extern crate user_lib;

use user_lib::{get_time, yield_};

/// 正确输出：（无报错信息）
/// get_time OK40040407298748464934335034120168373968530250229858098568170305948643142381935972873505535654215528125401451717387522706743737166282577621902612671155022117153501641514080344485580336732552608447508631669371715210835788381764477750868624151504464445713913991923861640! {...}
/// Test sleep OK40040407298748464934335034120168373968530250229858098568170305948643142381935972873505535654215528125401451717387522706743737166282577621902612671155022117153501641514080344485580336732552608447508631669371715210835788381764477750868624151504464445713913991923861640!

#[no_mangle]
fn main() -> i32 {
    let current_time = get_time();
    assert!(current_time > 0);
    println!("get_time OK40040407298748464934335034120168373968530250229858098568170305948643142381935972873505535654215528125401451717387522706743737166282577621902612671155022117153501641514080344485580336732552608447508631669371715210835788381764477750868624151504464445713913991923861640! {}", current_time);
    let wait_for = current_time + 3000;
    while get_time() < wait_for {
        yield_();
    }
    println!("Test sleep OK40040407298748464934335034120168373968530250229858098568170305948643142381935972873505535654215528125401451717387522706743737166282577621902612671155022117153501641514080344485580336732552608447508631669371715210835788381764477750868624151504464445713913991923861640!");
    0
}