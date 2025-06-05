function solution(s) {
    const target = s.split(' ').map(e=>Number(e))
    return `${Math.min(...target)} ${Math.max(...target)}`
}