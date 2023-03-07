function checkIfNumberIsPerfect(number) {
    let halfNumber = number / 2;
    let sum = 0;
    if (!Number.isInteger(halfNumber)) {
        return "It's not so perfect.";
    }

    for (let i = 1; i <= halfNumber; i++) {
        if (number % i === 0) {
            sum += i;
        }
        
    }

    if (sum === number) {
        return "We have a perfect number!"
    } else {
        return "It's not so perfect.";
    }
}

console.log(checkIfNumberIsPerfect(6))