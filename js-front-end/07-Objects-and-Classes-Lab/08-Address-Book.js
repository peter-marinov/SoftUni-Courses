function addressBook(input) {
    let addressBookMap = {};
    for (const line of input) {
        let [name, address] = line.split(':');
        addressBookMap[name] = address;
    }

    let sortedNames = Object.keys(addressBookMap)
        .sort((nameA, nameB) => nameA.localeCompare(nameB));
    for (const name of sortedNames) {
        console.log(`${name} -> ${addressBookMap[name]}`);
    }
}

addressBook(['Tim:Doe Crossing',

'Bill:Nelson Place',

'Peter:Carlyle Ave',

'Bill:Ornery Rd']);