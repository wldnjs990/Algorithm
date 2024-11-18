function solution(n, m) {
    let low = n > m ? m : n;
    let big = n > m ? n : m;
    let temp;
    while (low > 0){
        temp = low
        low = big % low
        big = temp
    }
    return [big, n * m / big]
}