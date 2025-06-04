function solution(board) {
    let o = 0;
    let x = 0;
    board = board.map((e)=>{
        return e.split('')
    })
    for(let i = 0; i < board.length; i++){
        for(let j = 0; j < board[0].length; j++){
            if(board[i][j] === 'O') o += 1
            else if(board[i][j] === 'X') x += 1
        }
    }
    // O, X 갯수가 정상적인지 1차 검사
    if(o === 0 && x === 0) return 1
    if(o - x !== 0 && o - x !== 1) return 0
    
    const dx = [1, 1, 0, -1, -1, -1, 0, 1]
    const dy = [0, 1, 1, 1, 0, -1, -1, -1]
    let xBingo = false
    let oBingo = false
    // DFS로 빙고 카운트 찾기
    function DFS(x, y, target, count, map, dir){
        const nx = x + dx[dir]
        const ny = y + dy[dir]
        if(nx >= 0 && ny >= 0 && nx < board[0].length && ny < board.length && map[ny][nx] && board[ny][nx] === target){
            if(count < 3){
                count += 1
                map[ny][nx] = false
                if(count === 3) {
                    if(target === 'X'){
                        xBingo = true
                    } else if(target === "O"){
                        oBingo = true
                    }
                }
                else DFS(nx, ny, target, count, map, dir) 
            }
        }
    }
    
    for(let y = 0; y < board.length; y++){
        for(let x = 0; x < board.length; x++){
            for(let i = 0; i < 8; i++){
                const map = new Array(board.length).fill('').map(e=>{
                    return new Array(board[0].length).fill(true)
                })
                if(board[y][x] === 'O'){
                    DFS(x, y, "O", 1, map, i)
                } else if(board[y][x] === 'X'){
                    DFS(x, y, "X", 1, map, i)
                }
            }
        }
    }
    console.log(oBingo,xBingo)
    if(oBingo && xBingo) return 0
    if(xBingo && o !== x) return 0
    if(oBingo && o !== x + 1) return 0
    return 1
}