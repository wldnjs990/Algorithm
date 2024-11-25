function solution(n) {
    let plus = 0;
    let count = 0;
    for(let i = 1; i <= n; i++){
        let start = i
        while (plus < n){
            plus += start
            start += 1
        }
        if(plus === n) count += 1
        plus = 0
    }
    return count
}