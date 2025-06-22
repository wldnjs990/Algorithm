function solution(order) {
    let truck = 0;
    let main_trail_index = 1;

    const sub_trail = [];

    for(const o of order) {
        while(main_trail_index <= o) {
            sub_trail.push(main_trail_index++);
        }
        if(sub_trail.at(-1) !== o) break;
        sub_trail.pop();
        truck++;
    }
    return truck;
}