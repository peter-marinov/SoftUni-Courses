function factorialDivision(firstNum, secondNum) {
    function factorial(number) {
        if (number < 0 ) {
            return -1;
        } else if (number === 0) {
            return 1;
        } else {
            return number * factorial(number - 1);
        }
    }

    result = (factorial(firstNum) / factorial(secondNum)).toFixed(2);

    return result;

    
}

console.log(factorialDivision(5, 2));