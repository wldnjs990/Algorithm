function solution(n, left, right) {
    const result = []
    for(let i = left; i <= right; i++){
        const row = Math.floor(i / n)
        const col = i % n
        let now;
        if(row >= col) now = row + 1
        else now = col + 1
        result.push(now)
    }
    return result
    
}