function solution(cacheSize, cities) {
    const queue = []
    let result = 0;
    for(let i = 0; i < cities.length; i++){
        const lower = cities[i].toLowerCase()
        if(queue.includes(lower)) {
            const index = queue.indexOf(lower)
            const target = queue.splice(index, 1)
            queue.unshift(target[0])
            result += 1
        } else {
            result += 5
        }
        if(queue.length < cacheSize){
            queue.push(lower)   
        } else {
            queue.push(lower)
            queue.shift()
        }
    }
    return result
}