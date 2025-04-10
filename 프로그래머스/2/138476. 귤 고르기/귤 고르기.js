// 귤 박스 tangerine에서 k개만 따로 빼서 담을때 서로 다른 종류의 수가 최소인 값을 구하라.
// 해쉬 자료형에 담아서 value값만 빼고 큰 값 부터 k에 빼주면서 최소 종류 구하면 될듯

function solution(k, tangerine) {
    const hash = {}
    tangerine.sort()
    for(let i = 0; i < tangerine.length; i++){
        const now = tangerine[i]
        if(hash[now]) hash[now] += 1
        else hash[now] = 1
    }
    
    const values = Object.values(hash).sort((a, b) => b - a)
    
    let result = 0
    for(let i = 0; i < values.length; i++){
        k -= values[i]
        result += 1
        if(k <= 0) return result
    }
    return result
    
}