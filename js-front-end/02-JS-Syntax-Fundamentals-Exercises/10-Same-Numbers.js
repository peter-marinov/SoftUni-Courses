function solve(number) {
    let sum = 0;
    let isAllNumbersEqual = true;
    let numberAsString = String(number);
    
    for (let i = 0; i < numberAsString.length - 1; i++) {
        if (numberAsString[i] !== numberAsString[i + 1]) {
            isAllNumbersEqual = false;
            // console.log(i)
            // console.log(`${numberAsString[i]} !== ${numberAsString[i + 1]}`)
            break;
        }
    }

    while (number !== 0) {
        sum += number % 10;
        number = parseInt(number / 10);
    }
    
    console.log(isAllNumbersEqual)
    console.log(sum)
}

solve(2222222)