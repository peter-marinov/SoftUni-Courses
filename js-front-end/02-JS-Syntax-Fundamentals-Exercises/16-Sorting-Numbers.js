function solve(numbers) {
    let finalArray = []
    // numbers.sort(function(a, b) {return a - b});
    numbers.sort((a, b) => a - b);
    while ( numbers.length > 0) {
        finalArray.push(numbers.shift())
        finalArray.push(numbers.pop())
    }
    return finalArray
 }

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]));