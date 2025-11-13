function solution(info, n, m) {
  // dp[b] = 최소 A 누적 흔적으로, 현재 B 누적 흔적이 b일 때의 값
  // 초기: dp[0] = 0 (아직 아무도 훔치지 않음)
  const INF = 1e9;
  // B 누적 흔적은 m-1 까지만 허용 (m 이상이면 B가 붙잡힘)
  const maxB = m - 1;
  // 만약 m이 0 이라면(이론상 있을 수 있음) B는 바로 붙잡히므로 불가능
  if (m <= 0) return -1;
  // dp 배열 초기화
  let dp = new Array(m).fill(INF);
  dp[0] = 0;

  for (const [aTrace, bTrace] of info) {
    const next = new Array(m).fill(INF);
    for (let b = 0; b < m; b++) {
      if (dp[b] === INF) continue; // 도달 불가 상태
      const curA = dp[b];

      // 1) 이 물건을 A가 훔침 -> A 누적 증가, B는 그대로
      const newA = curA + aTrace;
      const newB = b;
      // A가 붙잡히지 않아야 함 (newA < n)
      if (newA < n) {
        // newB < m 는 항상 만족(현재 b < m)
        if (next[newB] > newA) next[newB] = newA;
      }

      // 2) 이 물건을 B가 훔침 -> B 누적 증가
      const newA2 = curA;
      const newB2 = b + bTrace;
      // B가 붙잡히지 않아야 함 (newB2 < m)
      if (newB2 < m) {
        if (next[newB2] > newA2) next[newB2] = newA2;
      }
    }
    dp = next;
  }

  // 모든 물건 처리 후 가능한 상태들 중 A 누적의 최솟값을 찾음
  let ans = INF;
  for (let b = 0; b < m; b++) {
    if (dp[b] < ans) ans = dp[b];
  }
  return ans === INF ? -1 : ans;
}
