// 아니 이게 피보나치 수열이네
function solution(n) {
    const fibo = [1, 2]
    for(let i = 2; i < n; i++){
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1234567
    }
    return fibo[n - 1]
}