// p랑 y의 갯수가 같으면 true, 아니면 false 출력

function solution(s){
    const S = s.toUpperCase()
    let p = 0
    let y = 0
    for(let i = 0; i < s.length; i++){
        if(S[i] === 'P') p += 1
        else if(S[i] === 'Y') y += 1
    }
    return p === y ? true : false
}