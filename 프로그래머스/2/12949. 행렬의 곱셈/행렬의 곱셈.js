function solution(arr1, arr2) {
    const x1 = arr1[0].length
    const y1 = arr1.length
    const x2 = arr2[0].length
    const y2 = arr2.length
    
    const result = []
    for(let i = 0; i < y1; i++){
        const arr = new Array(x2).fill(0)
        result.push(arr)
    }
    for(let i = 0; i < y1; i++){
        for(let j = 0; j < x2; j++){
            for(let k = 0; k < x1; k++){
                result[i][j] += arr1[i][k] * arr2[k][j]
            }
        }
    }
    return result
}