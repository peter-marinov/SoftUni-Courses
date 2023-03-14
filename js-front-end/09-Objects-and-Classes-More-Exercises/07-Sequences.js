function sequences(input) {
    let numbersArray = [];
    for (const line of input) {
        let numbers = line
            .slice(1, line.length -1)
            .split(', ')
            .map(num => Number(num))
            .sort((a, b) => b - a);

        for (const currentNumbers of numbersArray) {
            if (currentNumbers.toString() === numbers.toString()) {
                let index = numbersArray.indexOf(currentNumbers);
                numbersArray.splice(index, 1);
                isSame = true;
                break
            }
        }

        numbersArray.push(numbers);
    }

    for (const iterator of numbersArray) {
        console.log(iterator);
    }
}

sequences(["[-3, -2, -1, 0, 1, 2, 3, 4]",

"[10, 1, -17, 0, 2, 13]",

"[4, -3, 3, -2, 2, -1, 1, 0]"]);