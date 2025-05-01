// 2차원 배열 순회하면서 1차원 배열의 크기를 비교해서 거기서 나오는 큰 숫자는 큰 숫자들이랑 비교, 작은 숫자들은 작은 숫자들이랑 비교하면서 값 도출하면 되지 않을까
function solution(sizes) {
    let long = 0;
    let short = 0;
    sizes.forEach((e)=>{
        let eLong;
        let eShort;
        if(e[0] > e[1]){
            eLong = e[0]
            eShort = e[1]
        } else {
            eLong = e[1]
            eShort = e[0]
        }
        if(eLong > long) long = eLong;
        if(eShort > short) short = eShort;
    })
    return long * short
}