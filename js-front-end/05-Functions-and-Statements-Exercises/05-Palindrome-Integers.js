function palindromeCheck(numbers) {
    let reverseNumber = undefined;
    numbers.forEach(number => {
        reverseNumber = Number(number
            .toString()
            .split('')
            .reverse()
            .join('')
        );

        if (number === reverseNumber) {
            console.log(true)
        } else {
            console.log(false)
        }
    });
}

palindromeCheck([123, 323, 421, 121])