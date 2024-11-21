function solution(s, n) {
    const str = s.split("")
    return str.map(e => {
        if(e === " ") return e
        const ascii = e.charCodeAt() + n
        const Z = "Z".charCodeAt()
        const z = "z".charCodeAt()
        const A = "A".charCodeAt()
        const a = "a".charCodeAt()
        if(e.toUpperCase() === e){
            if(ascii > Z){
                return String.fromCharCode(A + (ascii - Z) - 1)
            } else {
                return String.fromCharCode(ascii)
            }
        } else {
            if(ascii > z){
                return String.fromCharCode(a + (ascii - z) - 1)
            } else {
                return String.fromCharCode(ascii)
            }
        }
    }).join("")
}