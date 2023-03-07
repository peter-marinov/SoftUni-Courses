function solve(firstNumber, lastNumber) {
    let sum = null;
    let numberArray = [];
    for (let i = firstNumber; i <= lastNumber; i++) {
        sum += i;
        numberArray.push(i);
    }

    console.log(...numberArray);
    console.log(`Sum: ${sum}`)
}

solve(5, 10)