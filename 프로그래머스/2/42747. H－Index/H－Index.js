function solution(citations) {
    let i = 0;
    const sorted = citations.sort((a, b) => b - a)
    while(i + 1 <= sorted[i]) i++;

    return i;
}