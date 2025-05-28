// strings와 정수
function solution(strings, n) {
    strings.sort()
    return strings.sort((a, b)=> {
        return a[n].charCodeAt() - b[n].charCodeAt()    
    })
}