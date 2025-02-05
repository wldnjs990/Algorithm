function solution(numbers) {
    const result = []
    let stack = []
    let maxnum = 0
    for(let i = numbers.length - 1; i >= 0; i--){
        if(maxnum <= numbers[i]){
            maxnum = numbers[i]
            stack = []
            result.push(-1)
            stack.push(numbers[i])
        } else {
            while(true){
                if(numbers[i] < stack[0]){
                    result.push(stack[0])
                    stack.unshift(numbers[i])
                    break;
                } else {
                    stack.shift()
                }
            }
        }
    }
    result.reverse()
    return result
}