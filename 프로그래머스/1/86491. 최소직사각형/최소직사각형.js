// 2차원 배열 순회하면서 1차원 배열의 크기를 비교해서 거기서 나오는 큰 숫자는 큰 숫자들이랑 비교, 작은 숫자들은 작은 숫자들이랑 비교하면서 값 도출하면 되지 않을까
function solution(sizes) {
    const a = []
    const b = []
    sizes.forEach(e=>{
        if(e[0] < e[1]) e.reverse()
        a.push(e[0])
        b.push(e[1])
    })
    console.log(a, b)
    return Math.max(...a) * Math.max(...b)
}