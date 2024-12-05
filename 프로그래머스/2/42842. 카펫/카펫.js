function solution(brown, yellow) {
    const size = brown + yellow;
    const sqrt = Math.sqrt(size); 
    
    for (let height = 3; height <= sqrt; height++) {
        if (size % height === 0) {
            const width = size / height;
            
            if ((width - 2) * (height - 2) === yellow) {
                return [width, height];
            }
        }
    }
}