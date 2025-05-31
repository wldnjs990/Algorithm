function solution(n) {
    let answer = 0;
    
    let arr = Array(n+1).fill(true);
    
    for(let i = 2; i <= Math.sqrt(n); i++) {
        if(arr[i]) {
            for(let j = i*i; j <= n; j += i) {
                arr[j] = false;
            }
        }
    }
    for(let i = 2; i <= n; i++)
        if(arr[i] !== false) answer++;
    return answer;
}