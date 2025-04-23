function solution(arr) {
    const min = Math.min(...arr)
    if(arr.length > 1){
        return arr.filter(e=> {if(e !== min) return e})
    } else {
        return [-1]
    }
}