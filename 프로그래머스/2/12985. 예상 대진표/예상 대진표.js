function solution(n,a,b){
    let count = 1
    while(true){
        // 결승전이면 바로 결과 출력
        if(n === 2) return count
        n /= 2
        
        if(a === 1 & b === 2) return count
        if(a === 2 & b === 1) return count
        if(a - b === 1 && a % b === 1 && a % 2 === 0) {
            return count
        }
        if(b - a === 1 && b % a === 1 && b % 2 === 0) {
            return count
        }
        if(a % 2 === 0) a = a / 2
        else a = Math.floor(a / 2) + 1
        if(b % 2 === 0) b = b / 2
        else b = Math.floor(b / 2) + 1
        count += 1
    }
}