function solve(number, operator, anotherNumber) {
    let result = null;

    switch(operator) {
        case '+': result = number + anotherNumber; break;
        case '-': result = number - anotherNumber; break;
        case '/': result = number / anotherNumber; break;
        case '*': result = number * anotherNumber; break;
    }

    console.log(result.toFixed(2))
}

solve(5,

    '+',
    
    10)