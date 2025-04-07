function solution(d, budget) {
    let count = 0
    d.sort((a, b)=>a-b)
    console.log(d)
    while(true){
        budget -= d.shift()
        if(budget < 0) {
            return count
        } else if(budget === 0){
            return count + 1
        } else if(d.length === 0){
            return count + 1
        } else {
            count += 1    
        }
    }
}