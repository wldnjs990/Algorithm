function solution(food) {
    food.shift()
    let foods = ''
    food.forEach((e, idx)=>{
        let now = idx + 1
        if(e % 2 !== 0) foods += now.toString().repeat(e / 2)
        else foods += now.toString().repeat(Math.floor(e / 2))
    })
    return foods + 0 + foods.split('').reverse().join('')
}