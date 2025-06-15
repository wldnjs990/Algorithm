// 효율성 테스트 통과 못해서 질문하기에 있는 답 긁어옴
// 좀이따 힙 구현하는법 정리하겠음

function solution(scoville, K) {
    var answer = 0;

    scoville.sort((a, b) => a - b);
    const newScoville = [];
    // scoville 배열의 인덱스
    let index1 = 0; 
    // newScoville 배열의 인덱스
    let index2 = 0; 

    //2개의 리스트를 합쳐서 작은 값 찾기
    const findMin = () =>{
        const a = scoville[index1]
        const b = newScoville[index2]

        if (a === undefined) return newScoville[index2++];
        if (b === undefined) return scoville[index1++];
        return a < b ? scoville[index1++] : newScoville[index2++];
    }

    //조리가 가능 할때 까지
    while(scoville.length - index1 + newScoville.length - index2 > 0){

        //가장 안매운 음식이 K이상일때
        const min1 = findMin()
        if (min1 >= K) return answer

        //마지막 남은 요리가 K보다 안매웟을때
        const min2 = findMin()
        if(min2 === undefined) return -1

        //새로운 요리를 만들어 newScoville에 추가
        const mix = min1+min2*2
        newScoville.push(mix)
        answer++
    }
}