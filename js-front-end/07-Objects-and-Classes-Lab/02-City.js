// function cityInfo(city) {
//     let keys = Object.keys(city);
//     for (const key of keys) {
//         console.log(`${key} -> ${city[key]}`);
//     }
// }

// cityInfo({name: "Sofia",

// area: 492,

// population: 1238438,country: "Bulgaria", postCode: "1000"})


let count = 5;
// switch (command) {
//     case 'increment':
//         count++;
//         break;
//     case 'decrement':
//         count--;
//         break;
//     case 'reset':
//         count = 0;
//         break;
// }

const commandParser = {
    increment: (count) => ++count,
    decrement: (count) => --count,
    reset: () => 0,
};

count = commandParser.increment(count);
console.log(count);