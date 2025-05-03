function solution(phone_number) {
    return phone_number.split('').reverse().map((e, idx)=>{
        if(idx > 3){return "*"}
        else return e
    }).reverse().join('')
}