function solution(weights) {
    let result = 0
    
    const hashMap = {}
    
    weights.sort((a, b)=> a - b)
    // 해시맵에 weights 넣기
    weights.forEach(e=>{
        const hash = hashMap[e]
        if(!hash){
            hashMap[e] = 1 
        } else {
            hashMap[e] += 1
        }
    })
    // 해시맵에서 1 이상인 숫자들은 짝꿍으로 취급
    const hashKeys = Object.keys(hashMap)
    hashKeys.forEach(e=>{
        const count = hashMap[e]
        if(count > 1) {
            result += (count * (count - 1)) / 2;
        }
    })
    
    // BFS
    function BFS(start){
        const queue = [[start, start + 1]]
        
        while(queue.length){
            let [x, y] = queue.shift()
            if(y >= hashKeys.length || x > hashKeys.length) continue
            const meter = [2, 3, 4]

            const now = hashKeys[x]
            const next = hashKeys[y]

            for(let i = 0; i < 3; i++){
                if(now * meter[i] === next * 2){
                    result += hashMap[now] * hashMap[next]
                    console.log('2배',meter[i],now,next,hashMap[now] * hashMap[next])
                    break
                }
                if(now * meter[i] === next * 3){
                    result += hashMap[now] * hashMap[next]
                    console.log('3배',meter[i],now,next,hashMap[now] * hashMap[next])
                    
                    break
                }
                if(now * meter[i] === next * 4){
                    result += hashMap[now] * hashMap[next]
                    console.log('4배',meter[i],now,next,hashMap[now] * hashMap[next])
                    
                    break
                }
            }

            y += 1
            queue.push([x, y])
        }
    }
    for(let i = 0; i < hashKeys.length; i++){
        BFS(i)
    }
    return result
}