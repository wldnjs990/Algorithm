function solution(n, m, section) {
    let start = true
    let result = 0
    while(section.length){
        if(start){
            // 시작점의 숫자로 부터 m길이만큼 해당하면 제거
            const now = section[0] + m
            while(section[0] < now){
                section.shift()
            }
            result += 1
        } else {
            // 끝점의 숫자로 부터 m길이만큼 해당하면 제거
            const now = section[section.length - 1] - m
            while(section[0] > now){
                section.pop()
            }
            result += 1
        }
    }
    return result
}