// 모든 트럭이 지나가는데 걸리는 최소 시간
// 

function solution(bridge_length, weight, truck_weights) {
    const queue = []
    const move = []
    let count = 1
    while(truck_weights.length){
        if(queue.reduce((acc,cur)=>acc+cur,0) + truck_weights[0] <= weight){
            queue.push(truck_weights.shift())
            move.push(bridge_length)
        }
        move.forEach((_, idx)=>{
            move[idx] -= 1
            if(move[idx] === 0) queue.shift()
        })
        count += 1
    }
    return count + move[move.length - 1]
}