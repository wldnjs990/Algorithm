function solution(prices) {
    let result = []
    for(let idx = 0; idx < prices.length; idx++){
        let count = 0
        if(idx === prices.length - 1) {
            result.push(0)
            continue
        }
        for(let next = idx + 1; next < prices.length; next++){
            if(prices[idx] <= prices[next]) {
                count += 1
            } else {
                count += 1
                break
            }
        }
        result.push(count)
    }
    return result
}