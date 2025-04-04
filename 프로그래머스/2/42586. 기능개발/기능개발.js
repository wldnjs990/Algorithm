function solution(progresses, speeds) {
    const result = []
    while(progresses.length){
        let count = 0
        // 첫 번째 기능이 완성되는 날짜 구하기
        const frontEnded = Math.ceil((100 - progresses[0]) / speeds[0])
        // 모든 배열을 첫 번째 기능이 완성되는 날짜 만큼 속도 더해주기
        progresses = progresses.map((e, idx)=>{
            return e += (speeds[idx] * frontEnded)
        })
        // 첫 번째 기능부터 100을 넘겼으면 현재 배열에서 제거 + 결과에 추가해주고 그렇지 않으면 반복문 중단
        const progressesLen = progresses.length
        for(let i = 0; i < progressesLen; i++){
            if(progresses[0] >= 100){
                progresses.shift()
                speeds.shift()
                count += 1
            } else {
                break
            }
        }
        
        // 무조건 한 개 이상은 카운트가 쌓였을테니 result에 값 추가해주기
        result.push(count)
    }
    return result
}