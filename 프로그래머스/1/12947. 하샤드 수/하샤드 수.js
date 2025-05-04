function solution(x) {
    const a = x.toString().split('').reduce((acc, cur)=> acc + Number(cur), 0)
    return x % a === 0 ? true : false
}