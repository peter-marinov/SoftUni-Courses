function makeADictionary(inputJSON) {
    let dataBaseSorted = [];
    let dataBase = [];
    for (const line of inputJSON) {
        let isSameKey = false;
        let currentObject = JSON.parse(line);
        let key = Object.keys(currentObject)[0];
        for (const iterator of dataBase) {
            let keyDB = Object.keys(iterator)[0];
            if (keyDB === key) {
                iterator[keyDB] = currentObject[key];
                isSameKey = true;
                break;
            }
        }
        if (!isSameKey) {
            dataBase.push({Term: key, Definition: currentObject[key]});
        }
        

    }



    dataBase.sort((a, b) => a['Term'].localeCompare(b['Term']));

    for (const iterator of dataBase) {
        // console.log(iterator)
        console.log(`Term: ${iterator['Term']} => Definition: ${iterator['Definition']}`)
    }
    
}

makeADictionary([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ])