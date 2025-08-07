function solution(a, d, included) {
    let arr = []
    let result = 0
    included.forEach((e, idx)=>{
        arr.push(a + d * idx)
        if(e){
            result += arr[idx]
        }
    })
    return result
}