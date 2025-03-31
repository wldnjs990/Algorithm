function solution(skill, skill_trees) {
    let result = 0
    
    skill_trees.forEach(e=>{
        let able = true
        const skill_tree = e.split('')
        
        // 선행스킬
        const skillArr = skill.split('')
        let sequence = skillArr.shift()
        
        // 사용가능한 스킬트리인지 판별
        for(let i = 0; i < skill_tree.length; i++){
            const nowSkill = skill_tree[i]
            if(sequence === nowSkill){
                sequence = skillArr.shift()
                continue
            }
            if(skillArr.includes(nowSkill)){
                able = false
                break
            }
        }
        if(able) result += 1
    })
    return result
}