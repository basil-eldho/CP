fn main(){
    let mut arr= vec!(3, 30, 6, 45, 9, 1);

    let n = arr.len();

    for i in 0..n-1{
        let mut swapped = false;
        for j in 0..n-i-1{
            if arr[j]> arr[j+1]{
                arr.swap(j, j+1);
                swapped= true;
            }
        }
        if !swapped{
            break;
        }
    }

    println!("{:?}", arr);
}