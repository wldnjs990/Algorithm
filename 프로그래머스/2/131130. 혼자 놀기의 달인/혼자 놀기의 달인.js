// DFS로 풀면 될 거 같은데
// 배열을 순회하면서 각각의 인덱스별 끝까지 진행한 상자의 곱들을 저장해서 거기의 최댓값 구하면 끝?
// 길이도 100이라 시간복잡도는 충분할거 같은데
function solution(cards) {
    const result = []
    function DFS1(idx, cardsClone){
        const st = []
        let now = idx;
        while(cardsClone[now] !== '_'){
            if(cardsClone.includes(cardsClone[now])){
                st.push(cardsClone[now])
                cardsClone[now] = '_'
                // 현재 카드 순번이 cards 안에 숫자로 존재하는 경우 다음 타깃으로 지정
                now = cardsClone.indexOf(now + 1)
            } else {
                break
            }
        }
        return [st, cardsClone]
    }
    // 2번째 상자
    function DFS2(idx, st, cardsClone){
        let now = idx
        const nd = []
        while(now >= 0 && now && cardsClone[now] && cardsClone[now] !== '_'){
            if(cardsClone.includes(cardsClone[now])){
                nd.push(cardsClone[now])
                cardsClone[now] = '_'
                // 현재 카드 순번이 cards 안에 숫자로 존재하는 경우 다음 타깃으로 지정
                now = cardsClone.indexOf(now + 1)
            } else {
                break
            }
        }
        result.push(st.length * nd.length)
    }
    
    for(let i = 0; i < cards.length; i++){
        const res = DFS1(i, [...cards])
        for(let j = 0; j < cards.length; j++){
            DFS2(j, ...res)
        }
    }
    return Math.max(...result)
}