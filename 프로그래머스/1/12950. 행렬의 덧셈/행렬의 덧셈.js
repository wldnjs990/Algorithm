function solution(arr1, arr2) {
    return arr1.map((e, e_i) => e.map((j, j_i) => j + arr2[e_i][j_i]))
}