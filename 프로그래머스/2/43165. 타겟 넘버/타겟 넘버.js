function solution(numbers, target) {
    let result = 0
    
    const numX = numbers.length
    
    function DFS(x, ctn){
        if(x >= numX) {
            if(ctn === target) result += 1
            return
        } else {
            const currentNum = numbers[x]
            DFS(x + 1, ctn + currentNum)
            DFS(x + 1, ctn - currentNum)
        }
    }
    
    DFS(0, 0)
    
    return result
}