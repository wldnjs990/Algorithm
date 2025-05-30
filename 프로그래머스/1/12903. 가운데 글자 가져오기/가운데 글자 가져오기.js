function solution(s) {
    const length = s.length
    if(length % 2 > 0) return s.split('').splice(length / 2, 1).join('')
    else return s.split('').splice(length / 2 - 1, 2).join('')
}