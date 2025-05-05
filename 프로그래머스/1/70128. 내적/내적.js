function solution(a, b) {
    let result = 0;
    a.forEach((e, idx)=>{
        result += e * b[idx]
    })
    return result
}