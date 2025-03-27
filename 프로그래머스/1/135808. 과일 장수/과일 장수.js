function solution(k, m, score) {
    score.sort((a, b)=>b-a)
    let result = 0
    
    for(let i = 1; i <= score.length; i++){
        if(i % m === 0){
            result += score[i - 1] * m
        }
    }
    
    return result
    
}