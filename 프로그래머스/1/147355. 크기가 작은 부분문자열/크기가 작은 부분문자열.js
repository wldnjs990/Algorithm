function solution(t, p) {
    let word = [];
    let count = 0;
    for(spell of t){
        word.push(spell);
        if(word.length === p.length){
            if(word.join("") <= p){
                count += 1;
            }
            word.shift()
        }
    }
    return count
}