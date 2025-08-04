function solution(n) {
    if(n % 2 === 0) {
        let result = 0
        for(let i = 1; i <= n; i++){
            if(i % 2 === 0) {
                result += i**2
            }
        }
        return result
    } else if(n % 2 === 1) {
        let result = 0
        for(let i = 1; i <= n; i++){
            if(i % 2 === 1){
                result += i
            }
        }
        return result
    }
}