use std::io;

fn main() {
    println!("Guess right tf now :gunr:");
    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("U FUCKED UP BUCKO");
    println!("Here's ur number: {guess} good work scout.");
}
