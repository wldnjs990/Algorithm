function solution(targets) {
    targets.sort((a, b)=>a[1] - b[1])
    // 새로운 공격의 끝점
    let temp = targets[0][1]
    let count = 1
    for(let i = 0; i < targets.length; i++){
        // 현재 공격의 시작점이 temp 공격의 끝점보다 앞에 나가있다면 새로운 요격 준비
        if(targets[i][0] >= temp){
            count += 1
            temp = targets[i][1]
        }
    }
    console.log(targets)
    return count
}