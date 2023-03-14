function flightSchedule(input) {
    let flights = {};
    for (const line of input[0]) {
        let [flightNumber, city] = line.split(' ');
        flights[flightNumber] = [city, ''] ;
    }
    
    for (const line of input[1]) {
        let [flightNumber, status] = line.split(' ');
        for (const key in flights) {
            if (key === flightNumber) {
                flights[key][1] = status;
            }
        }
    }

    if (input[2][0] === 'Ready to fly') {
        for (const key in flights) {
            if (flights[key][1] === input[2][0] || flights[key][1] === '') {
                console.log(`{ Destination: '${flights[key][0]}', Status: 'Ready to fly' }`);
            }
        }
    }

    if (input[2][0] === 'Cancelled') {
        for (const key in flights) {
            if (flights[key][1] === input[2][0]) {
                console.log(`{ Destination: '${flights[key][0]}', Status: 'Cancelled' }`);
            }
        }
    }

}

flightSchedule([['WN269 Delaware',
'FL2269 Oregon',
'WN498 Las Vegas',
'WN3145 Ohio',
'WN612 Alabama',
'WN4010 New York',
'WN1173 California',
'DL2120 Texas',
'KL5744 Illinois',
'WN678 Pennsylvania'],

['DL2120 Cancelled',
'WN612 Cancelled',
'WN1173 Cancelled',
'SK430 Cancelled'],

['Cancelled']

]);