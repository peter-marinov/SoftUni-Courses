function solve(range, numbers) {
    let newArray = [];
    let y = 0;
    for (let i = range - 1; i >= 0; i--) {
        newArray[y] = numbers [i];
        y++;
    }

    console.log(...newArray)
}

solve(3, [10, 20, 30, 40, 50])