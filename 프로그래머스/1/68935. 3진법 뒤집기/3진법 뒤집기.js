function solution(n) {
    let result = []
    while (n){
        if(n < 3) {
            result.push(n)
            break;
        }
        result.push(n % 3)
        n = Math.floor(n / 3)
    }
    return result.reverse().reduce((acc, cur, idx)=> acc + cur * (3 ** idx), 0)
}