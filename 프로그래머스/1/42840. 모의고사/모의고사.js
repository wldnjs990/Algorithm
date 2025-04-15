function solution(answers) {
    const st = [1, 2, 3, 4, 5]
    const nd = [2, 1, 2, 3, 2, 4, 2, 5]
    const rd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    const obj = {1 : 0, 2 : 0, 3 : 0}
    const keys = [1, 2, 3]
    for(let i = 0; i < answers.length; i++){
        if(st[i % st.length] === answers[i]) obj[1] += 1 
        if(nd[i % nd.length] === answers[i]) obj[2] += 1
        if(rd[i % rd.length] === answers[i]) obj[3] += 1
    }
    
    const max = Math.max(...Object.values(obj))
    return keys.filter(e => { if(obj[e] === max) return e })
}