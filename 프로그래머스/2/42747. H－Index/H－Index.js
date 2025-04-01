function solution(citations) {
    // H-index : 자신 이상으로 인용된 논문의 숫자 >= 자신 && 자신 >= 자신 보다 낮게 인용된 논문의 숫자
    // 그런 논문 중에서 가장 큰 수를 리턴해야함
    const result = []
    const max = Math.max(...citations)
    
    for(let i = 0; i <= max; i++){
        const h = i
        let low = 0
        let height = 0
        citations.forEach(now=>{
            if(now >= h) {
                height += 1
            } else {
                low += 1
            }
        })
        if(h <= height && h >= low) result.push(h)
    }
    
    return Math.max(...result)
}