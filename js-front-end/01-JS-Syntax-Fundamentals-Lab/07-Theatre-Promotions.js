function solve(day, age) {
    if (0 <= age && age <= 18) {
        if (day === 'Weekday') {
            console.log('12$');
        } else if (day === 'Weekend') {
            console.log('15$');
        } else {
            console.log('5$');
        }
    } else if (18 < age && age <= 64) {
        if (day === 'Weekday') {
            console.log('18$');
        } else if (day === 'Weekend') {
            console.log('20$');
        } else {
            console.log('12$');
        }
    } else if (64 < age && age <= 122) {
        if (day === 'Weekday') {
            console.log('12$');
        } else if (day === 'Weekend') {
            console.log('15$');
        } else {
            console.log('10$');
        }
    } else {
        console.log('Error!')
    }
}

solve('Weekday',

42)