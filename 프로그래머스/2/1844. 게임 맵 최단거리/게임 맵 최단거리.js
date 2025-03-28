function solution(maps) {
    const mapRow = maps.length
    const mapCol = maps[0].length
    
    // BFS
    const dx = [0, 1, 0, -1]
    const dy = [1, 0, -1, 0]
    
    const visitedArr = []
    for(let y = 0; y < mapRow; y++){
        visitedArr.push(new Array(mapCol).fill(false))
    }
    
    const answerArr = []
    function BFS(x, y){
        const queue = [[x, y, 1]]
        
        while(queue.length){
            const [x, y, ctn] = queue.shift()
            
            for(let i = 0; i < 4; i++){
                const nx = x + dx[i]
                const ny = y + dy[i]
                
                if(nx < 0 || ny < 0 || nx >= mapCol || ny >= mapRow || maps[ny][nx] === 0 || visitedArr[ny][nx]) continue;
                
                visitedArr[ny][nx] = true
                if(nx === mapCol - 1 && ny === mapRow - 1) answerArr.push(ctn + 1)
                queue.push([nx, ny, ctn + 1])
            }
        }
    }
    BFS(0, 0)
    
    
    return answerArr.length ? Math.min(...answerArr) : -1
}