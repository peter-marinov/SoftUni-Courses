function garage(input) {
    let garagesDB = {};
    for (const line of input) {
        let currentItems = [];
        let [garageNumber, restOfLine] = line.split(' - ');
        let otherInfo = restOfLine.split(', ');

        // console.log(otherInfo)
        if (!garagesDB.hasOwnProperty(garageNumber)) {
            garagesDB[garageNumber] = [];
        }
        
        for (const info of otherInfo) {
            let [key, value] = info.split(': ');
            currentItems.push(`${key} - ${value}`)
        }

        garagesDB[garageNumber].push(currentItems)
    }

    for (const key in garagesDB) {
        // console.log(key, garagesDB[key])
        console.log(`Garage № ${key}`);
        for (const values of garagesDB[key]) {
            // console.log(values)
            console.log(`--- ${values.join(', ')}`)
        }
    }
}

garage(
    ['1 - color: blue, fuel type: diesel', 
    '1 - color: red, manufacture: Audi', 
    '2 - fuel type: petrol', 
    '4 - color: dark blue, fuel type: diesel, manufacture: Fiat']
)