function solution(storey) {
    const storeyArr = storey.toString().split('').reverse().map(e=>{
        return Number(e)
    })
    
    let result = 0
    for(let i = 0; i < storeyArr.length; i++){
        if(i === storeyArr.length - 1) {
            if(storeyArr[i] > 5){
                result += (10 - storeyArr[i] + 1)
            } else {
                result += storeyArr[i];    
            }
            continue;
        }
        const case1 = storeyArr[i] + (10 - storeyArr[i+1])
        const case2 = (10 - storeyArr[i]) + (10 - storeyArr[i+1] - 1)
        const case3 = (10 - storeyArr[i]) + (storeyArr[i+1] + 1)
        const case4 = storeyArr[i] + storeyArr[i+1]
        const low = Math.min(case1, case2, case3, case4)
        if(storeyArr[i] === 5 && storeyArr[i+1] === 5){
            result += storeyArr[i]
            storeyArr[i+1] += 1
        } else if(low === case1 || low === case4){
            result += storeyArr[i]
        } else if(low === case2 || low === case3){
            result += (10 - storeyArr[i])
            storeyArr[i+1] += 1
        }
    }
    
    return result
    
}