function solution(nums) {
    const hash = {}
    for(let i = 0; i < nums.length; i++){
        if(!hash[nums[i]]) hash[nums[i]] = 1
        else hash[nums[i]] += 1
    }
    const length = Object.values(hash).length
    return length < nums.length / 2 ? length : nums.length / 2
}