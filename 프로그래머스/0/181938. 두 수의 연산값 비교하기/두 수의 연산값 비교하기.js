function solution(a, b) {
    const str = Number(a.toString() + b.toString())
    const num = 2 * a * b
    return str >= num ? str : num
}