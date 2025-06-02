function solution(priorities, location) {
    const result = []
    const indexArr = new Array(priorities.length).fill(0).map((_,idx)=> idx)
    console.log(indexArr)
    while(priorities.length){
        const now = priorities.shift()
        const index = indexArr.shift()
        
        let isSmall = false
        for(let i = 0; i < priorities.length; i++){
            if(now < priorities[i]) {
                isSmall = true
                break;
            }
        }
        if(isSmall) {
            priorities.push(now)
            indexArr.push(index)
        } else {
            result.push(index)
        }
    }
    return result.indexOf(location) + 1
}