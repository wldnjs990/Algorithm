function solution(book_time) {
    const times = book_time.map((e=>{
        const start = e[0].split(':').reduce((acc,cur,idx)=>{
            return idx === 0 ? acc + Number(cur) * 60 : acc + Number(cur)
        },0)
        const end = e[1].split(':').reduce((acc,cur,idx)=>{
            return idx === 0 ? acc + Number(cur) * 60 : acc + Number(cur)
        },0)
        return [start, end + 10]
    }))
    times.sort((a, b)=> b[0] - a[0])
    
    const room = []
    while(times.length){
        const now = times.pop()
        const start = now[0]
        const end = now[1]
        
        if(room.length){
            const length = room.length
            for(let i = 0; i < length; i++){
                if(start > room[i]){
                    room[i] = end
                    break
                } else if(start < room[i]){
                    if(i === length - 1) room.push(end)
                    else continue
                } else {
                    if(start >= room[i]){
                        room[i] = end
                        break
                    } else {
                        if(i === length - 1) room.push(end)
                        else continue
                    }
                }
            }
        } else room.push(end)
    }
    return room.length
}