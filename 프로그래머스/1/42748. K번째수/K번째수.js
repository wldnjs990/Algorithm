function solution(array, commands) {
    const result = []
    commands.forEach(e=>{
        const start = e[0] - 1
        const end = e[1] - 1
        const point = e[2] - 1
        const slice = array.filter((e, idx)=>{
            if(idx >= start && idx <= end){
                return e
            }
        })
        result.push(slice.sort((a, b) => a - b)[point])
    })
    return result
}