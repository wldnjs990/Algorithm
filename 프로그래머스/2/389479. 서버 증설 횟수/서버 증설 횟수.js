function solution(players, m, k) {
    // 총 증설 횟수
    let result = 0
    // 운영중인 서버
    const queue = []
    // 게임 운영
    for(let i = 0; i < 24; i++){
        const needServer = Math.floor(players[i] / m)
        while(queue.length && queue[0] === i){
            queue.shift()
        }
        while(queue.length < needServer){
            queue.push(i + k)
            result += 1
        }
    }
    return result;
}