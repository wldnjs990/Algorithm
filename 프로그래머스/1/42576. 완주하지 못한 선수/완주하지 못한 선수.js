function solution(participant, completion) {
    const hash = {}
    completion.forEach(e=>{
        if(hash[e]){
            hash[e] += 1
        } else {
            hash[e] = 1
        }
    })
    let result = ''
    participant.forEach(e=>{
        if(hash[e] === undefined || hash[e] < 1) {
            result = e
        } else {
            hash[e] -= 1
        }
    })
    return result
}