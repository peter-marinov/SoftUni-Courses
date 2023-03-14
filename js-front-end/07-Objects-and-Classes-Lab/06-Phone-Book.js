function phoneBookParser(input) {
    let phoneBook = {};
    for (const line of input) {
        let [name, phoneNumber] = line.split(' ');
        phoneBook[name] = phoneNumber;
    }

    for (const key in phoneBook) {
        console.log(`${key} -> ${phoneBook[key]}`);
    }
}


phoneBookParser(['Tim 0834212554',

    'Peter 0877547887',

    'Bill 0896543112',

    'Tim 0876566344'])