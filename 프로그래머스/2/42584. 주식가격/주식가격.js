function solution(prices) {
    const queue = []
    for(let i = 0; i < prices.length; i++){
        let count = 0
        while(i + count < prices.length - 1 && prices[i] <= prices[i + count]){
            count += 1
        }
        queue.push(count)
    }
    return queue
}