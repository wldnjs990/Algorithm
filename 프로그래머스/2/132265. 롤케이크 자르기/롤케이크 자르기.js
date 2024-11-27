function solution(topping) {
    let count = 0;
    const st = new Map();
    const nd = new Map();
    st.set(topping[0], 1)
    for(let i = 1; i < topping.length; i++){
        nd.get(topping[i]) ? nd.set(topping[i], nd.get(topping[i]) + 1) : nd.set(topping[i], 1)
    }
    for(let i = 1; i < topping.length - 1; i++){
        st.get(topping[i]) ? st.set(topping[i], st.get(topping[i]) + 1) : st.set(topping[i], 1)
        if(nd.get(topping[i])){
            nd.set(topping[i], nd.get(topping[i]) - 1)
            if(nd.get(topping[i]) === 0) nd.delete(topping[i])
        }
        if(st.size === nd.size) count += 1
    }
    return count
}