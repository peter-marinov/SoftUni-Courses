function solve([x1, y1, x2, y2]) {
    
    let distanceXToZero = Math.sqrt((0 - x1) ** 2 + (0 - y1) ** 2);
    let distanceYToZero = Math.sqrt((x2 - 0) ** 2 + (y2 - 0) ** 2);
    let distanceXTOY = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
    // console.log(distanceXToZero);
    // console.log(distanceYToZero);
    // console.log(distanceXTOY);
    if (Number.isInteger(distanceXToZero)) {
        console.log(`{${x1}, ${y1}} to {0, 0} is valid`)
    } else {
        console.log(`{${x1}, ${y1}} to {0, 0} is invalid`)
    }

    if (Number.isInteger(distanceYToZero)) {
        console.log(`{${x2}, ${y2}} to {0, 0} is valid`)
    } else {
        console.log(`{${x2}, ${y2}} to {0, 0} is invalid`)
    }

    if (Number.isInteger(distanceXTOY)) {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is valid`)
    } else {
        console.log(`{${x1}, ${y1}} to {${x2}, ${y2}} is invalid`)
    }
}

// solve(3, 0, 0, 4);

solve(2, 1, 1, 1);