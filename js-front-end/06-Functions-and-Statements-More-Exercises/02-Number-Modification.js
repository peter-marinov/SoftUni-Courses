function numberModification(number) {
    let numbers = number
        .toString()
        .split('')
        .map(Number);
       
    while (true) {
        const numbersSum = numbers.reduce((a, b) => a + b);
        if (numbersSum / numbers.length > 5) {
            return numbers.join('')
        } else {
            numbers.push(9);
        }
    }
}


console.log(
    numberModification(101)
)