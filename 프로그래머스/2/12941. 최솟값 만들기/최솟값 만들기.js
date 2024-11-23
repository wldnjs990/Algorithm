function solution(A,B){
    let result = 0;
    A.sort((a, b) => a - b)
    B.sort((a, b) => b - a)
    A.forEach((e, idx) => {
        result += e * B[idx]
    })
    return result
}