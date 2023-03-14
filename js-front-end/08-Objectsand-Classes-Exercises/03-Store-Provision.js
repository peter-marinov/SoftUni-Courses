function storeProvision(...input) {
    let provisions = {};
    for (const line of input) {
        for (let i = 0; i < line.length; i+=2) {
            let key = line[i];
            let value = Number(line[i + 1]);
            if(!provisions.hasOwnProperty(key)) {
                provisions[key] = 0;
            }
            provisions[key] += value;
        }
    }

    for (const key in provisions) {
        console.log(`${key} -> ${provisions[key]}`)
    }
}

storeProvision([
    'Chips', '5', 'CocaCola', '9', 'Bananas',
    '14', 'Pasta', '4', 'Beer', '2' 
    ],
    
    ['Flour', '44', 'Oil', '12', 'Pasta', '7',
    
    'Tomatoes', '70', 'Bananas', '30']);