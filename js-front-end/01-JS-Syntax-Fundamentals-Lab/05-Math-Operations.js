function solve(firstNumber, secondNumber, operator) {
    let result = null;
    if (operator === '+') {
        result = firstNumber + secondNumber
    } else if (operator === '-') {
        result = firstNumber - secondNumber
    } else if (operator === '*') {
        result = firstNumber * secondNumber
    } else if (operator === '/') {
        result = firstNumber / secondNumber
    } else if (operator === '%') {
        result = firstNumber % secondNumber
    } else  {
        result = firstNumber ** secondNumber
    }

    console.log(result)
}

solve(5, 6, '+')