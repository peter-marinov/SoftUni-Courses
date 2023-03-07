function printDNA(number){
    let lettersArray = 'ATCGTTAGGG'.split('');

    for(let i = 1; i <= number; i++){
        let [a, b] = lettersArray.splice(0,2)
        if(i === 1 || i % 4 === 1){
            console.log(`**${a}${b}**`);
        } else if (i === 2 || i % 4 === 2) {
            console.log(`*${a}--${b}*`);
        } else if(i === 3 || i % 4 === 3) {
            console.log(`${a}----${b}`);
        } else if(i === 4 || i % 4 === 0){
            console.log(`*${a}--${b}*`);
        }
 
        lettersArray.push(a)
        lettersArray.push(b)
    }
}


printDNA(10)