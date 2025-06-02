function solution(phone_book) {
    const hash = new Set()
    phone_book.sort((a, b)=> a - b)
    
    for(let i = 0; i < phone_book.length; i++){
        for(let j = 0; j < phone_book[i].length; j++){
            if(hash.has(phone_book[i].substr(0, j))) return false
        }
        
        hash.add(phone_book[i])
    }
    
    return true
}