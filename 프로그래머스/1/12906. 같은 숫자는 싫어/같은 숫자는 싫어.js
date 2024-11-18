function solution(arr)
{
    const result = []
    arr.forEach(e => e !== result[result.length - 1] ? result.push(e) : null)
    return result
}