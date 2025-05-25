// 시간을 분단위로 표현하면 더 쉽게 풀 수 있지 않을까?

function solution(plans) {
    
    // 실행시간별 오름차순하기
    const sortPlans = plans.map((plan)=>{
        // 시간 분으로 변환
        const minuite = plan[1].split(':').reduce((acc, cur, idx)=>{
            if(idx === 0) return Number(cur) * 60
            else return acc + Number(cur)
        }, 0)
        plan[1] = minuite
        plan[2] = Number(plan[2])
        return plan
    })
    sortPlans.sort((a, b)=> a[1] - b[1])
    
    let curTime = sortPlans[0][1]
    const hash = {}
    const stack = []
    let finished = 0
    const result = []
    
    sortPlans.forEach((e)=>{
        hash[e[1]] = [e[0], e[2]]
    })
    
    while(finished < sortPlans.length){
        if(stack.length){
            stack[stack.length - 1][1] -= 1;
            // 마지막 스택 잔여시간이 다 되면 이름 결과에 추가하고 스택 지우기
            if(stack[stack.length - 1][1] === 0){
                result.push(stack[stack.length - 1][0])
                stack.pop()
                finished += 1
            }
        }
        
        if(hash[curTime]){
            stack.push(hash[curTime])
        }
        curTime += 1
    }
    return result
}