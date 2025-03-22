function solution(absolutes, signs) {
    let result = 0
    absolutes.forEach((e, idx)=>{
        if(signs[idx]){
            result += e
        } else {
            result -= e
        }
        
    })
    return result
}