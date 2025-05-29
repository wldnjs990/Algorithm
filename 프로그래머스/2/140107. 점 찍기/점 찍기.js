function solution(k, d) {
    let result = 0;
    let temp = 0
    let count = 1
    for(let i = 0; i <= d; i += k){
        while(true){
            if(i ** 2 + temp ** 2 <= d ** 2){
                // temp에서 한번 더 키웠을때 d를 넘어가면 지금이 최선인거잖아
               if(i ** 2 + (temp + k) ** 2 > d ** 2){
                   result += count
                   break;
               } else {
                   temp += k
                   count += 1
               }
           } else {
               // temp에서 한번 더 줄였을때 d와 길이가 같아졌으면 줄인 값이 최선이잖아
               if(i ** 2 + (temp - k) ** 2 <= d ** 2){
                   temp -= k
                   count -= 1
                   result += count
                   break;
               } else {
                   temp -= k
                   count -= 1
               }
           }
        }
    }
       
    return result
}