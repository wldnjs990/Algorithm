function solution(n, k) {
    return new Array(Math.floor(n / k)).fill(k).map((e, idx)=> e * (idx + 1))
}