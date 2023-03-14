function employees(input) {
    let peopleData = {};
    // for (const line of input) {
    //     peopleData[line] = line.length;
    // }

    peopleData = input.reduce((data, employee) => {
        data[employee] = employee.length;
        return data;
    }, {});

    for (const key in peopleData) {
        console.log(`Name: ${key} -- Personal Number: ${peopleData[key]}`)
    }

}

employees([

    'Silas Butler',

    'Adnaan Buckley',

    'Juan Peterson',

    'Brendan Villarreal'

])