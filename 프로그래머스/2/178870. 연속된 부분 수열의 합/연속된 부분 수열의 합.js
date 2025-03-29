function solution(sequence, k) {
    const sequenceLen = sequence.length
    const result = []
    
    // BinarySearch
    let start = 0
    let total = 0
    for(let end = 0; end < sequence.length; end++){
        total += sequence[end]
        
        while(total > k){
            total -= sequence[start]
            start += 1
        }
        if(total === k){
            result.push([start, end])
        }
    }
    
    return result.reduce((acc, cur)=>{
        const accLen = acc[1] - acc[0]
        const curLen = cur[1] - cur[0]
        if(accLen > curLen){
            return cur
        } else if(accLen < curLen){
            return acc
        } else {
            return acc[0] > cur[0] ? cur : acc
        }
    })
}