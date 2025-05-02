// 시간복잡도는 전혀 문제 없는거 같으니 객체 자료형으로 담아서 풀면 되겠는데?
function solution(n, w, num) {
    const map = {}
    for(let i = 0; i < w; i++){
        map[i] = [];
    }
    let start = 1;
    let direction = true
    while(n >= start){
        if(direction){
            for(let i = 0; i < w; i++){
                if(start > n) continue;
                map[i].push(start)
                start += 1
            }
            direction = !direction
        } else {
            for(let i = w - 1; i >= 0; i--){
                if(start > n) continue;
                map[i].push(start)
                start += 1
            }
            direction = !direction
        }
    }
    for(let key in map){
        let count = 1;
        const now = [...map[key]]
        while(now.length){
            if(now.pop() === num){
                return count
            } else {
                count += 1
            }
        }
    }
}