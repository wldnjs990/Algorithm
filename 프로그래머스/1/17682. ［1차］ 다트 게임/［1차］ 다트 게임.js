function solution(dartResult) {
    const dartResultArr = dartResult.split('')
    
    const result = []
    let prevIsNum = false
    dartResultArr.forEach(e=>{
        const resultEnd = result.length - 1
        const numE = Number(e)
        if(numE){
            // 현재 문자가 숫자라면 result배열에 추가
            result.push(numE)
            prevIsNum = true
        } else if(numE === 0){
            if(prevIsNum){
                result[resultEnd] = 10
                prevIsNum = false
            } else {
                result.push(numE)
            }
        } else {
            prevIsNum = false
            // 숫자가 아니라면 문자에 따른 후처리
            if(e === "D") result[resultEnd] **= 2
            if(e === 'T') result[resultEnd] **= 3
            if(e === '*'){
                if(result.length > 0){
                    result[resultEnd] *= 2
                    result[resultEnd - 1] *= 2
                } else {
                    result[resultEnd] *= 2
                }
            }
            if(e === '#'){
                result[resultEnd] = -result[resultEnd]
            }
        }
    })
    return result.reduce((acc, cur)=> acc + cur, 0)
}