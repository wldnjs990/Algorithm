// 이진탐색 문제
// 절반을 잘라서 내림차순 한 뒤 무적권의 갯수만큼 큰 수들을 제거하고 나머지 적들을 다 더함
// 
function solution(n, k, enemy) {
    let [left, right] = [0, enemy.length];
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