function solution(word) {
    const spells = ['', 'A', 'E', 'I', 'O', 'U']
    
    const result = []
    function DFS(num, item){
        // 숫자 길이가 마지막에 달했을때 현재 문자 결과에 push하기
        if(num === 0){
            result.push(item)
            return
        }
        // 다음 문자 자리에 spell 하나씩 대입하기
        for(let i = 0; i < 6; i++){
            DFS(num - 1, `${item}${spells[i]}`)
        }
    }
    DFS(5, '')
    
    // 중복되는 배열값 제거 후 인덱스 찾기
    const sortResult = [...new Set(result)].sort()
    return sortResult.indexOf(word)
}