function solution(N, stages) {
    const totalPlayers = stages.length;
    const stageFailure = [];
    const stageCount = new Array(N + 2).fill(0); // 0은 안 씀

    // 각 스테이지에 도달한 플레이어 수 저장
    for (const s of stages) {
        stageCount[s]++;
    }

    let playersRemaining = totalPlayers;

    for (let stage = 1; stage <= N; stage++) {
        const reached = playersRemaining;
        const stuck = stageCount[stage];

        const failure = reached === 0 ? 0 : stuck / reached;

        stageFailure.push([stage, failure]);
        playersRemaining -= stuck;
    }

    stageFailure.sort((a, b) => b[1] - a[1]); // 실패율 기준 내림차순

    return stageFailure.map(([stage]) => stage);
}
