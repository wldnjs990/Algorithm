// 해시를 이용해 유저의 이름을 uid값에 따라 저장하고 uid의 값이 언급될 때 마다 leave, enter, change의 내용을 파악해 닉네임을 그때그때 바꿔주면 어떨까
function solution(record) {
    const user = {}
    const ment = {
        Enter : '들어왔습니다.',
        Leave : '나갔습니다.'
    }
    const log = []
    for(let i = 0; i < record.length; i++){
        const now = record[i].split(' ')
        if(!user[now[1]]) user[now[1]] = now[2]
        else if(now[2] && user[now[1]] !== now[2]) user[now[1]] = now[2]
        if(now[0] !== 'Change')log.push([now[0], now[1]])
    }
    return log.map(e=>{
        return  user[e[1]]+'님이'+' '+ment[e[0]]
    })
}