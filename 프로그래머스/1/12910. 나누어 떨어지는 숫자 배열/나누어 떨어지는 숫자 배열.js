function solution(arr, divisor) {
    const result = arr.filter((e)=>{
        if(e % divisor === 0) return true
        return false
    }).sort((a, b)=>a-b)
    return result.length > 0 ? result : [-1]
}