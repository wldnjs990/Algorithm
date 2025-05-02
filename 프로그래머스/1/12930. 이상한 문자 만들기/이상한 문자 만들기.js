function solution(s) {
    return s.split(' ').map((e) => e.split('').map((j, idx) => idx % 2 === 0 ? j.toUpperCase() : j.toLowerCase()).join('')).join(' ') 
}