function solution(n, arr1, arr2) {
    // 이진수 2차원 배열 구하기
    function getBinaryArrs(n, arr){
        // 반환할 이진수 2차원 배열
        const binaryArrs = []
        // arr1, arr2 반복문 돌리기
        for(let now = 0; now < arr.length; now++){
            // 현재 정수
            let nowNum = arr[now]
            // 이진수 1차원 배열
            const binaryArr= []
            // 현재 nowNum 값에서 2의 i제곱을 뺄 수 있는지 검증하는 반복문
            for(let i = n - 1; i >= 0; i--){
                if(i !== 0){
                    // nowNum에 2의 i제곱을 뺄 수 있으면 이진수 1 = '#', 현재값에서 빼기
                    if(nowNum - (2 ** i) >= 0){
                        binaryArr.push('#')
                        nowNum -= 2 ** i
                    // 안되면 이진수 0 = ' '
                    } else {
                        binaryArr.push(' ')
                    }
                } else {
                    // 마지막 남은 nowNum이 1이면 이진수 1 = '#'
                    if(nowNum === 1){
                        binaryArr.push('#')
                    // 0이면 이진수 0 = ' '
                    } else {
                        binaryArr.push(' ')
                    }
                }
            }
            // 이진수 2차원 배열에 이진수 1차원 배열 넣기
            binaryArrs.push(binaryArr)
        }
        // 다 만든 이진수 2차원 배열 반환하기
        return binaryArrs
    }
    // arr1과 arr2 이진수 배열 반환
    const binaryA = getBinaryArrs(n, arr1)
    const binaryB = getBinaryArrs(n, arr2)
    
    // 조합한 결과 반환
    return binaryA.map((arr, row)=>{
        const nowLine = arr.map((item, col)=>{
            if(binaryB[row][col] === '#' || item === '#'){
                return '#'
            } else {
                return ' '
            }
        })
        return nowLine.join('')
    })
}