function solution(clothes) {
    const hash = {}
    clothes.forEach(e=>{
        if(hash[e[1]]) {
            hash[e[1]] += 1
        } else {
            hash[e[1]] = 1
        }
    })
    const hashKeys = Object.keys(hash)
    if(hashKeys.length === 1) return clothes.length
    
    return hashKeys.reduce((acc, cur)=>{
        return acc * (hash[cur] + 1)
    }, 1) - 1
}