const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    let str = input[0];
    console.log(str.split('').map(e=>{
        if(e === e.toUpperCase()) return e.toLowerCase()
        else return e.toUpperCase()
    }).join(''))
});