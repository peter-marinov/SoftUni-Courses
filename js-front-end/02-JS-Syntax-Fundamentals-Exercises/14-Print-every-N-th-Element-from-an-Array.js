function solve(inputArray, step) {
    let newArray = [];
    for (let i = 0; i < inputArray.length; i += step) {
        newArray.push(inputArray[i]);
    }
    
    return newArray;
}

solve(['5', '20', '31', '4', '20'], 2)

