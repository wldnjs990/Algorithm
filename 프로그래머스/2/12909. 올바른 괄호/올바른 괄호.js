function solution(s){
    const queue = []
    if(s[0] === ')' || s[s.length - 1] === '(') return false
    for(let i = 0; i < s.length; i++){
        if(!queue.length){
            if(s[i] === ')') return false
            else queue.push(s[i])
        } else if(s[i] === queue[queue.length - 1]){
            queue.push(s[i])
        } else {
            queue.pop()
        }
    }
    if(queue.length) return false
    else return true
}