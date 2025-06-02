function solution(arr){
    return arr.reduce((acc, cur)=>{
        if(!acc.length || acc[acc.length - 1] !== cur){
            // push는 넣은 숫자를 반환하는구나....
            acc.push(cur)
            return acc
        } else return acc
    }, [])
}