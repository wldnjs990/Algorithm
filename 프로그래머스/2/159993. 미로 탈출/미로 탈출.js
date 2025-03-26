function solution(maps) {
    const mapRow = maps.length
    const mapCol = maps[0].length
    // 시작점 구하기
    function getStartAt(){
        for(let row = 0; row < mapRow; row++){
            for(let col = 0; col < mapCol; col++){
                if(maps[row][col] === 'S') return [row, col]
            }
        }
    }
    const startAt = getStartAt()
    
    // 레버 위치 구하기
    function getLeverAt(){
        for(let row = 0; row < mapRow; row++){
            for(let col = 0; col < mapCol; col++){
                if(maps[row][col] === 'L') return [row, col]
            }
        }
    }
    const leverAt = getLeverAt()
    
    // 레버 BFS
    function leverBFS(row, col){
        const queue = [[row, col, 0]]
        const dRow = [0, 1, 0, -1]
        const dCol = [1, 0, -1, 0]
        // 2차원 필터 배열 만들기
        const filterArr = []
        for(let row = 0; row < mapRow; row++){
            const arr = new Array(mapRow).fill(false)
            filterArr.push(arr)
        }
        
        let result = -1;
        while(queue.length){
            const [row, col, count] = queue.shift()
            
            for(let i = 0; i < 4; i++){
                const nowRow = row + dRow[i]
                const nowCol = col + dCol[i]
                if(nowRow < 0 || nowCol < 0 || nowRow >= mapRow || nowCol >= mapCol || filterArr[nowRow][nowCol] || maps[nowRow][nowCol] === 'X') continue;
                if(maps[nowRow][nowCol] === 'L') result = count + 1
                queue.push([nowRow, nowCol, count + 1])
                filterArr[nowRow][nowCol] = true
            }
            if(result !== -1) break;
        }
        return result
    }
    
    // 출구 BFS
    function enterBFS(row, col){
        const queue = [[row, col, 0]]
        const dRow = [0, 1, 0, -1]
        const dCol = [1, 0, -1, 0]
        // 2차원 필터 배열 만들기
        const filterArr = []
        for(let row = 0; row < mapRow; row++){
            const arr = new Array(mapRow).fill(false)
            filterArr.push(arr)
        }
        
        
        let result = -1;
        while(queue.length){
            const [row, col, count] = queue.shift()
            
            for(let i = 0; i < 4; i++){
                const nowRow = row + dRow[i]
                const nowCol = col + dCol[i]
                if(nowRow < 0 || nowCol < 0 || nowRow >= mapRow || nowCol >= mapCol || filterArr[nowRow][nowCol] || maps[nowRow][nowCol] === 'X') continue;
                if(maps[nowRow][nowCol] === 'E') result = count + 1
                queue.push([nowRow, nowCol, count + 1])
                filterArr[nowRow][nowCol] = true
            }
            if(result !== -1) break;
        }
        return result
    }
    
    const leverCount = leverBFS(startAt[0], startAt[1])
    const enterCount = enterBFS(leverAt[0], leverAt[1])
    
    if(leverCount !== -1){
        if(enterCount !== -1){
            return leverCount + enterCount
        }
    }
    return -1
}