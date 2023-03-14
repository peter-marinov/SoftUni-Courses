// let person = {
//     name: 'Kiril',
//     age: 25,
//     colorHair: 'brown',
//     grades: [5, 5, 5],
//     sayHello: function() {
//         return `${this.name} ${this.age}`
//     }
// };

// const keys = Object.keys(person)
// for (const key of keys) {
//     console.log(person[key])
// }

// const values = Object.values(person)
// for (const value of values) {
//     console.log(`Value ${value}`)
// }

// const tuples = Object.entries(person)
// for (const [key, value] of tuples) {
//     console.log(`Key: ${key} Value ${value}`)
// }

// console.log(Object.keys(person))
// console.log(person);

let people = { 
    'Kiril': { age: 25, email: 'kiril@abv.bg' },
    'Peter': { age: 24, email: 'pesho@abv.bg' },
    'Georgi': { age: 23, email: 'georgi@abv.bg' },
};

let entries = Object.entries(people);
let sortedByName = entries.sort((personA, personB) => {
    let personAName = personA[0];
    let personBName = personB[0];
    return personAName.localeCompare(personB);
});

let sortedByEmail = entries.sort((personA, personB) => {
    let personAEmail = personA[1].email;
    let personBEmail = personB[1].email;
    return personAEmail.localeCompare(personBEmail);
});

for (const [name, info] of sortedByEmail) {
    console.log(name, info)
}