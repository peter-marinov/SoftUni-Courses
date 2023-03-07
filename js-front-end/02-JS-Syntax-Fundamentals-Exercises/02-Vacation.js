function solve(people, group, day) {
    let totalPrice = null;
    if (day === 'Friday') {
        if (group === 'Students') {
            totalPrice = 8.45 * people
            if (people >= 30) {
                totalPrice *= 0.85
            }
        } else if (group === 'Business') {
            totalPrice = 10.90 * people
            if (people >= 100) {
                totalPrice -= 10.90 * 10
            }
        } else {
            totalPrice = 15 * people
            if (people >= 10 && people <= 20) {
                totalPrice *= 0.95
            }
        }
    } else if (day === 'Saturday') {
        if (group === 'Students') {
            totalPrice = 9.80 * people
            if (people >= 30) {
                totalPrice *= 0.85
            }
        } else if (group === 'Business') {
            totalPrice = 15.60 * people
            if (people >= 100) {
                totalPrice -= 15.60 * 10
            }
        } else {
            totalPrice = 20 * people
            if (people >= 10 && people <= 20) {
                totalPrice *= 0.95
            }
        }
    } else {
        if (group === 'Students') {
            totalPrice = 10.46 * people
            if (people >= 30) {
                totalPrice *= 0.85
            }
        } else if (group === 'Business') {
            totalPrice = 16 * people
            if (people >= 100) {
                totalPrice -= 16 * 10
            }
        } else {
            totalPrice = 22.50 * people
            if (people >= 10 && people <= 20) {
                totalPrice *= 0.95
            }
        }
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`)
}

solve(30,

    "Students",
    
    "Sunday")