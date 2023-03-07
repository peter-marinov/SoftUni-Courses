function oddAndEvenSums(inputNumber) {
    let oddSum = 0;
    let evenSum = 0;
    let numbers = inputNumber.toString().split('').map(Number);

    for (let i = 0; i < numbers.length; i++) {
        if (numbers[i] % 2 === 0) {
            evenSum += numbers[i];
        } else {
            oddSum += numbers[i];
        }
    }

    return `Odd sum = ${oddSum}, Even sum = ${evenSum}`;
}

console.log(oddAndEvenSums(1000435));