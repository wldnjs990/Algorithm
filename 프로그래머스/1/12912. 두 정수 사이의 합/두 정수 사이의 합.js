function solution(a, b) {
    if(a === b) return a
    let result = 0;
    if(a > b){
        for(let i = b; i <= a; i++){
            result += i
        }
    } else {
        for(let i = a; i <= b; i++){
            result += i
        }
    }
    return result
}