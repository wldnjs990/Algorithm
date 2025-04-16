function solution(n)
{
    return (n.toString().split('')).reduce((acc, cur)=>{return acc + Number(cur)}, 0)
}