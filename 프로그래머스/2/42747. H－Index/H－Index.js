function solution(citations) {
    const stack = []
    citations.sort((a, b)=> a - b)
    const n = citations.length
    for(let i = 0; i < n; i++){
        const h = citations[i]
        const candidate = n - i
        if(h >= candidate) stack.push(candidate)
    }
    return stack.length ? Math.max(...stack) : 0
}