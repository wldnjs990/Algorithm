function solution(maps) {
    const result = []
    
    const mapRow = maps.length
    const mapCol = maps[0].length
    
    // 무인도 존재 확인
    const isExist = isIslandExist(maps, mapRow, mapCol)
    if(!isExist) return [-1]
    
    // BFS
    const dx = [0, 1, 0, -1]
    const dy = [1, 0, -1, 0]
    
    // 탐색한 지역 2차배열
    const visitedArr = []
    for(let i = 0; i < mapRow; i++){
        visitedArr.push(new Array(mapCol).fill(false))
    }
    
    function BFS(x, y){
        let count = 0
        const queue = [[x, y]]
        
        while(queue.length){
            const [x, y] = queue.shift()
            count += Number(maps[y][x])
            
            for(let i = 0; i < 4; i++){
                const nx = x + dx[i]
                const ny = y + dy[i]
                
                if(nx < 0 || ny < 0 || nx >= mapCol || ny >= mapRow || maps[ny][nx] === 'X' || visitedArr[ny][nx]) continue;
                
                queue.push([nx, ny])
                visitedArr[ny][nx] = true
            }
        }
        result.push(count)
    }
    
    for(let y = 0; y < mapRow; y++){
        for(let x = 0; x < mapCol; x++){
            if(visitedArr[y][x] || maps[y][x] === 'X') continue
            visitedArr[y][x] = true
            BFS(x, y)
        }
    }
    return result.sort((a, b)=>a-b)
}

// 무인도 존재 확인
function isIslandExist(maps, mapRow, mapCol){
    let exist = false
    for(let i = 0; i < mapRow; i++){
        for(let j =0; j < mapCol; j++){
            if(maps[i][j] !== 'X') exist = true
        }
    }
    return exist
}


