function piccolo(input) {
    let parking = [];
    for (const line of input) {
        let [operation, carNumber] = line.split(', ');
        // console.log(carNumber, operation)
        if (parking.includes(carNumber) && operation === 'OUT') {
            // console.log(carNumber, operation)
            let index = parking.indexOf(carNumber);
            parking.splice(index, 1);
        } else if (!parking.includes(carNumber) && operation === 'IN') {
            // console.log(carNumber, operation)
            parking.push(carNumber);
        }
        
    }

    parking.sort();
    if (parking.length !== 0) {
        for (const car of parking) {
            console.log(car);
        }
        
    } else {
        console.log("Parking Lot is Empty");
    }
    
}

// piccolo(['IN, CA2844AA',

// 'IN, CA1234TA',

// 'OUT, CA2844AA',

// 'OUT, CA1234TA']);

piccolo([
    'IN, CA2844AA', 
    'IN, CA1234TA', 
    'OUT, CA2844AA', 
    'IN, CA9999TT', 
    'IN, CA2866HI', 
    'OUT, CA1234TA', 
    'IN, CA2844AA', 
    'OUT, CA2866HI', 
    'IN, CA9876HH', 
    'IN, CA2822UU'])