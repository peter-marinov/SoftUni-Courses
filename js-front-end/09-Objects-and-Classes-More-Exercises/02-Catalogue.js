function catalogue(input) {
    let items = [];
    for (const line of input) {
        let [item, price] = line.split(' : ');
        items.push([item, price]);
    }
    
    items.sort((a, b) => a[0].localeCompare(b[0]));

    for (let i = 0; i < items.length; i++) {
        if (i === 0 || items[i][0][0] !== items[i-1][0][0]) {
            console.log(items[i][0][0])
        } 
        console.log(`  ${items[i][0]}: ${items[i][1]}`)
    } 
}

catalogue([
    'Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
    ]);