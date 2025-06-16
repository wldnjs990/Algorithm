// 진짜 1도 모르겠어서 gpt 봤수다.

function solution(users, emoticons) {
  const discounts = [10, 20, 30, 40];
  let maxSubscribers = 0;
  let maxRevenue = 0;

  function DFS(depth, path){
    // 뭐든 할인율 길이 채우면 users 계산 시작
    if (depth === emoticons.length) {
      evaluate(path);
      return;
    }
    // 할인율 [10, 10, 10, 10, 10, 10, 10] 부터 [40, 40, 40, 40, 40, 40, 40] 까지 경우의 수 만드는 DFS였네 아
    for (let d of discounts) {
      path.push(d);
      DFS(depth + 1, path);
      path.pop();
    }
  };

    // 할인율 리스트 받으면 유저 전체 계산 시작
  function evaluate(discountSet){
      // 맴버십이랑 가격
    let subscribers = 0;
    let revenue = 0;

      // 유저 하나에서 희망 할인율과 가격 마지노선 빼와서 계산
    for (let [minDiscount, minSpend] of users) {
      let total = 0;

        // 이모티콘 반복문 돌려서 discountSet(이모티콘 하나마다 붙은 할인율 배열)을 적용한 이모티콘 가격들을 total에 하나씩 쌓기(희망 할인율 미달이면 그 이모티콘은 구매 안하니 if문으로 거르기)
      emoticons.forEach((price, idx) => {
        const discount = discountSet[idx];
        if (discount >= minDiscount) {
          const discountedPrice = price * (1 - discount / 100);
          total += discountedPrice;
        }
      });

        // 해당 유저가 이모티콘 싸이클 돌려서 나온 총 금액이 가격 마지노선 초과하면 맴버십으로 바꾸기
        // 가격 마지노선 안에 들면 총 가격(revenue)에 추가하기
      if (total >= minSpend) {
        subscribers++;
      } else {
        revenue += total;
      }
    }

      // 현재 구해진 맴버십(subscribers)와 현재 최대 맴버십 수(maxSubscribers)의 크기를 비교해 변경할지 그대로 둘 지 정함
      // 만약 맴버십이 같다면 가격을 비교
    if (
      subscribers > maxSubscribers ||
      (subscribers === maxSubscribers && revenue > maxRevenue)
    ) {
      maxSubscribers = subscribers;
      maxRevenue = revenue;
    }
  };

    // 이모티콘 시작 갯수(depth)와 경우에 따른 할인율(path)을 담을 빈 배열을 담아서 DFS 실행
  DFS(0, []);
  return [maxSubscribers, Math.floor(maxRevenue)];
}