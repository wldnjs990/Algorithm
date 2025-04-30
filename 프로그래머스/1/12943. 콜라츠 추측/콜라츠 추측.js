function solution(num) {
    let count = 0;
    while (num !== 1 && count < 500){
        if(num % 2 === 0){
            num /= 2
        } else {
            num = num * 3 + 1
        }
        count += 1
    }
    if(count === 500 && num !== 1) return -1
    return count
}