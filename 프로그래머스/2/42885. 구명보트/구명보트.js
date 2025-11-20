function solution(people, limit) {
    people.sort((a, b) => a - b); // 오름차순 정렬
    let left = 0;
    let right = people.length - 1;
    let boats = 0;

    while (left <= right) {
        if (people[left] + people[right] <= limit) {
            left++; // 둘이 같이 탐
        }
        right--; // 무거운 사람은 항상 태움
        boats++;
    }

    return boats;
}
