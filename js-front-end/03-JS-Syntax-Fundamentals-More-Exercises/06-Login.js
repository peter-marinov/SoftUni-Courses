function solve(input) {
    let user = input[0];
    let loginPassword = user
        .split('')
        .reverse()
        .join('')
    let passwords = input.slice(1);
    let count = 0;
    for (let i = 0; i < passwords.length; i++) {
        count++;
        if (passwords[i] === loginPassword) {
            console.log(`User ${user} logged in.`)
        } else {
            if (count === 4) {
                console.log(`User ${user} blocked!`);
                break;
            }
            console.log('Incorrect password. Try again.')
        }
    }
}

solve(['Acer','login','go','let me in','recA']);
solve(['sunny','rainy','cloudy','sunny','not sunny'])