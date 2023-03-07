function solve(inputArray, number) {
    let firstElement = undefined;
    for (let i = 0; i < number; i++) {
        firstElement = inputArray.shift();
        inputArray.push(firstElement);
    }
    
    console.log(...inputArray);
}

solve([2, 4, 15, 31], 5)
