function solution(my_string) {
    const answer = []
    const endIdx = my_string.length
    for(let i = 0; i < endIdx; i++){
        answer.push(my_string.slice(i, endIdx))
    }
    return answer.sort()
}