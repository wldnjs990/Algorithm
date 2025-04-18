function solution(picks, minerals) {
    // 곡괭이 다 돌려보고 그 중에서 가장 작은 피로도 구하면 그만 아님?
    const result = []
    function BFS(picks, minerals){
        const queue = [[[...picks], [...minerals], 0]]
        
        while(queue.length){
            let [pickArr, mineralArr, count] = queue.shift()
            
            // 곡괭이가 없어서 끝나는 경우
            let finished = true
            // 광물이 없으면 끝
            if(!mineralArr.length){
                result.push(count)
                continue;
            }
            // 곡괭이 3종류 만큼 반복문
            pickArr.forEach((pickCtn, idx)=>{
                const copyPicks = [...pickArr]
                const copyMineralArr = [...mineralArr]
                let copyCount = count
                // 현재 곡괭이가 0개 이상이면
                if(pickCtn > 0){
                    // 곡괭이가 있으니 끝나지 않음
                    finished = false
                    // 현재 남은 광물 갯수가 5 이상일때
                    if(copyMineralArr.length >= 5){
                        for(let i = 0; i < 5; i++){
                            const mineral = copyMineralArr.shift()
                            if(mineral === 'diamond'){
                                if(idx === 0) copyCount += 1
                                if(idx === 1) copyCount += 5
                                if(idx === 2) copyCount += 25
                            } else if(mineral === 'iron'){
                                if(idx === 0) copyCount += 1
                                if(idx === 1) copyCount += 1
                                if(idx === 2) copyCount += 5
                            } else {
                                copyCount += 1
                            }
                        }
                    }
                    // 현재 남은 광물 갯수가 5 미만일때
                    else {
                        const leastLen = copyMineralArr.length
                        for(let i = 0; i < leastLen; i++){
                            const mineral = copyMineralArr.shift()
                            if(mineral === 'diamond'){
                                if(idx === 0) copyCount += 1
                                if(idx === 1) copyCount += 5
                                if(idx === 2) copyCount += 25
                            } else if(mineral === 'iron'){
                                if(idx === 0) copyCount += 1
                                if(idx === 1) copyCount += 1
                                if(idx === 2) copyCount += 5
                            } else {
                                copyCount += 1
                            }
                        }
                    }
                    // 현재 곡괭이 1개 제거
                    copyPicks[idx] -= 1
                    // 변환정보 새로 큐에 쌓기
                    queue.push([copyPicks, copyMineralArr, copyCount])
                }
            })
            if(finished) result.push(count)
        }
    }
    BFS(picks, minerals)
    return Math.min(...result)
}