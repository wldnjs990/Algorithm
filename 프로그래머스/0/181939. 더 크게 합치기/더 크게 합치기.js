function solution(a, b) {
    return Number(a.toString() + b.toString()) >= Number(b.toString() + a.toString()) ? Number(a.toString() + b.toString()) : Number(b.toString() + a.toString())
}