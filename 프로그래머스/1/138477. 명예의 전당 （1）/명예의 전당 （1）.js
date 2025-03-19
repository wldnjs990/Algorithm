function solution(k, score) {
    const scoreStack = []
    const result = []
    score.forEach(e=>{
        if(scoreStack.length < k){
            scoreStack.unshift(e)
            scoreStack.sort((a, b)=> a - b)
        } else {
            if(scoreStack[0] < e){
                scoreStack.shift()
                scoreStack.unshift(e)
                scoreStack.sort((a, b)=> a - b)
            }
        }
        result.push(scoreStack[0])
    })
    return result
}