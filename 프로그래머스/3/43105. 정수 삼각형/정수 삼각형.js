function solution(triangle) {
    const DP = triangle.pop()
    for(let i = triangle.length - 1; i >= 0; i--){
        for(let j = 0; j < triangle[i].length; j++){
            DP[j] = Math.max(DP[j], DP[j + 1]) + triangle[i][j]
        }
    }
    return DP[0]
}
