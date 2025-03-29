function solution(priorities, location) {
    let result = 0
    
    while(priorities.length){
        location -= 1
        const max = Math.max(...priorities)
        const now = priorities.shift()
        if(now === max) {
            if(location === -1) {
                return result + 1
            }
            result += 1
        } else {
            priorities.push(now)
        }
        if(location < 0) location = priorities.length - 1
    }
}