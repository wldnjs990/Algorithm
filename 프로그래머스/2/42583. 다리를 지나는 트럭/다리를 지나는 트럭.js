// 모든 트럭이 지나가는데 걸리는 최소 시간
// 

function solution(bridge_length, weight, truck_weights) {
    let count = 1
    const queue = [[truck_weights.shift(), bridge_length]]

    while(truck_weights.length || queue.length){
        // 1초 추가하고, 현재 도로에 있는 차량들 거리 -1
        count += 1
        for(let i = 0; i < queue.length; i++) queue[i][1] -= 1
        if(queue[0][1] === 0) queue.shift()
        // 현재 도로에 있는 차들의 무게를 측정하고, 다음 차량을 더한 값 보다 weight가 낮으면 차량 queue 추가
        const sum = queue.reduce((acc, cur)=>{return acc + cur[0]}, 0)
        if(sum + truck_weights[0] <= weight) queue.push([truck_weights.shift(), bridge_length])
        // 현재 첫 번째 차량이 목적지에 도달했으면 차량 제거
    }
    return count
}