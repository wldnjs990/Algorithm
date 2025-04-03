function solution(board) {
    let X;
    let Y;
    const boardX = board[0].length
    const boardY = board.length
    
    for(let i = 0; i < boardY; i++){
        const row = board[i]
        if(row.indexOf('R') !== -1) {
            X = row.indexOf('R')
            Y = i
            break
        }
    }
    const visited = []
    for(let i = 0; i < boardY; i++){
        visited.push(new Array(boardX).fill(false))
    }
    
    // BFS
    let result = -1
    function BFS(x, y, count = 0){
        const queue = [[x, y, count]]
        
        const dx = [0, 1, 0, -1]
        const dy = [1, 0, -1, 0]
        
        while(queue.length){
            if(result !== -1) break
            let [x, y, count] = queue.shift()
            count += 1
            
            for(let i = 0; i < 4; i++){
                let nx = x + dx[i]
                let ny = y + dy[i]     
                

                if(nx < 0 || ny < 0 || nx >= boardX || ny >= boardY || board[ny][nx] === 'D') continue
                // 현재방향으로 슬라이드
                while(true){
                    nx += dx[i]
                    ny += dy[i]
                    if(nx < 0 || ny < 0 || nx >= boardX || ny >= boardY || board[ny][nx] === 'D') break;
                }
                nx -= dx[i]
                ny -= dy[i]
                // 현재 위치가 G일 경우 result값 업데이트
                if(board[ny][nx] === 'G'){
                    result = count
                    break
                }
                if(visited[ny][nx]) continue
                
                // 현재 위치 방문으로 설정하고 queue 쌓기
                visited[ny][nx] = true
                
                queue.push([nx, ny, count])
            }
        }
    }
    BFS(X, Y)
    return result
}