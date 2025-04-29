function solution(left, right) {
    let result = 0;
    for(let i = left; i <= right; i++){
        let count = 0
        const sqrt = Math.floor(Math.sqrt(i))
        // 짝수인 경우 : 제곱근의 제곱이 현재 정수가 아닌 경우
        // 홀수인 경우 : 제곱근의 제곱이 현재 정수인 경우
        if(sqrt ** 2 === i) result -= i
        else result += i
    }
    return result
}