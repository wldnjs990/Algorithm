function solution(s) {
    if(s.length !== 4 && s.length !== 6) return false
    const number = [0,1,2,3,4,5,6,7,8,9]
    let result = true
    s.split('').forEach((e)=>{
        if(!number.includes(Number(e))) result = false
    })
    return result
}