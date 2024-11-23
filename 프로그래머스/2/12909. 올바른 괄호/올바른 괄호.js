function solution(s){
    const result = []
    for(let e of s){
        if(e === "("){
            result.push(e)
        } else {
            if(result.length !== 0) result.pop(0)
            else return false
        }
    }
    return result.length === 0 ? true : false
}