function solution(babbling) {
    const ableWord = ['aya', 'ye', 'woo', 'ma']
    let result = 0
    babbling.forEach(babble => {
        let nowBabble = babble
        for(word of ableWord){
            nowBabble = nowBabble.replaceAll(word, 'ㅎ')
            let flag = false
            for(let i = 0; i < nowBabble.length; i++){
                if(nowBabble[i] === 'ㅎ'){
                    if(flag){
                        nowBabble += '탈락'
                        flag = false
                    } else {
                        flag = true
                    }
                } else {
                    flag = false
                }
            }
            nowBabble = nowBabble.replaceAll('ㅎ', 'ㅇ')
        }
        nowBabble = nowBabble.replaceAll('ㅇ', '')
        if(nowBabble.length === 0) result += 1
    })
    return result
}