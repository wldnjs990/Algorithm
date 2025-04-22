// 윤년이 뭔데
// 원래 짝수 = 30일, 홀수 = 31일이잖아
// 2월은 29일 까지 있고
// 8월 부터 갑자기 규칙 뒤집혀서 짝수 = 31일, 홀수 = 30일로 바
// 윤년이 뭔데
function solution(a, b) {
    const week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    let day = 0
    for(let i = 1; i < a; i++){
        if(i === 2){
            day += 29
        } else if(i < 8){
            if(i % 2 === 0){
                day += 30
            } else {
                day += 31
            }
        } else if(i >= 8) {
            if(i % 2 === 0){
                day += 31
            } else {
                day += 30
            }
        }
    }
    day += b - 1 
    console.log(day)

    return week[(day) % 7]
}