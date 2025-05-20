function solution(new_id) {
    // 1단계
    new_id = new_id.toLowerCase()
    // 2단계
    let filter2 = new_id.split('').filter((e, idx)=>{
        if(Number(e) + 1 > 0) return true
        const target = e.charCodeAt()
        return 97 <= target && target <= 122 || e === '-' || e === '_' || e === '.'
    })
    // 3단계
    let point = false
    const index = []
    const filter3 = filter2.filter((e, idx) => {
        if(e === '.') {
            if(point === true) return false
            else point = true
        }
        else {
            if(point === true) point = false
        }
        return true
    })
    // 4단계
    if(filter3[0] === '.') filter3.shift()
    if(filter3[filter3.length - 1] === '.') filter3.pop()
    // 5단계
    if(!filter3.length) filter3.push('a')
    // 6단계
    if(filter3.length > 15) {
        filter3.splice(15, filter3.length - 15)
        if(filter3[filter3.length - 1] === '.') filter3.pop()
    }
    // 7단계
    if(filter3.length > 3) return filter3.join('')
    else {
        while(filter3.length < 3){
            filter3.push(filter3[filter3.length - 1])
        }
        return filter3.join('')
    }
}