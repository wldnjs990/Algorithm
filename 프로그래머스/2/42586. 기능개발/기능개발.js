function solution(progresses, speeds) {
    const result = []
    while(progresses.length){
        for(let i = 0; i < progresses.length; i++){
            progresses[i] += speeds[i]
        }
        let count = 0
        while(progresses[0] >= 100){
            progresses.shift()
            speeds.shift()
            count += 1
        }
        if(count > 0) result.push(count)
    }
    return result
}