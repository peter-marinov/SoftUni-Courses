function solve(speed, type) {
    const motorwayLimit = 130;
    const interstateLimit = 90;
    const cityLimit = 50;
    const residentialLimit = 20;

    let speedDiff = 0;
    let status = undefined;

    if (type === 'motorway') {
        if (speed <= motorwayLimit) {
            console.log(`Driving ${speed} km/h in a ${motorwayLimit} zone`)
        } else {
            speedDiff = speed - motorwayLimit;
            if (speedDiff <= 20) {
                status = 'speeding'
            } else if (speedDiff <= 40) {
                status = 'excessive speeding'
            } else {
                status = 'reckless driving'
            }

            console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${motorwayLimit} - ${status}`)
        }
    } else if (type === 'interstate') {
        if (speed <= interstateLimit) {
            console.log(`Driving ${speed} km/h in a ${interstateLimit} zone`)
        } else {
            speedDiff = speed - interstateLimit;
            if (speedDiff <= 20) {
                status = 'speeding'
            } else if (speedDiff <= 40) {
                status = 'excessive speeding'
            } else {
                status = 'reckless driving'
            }

            console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${interstateLimit} - ${status}`)
        }
    } else if (type === 'city') {
        if (speed <= cityLimit) {
            console.log(`Driving ${speed} km/h in a ${cityLimit} zone`)
        } else {
            speedDiff = speed - cityLimit;
            if (speedDiff <= 20) {
                status = 'speeding'
            } else if (speedDiff <= 40) {
                status = 'excessive speeding'
            } else {
                status = 'reckless driving'
            }

            console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${cityLimit} - ${status}`)
        }
    } else if (type === 'residential') {
        if (speed <= residentialLimit) {
            console.log(`Driving ${speed} km/h in a ${residentialLimit} zone`)
        } else {
            speedDiff = speed - residentialLimit;
            if (speedDiff <= 20) {
                status = 'speeding'
            } else if (speedDiff <= 40) {
                status = 'excessive speeding'
            } else {
                status = 'reckless driving'
            }

            console.log(`The speed is ${speedDiff} km/h faster than the allowed speed of ${residentialLimit} - ${status}`)
        }
    } 
}

solve(40, 'city')
solve(21, 'residential')
solve(120, 'interstate')