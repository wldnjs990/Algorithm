function solution(numbers) {
    numbers.sort((a, b)=>{
        const A = String(a)
        const B = String(b)
        if(Number(A + B) > Number(B + A)) return -1
        else return 1
    })
    if(numbers.join('').replaceAll('0', '').length === 0) return '0'
    else return numbers.join('')
}