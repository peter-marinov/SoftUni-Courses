// printStars(5);

// function printStars(count) {
//     console.log('*'.repeat(count));
// }

// printStars(3);

// let printStarsVariable = function (count) {
//     console.log('*'.repeat(count));
// }

// printStarsVariable(4);

let numbers = [1, 2, 3, 4, 5, 6, 7];
numbers
    .map(multiplyByTwo);

function multiplyByTwo(value) {
    console.log(value * 2);
    return value * 2;

}