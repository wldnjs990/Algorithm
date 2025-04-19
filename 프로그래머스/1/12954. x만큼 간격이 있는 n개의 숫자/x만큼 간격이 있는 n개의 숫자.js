function solution(x, n) {
    return new Array(n).fill(x).map((e, idx)=>e * (idx + 1))
}