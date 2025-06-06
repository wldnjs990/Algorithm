function solution(n, lost, reserve) {
    for(let i = 0; i < lost.length; i++){
        for(let j = 0; j < reserve.length; j++){
            if(lost[i] === reserve[j] && lost[i] !== ''){
                lost[i] = ''
                reserve[j] = ''
            }
        }
    }
    const lFilter = lost.filter(e=>{
        if(e === '') return false
        else return true
    })
    const rFilter = reserve.filter(e=>{
        if(e === '') return false
        else return true
    })
    let minus = 0
    lFilter.sort((a, b)=>a-b)
    rFilter.sort((a, b)=>a-b)
    lFilter.forEach(e=>{
        let isTrue = false
        for(let i = 0; i < rFilter.length; i++){
            if(e === rFilter[i] + 1 || e === rFilter[i] - 1){
                isTrue = true
                rFilter[i] = Infinity
                break
            }
        }
        if(!isTrue) minus += 1
    })
    return n - minus
}