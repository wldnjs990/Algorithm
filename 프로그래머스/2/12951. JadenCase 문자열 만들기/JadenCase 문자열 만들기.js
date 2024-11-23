function solution(s) {
    return s.split(" ").map(e => {
        if(e.length === 0) return e
        const result = e.toLowerCase().split("")
        result[0] = result[0].toUpperCase()
        return result.join("")
    }).join(" ")
}