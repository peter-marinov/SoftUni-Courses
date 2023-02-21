function solve(firstNumber, secondNumber, thirdNumber) {
    let biggestNumber = null;
    if (firstNumber > secondNumber && firstNumber > thirdNumber) {
        biggestNumber = firstNumber;
    } else if (secondNumber > firstNumber && secondNumber > thirdNumber) {
        biggestNumber = secondNumber;
    } else {
        biggestNumber = thirdNumber;
    }

    console.log(`The largest number is ${biggestNumber}.`)
}


solve(5, -3, 16)