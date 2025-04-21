function solution(arr) {
    const map = {0 : 0, 1 : 0}
    
    function DFS(arr){
        const num = arr[0][0] === 0 ? 1 : 0;
        // 쿼드압축 가능하면 yes가 true, 아니면 false
        let yes = true
        for(let i = 0; i < arr.length; i++){
            if(arr[i].includes(num)){
                // 쿼드압축 못 할때
                const half = arr.length / 2
                const one = []
                const two = []
                const three = []
                const four = []
                arr.forEach((now, idx)=>{
                    const nd = [...now]
                    const st = nd.splice(0, half)
                    if(idx < half){
                        one.push(st)
                        two.push(nd)
                    } else {
                        three.push(st)
                        four.push(nd)
                    }
                })
                DFS(one)
                DFS(two)
                DFS(three)
                DFS(four)
                // 쿼드압축 안될시 yes변수 false로 바꾸기
                yes = false
                break
            }
        }
        // 쿼드압축 될 때(yes가 true일때)
        if(yes){
            map[arr[0][0]] += 1
        }
    }
    DFS(arr)
    
    return [map[0], map[1]]
}