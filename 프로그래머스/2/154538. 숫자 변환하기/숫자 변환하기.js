function solution(x, y, n) {
    const queue = [[y, 0]]
    
    while(queue.length){
        const [y, count] = queue.shift()
        if(y === x) return count
        if(y % 3 === 0 && y / 3 >= x) queue.push([y / 3, count + 1])
        if(y % 2 === 0 && y / 2 >= x) queue.push([y / 2, count + 1])
        if(y - n >= x) queue.push([y - n, count + 1])
    }
    
    return -1
}