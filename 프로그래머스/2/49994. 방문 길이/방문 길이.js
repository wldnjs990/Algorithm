function solution(dirs) {
    let x = 5;
    let y = 5;
    const set = new Set()
    for(let i of dirs){
        if(i === "U"){
            if(y < 10) {
                y += 1
                set.add(`${x} ${y} ${x} ${y - 1}`)
            }
        }
        if(i === "D"){
            if(y > 0) {
                y -= 1
                set.add(`${x} ${y + 1} ${x} ${y}`)
            }
        }
        if(i === "R"){
            if(x < 10) {
                x += 1
                set.add(`${x} ${y} ${x - 1} ${y}`)
            }
        }
        if(i === "L"){
            if(x > 0) {
                x -= 1
                set.add(`${x + 1} ${y} ${x} ${y}`)
            }
        }
    }
    return [...set].length
}