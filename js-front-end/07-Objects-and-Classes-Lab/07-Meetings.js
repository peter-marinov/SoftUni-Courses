function meetings(input) {
    let schedule = {};
    for (const line of input) {
        let [key, value] = line.split(' ');
        if (schedule.hasOwnProperty(key)) {
            console.log(`Conflict on ${key}!`);
        } else {
            schedule[key] = value;
            console.log(`Scheduled for ${key}`);
        }
    }

    for (const key in schedule) {
        console.log(`${key} -> ${schedule[key]}`);
    }
}



meetings(['Monday Peter',

'Wednesday Bill', 'Monday Tim', 'Friday Tim'])