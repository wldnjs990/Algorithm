// n이 0 이하가 될 때 까지 진행해서 가장 오래 버티는 라운드를 구하는 문제
// 일단 무적권 안 쓰고 끝까지 진행
// 해당 라운드에서 무적권을 쓸만한 큰 숫자들만 추려서 그만큼 n을 보충해주고 이어서 진행
// 이어서 진행된 라운드에서 나온 가장 큰 수들을 이전에 무적권을 쓴 가장 작은수랑 빼서 커버 가능하면 서로 값 변경해주기
// 끝 까지 간 길이 구하면 끝
function solution(n, k, enemy) {
    let [left, right] = [0, enemy.length]
    let mid = Math.floor((left + right) / 2)
    while(left <= right){
        const round = enemy.slice(0, mid).sort((a, b) => b - a)
        let skill = k
        const totalEnemy = round.reduce((acc, cur)=>{
            if(skill > 0){
                skill--
                return acc
            } else {
                return acc + cur
            }
        }, 0)
        if(n - totalEnemy >= 0){
            left = mid + 1
        } else {
            right = mid - 1
        }
        mid = Math.floor((left + right) / 2)
    }
    return left - 1
}