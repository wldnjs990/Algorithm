function solution(numbers) {
    let result = 0
    for(let i = 0; i < 10; i++){
        result += i
    } 
    for(let i = 0; i < numbers.length; i++){
        result -= numbers[i]
    }
    return result
}