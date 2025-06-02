function solution(array, commands) {
    const result = []
    for(let i = 0; i < commands.length; i++){
        const now = commands[i]
        const start = now[0] - 1
        const num = now[1] - 1
        const location = now[2] - 1
        result.push(array.slice(start, num + 1).sort((a, b)=>a-b)[location])
    }
    return result
}