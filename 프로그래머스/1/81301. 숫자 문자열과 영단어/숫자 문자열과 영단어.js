function solution(s) {
    let result = ""
    let spell = ""
    const map = {
        zero : 0,
        one : 1,
        two : 2,
        three : 3,
        four : 4,
        five : 5,
        six : 6,
        seven : 7,
        eight : 8,
        nine : 9
    }
    
    for(let i of s){
        if(!isNaN(i)){
            result += i;
        } else {
            spell += i;
            if(map[spell] !== undefined){
                result += map[spell];
                spell = ''
            }
        }
    }
    return Number(result)
}