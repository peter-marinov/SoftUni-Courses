function solve(number, ...operations) {
    // for (let i = 0; i < operations.length; i++) {
    //     let currentOperation = operations[i];
    //     if (currentOperation === 'chop') {
    //         number /= 2;
    //     } else if (currentOperation === 'dice') {
    //         number = Math.sqrt(number);
    //     } else if (currentOperation === 'spice') {
    //         number += 1;
    //     } else if (currentOperation === 'bake') {
    //         number *= 3;
    //     } else {
    //         number *= 0.8;
    //     }

    //     console.log(number)

    // }

    let numberNum = Number(number);

    operations
        .forEach((operations) => {
            switch (operations) {
                case 'chop':
                    numberNum /= 2;
                    break;
                case 'dice':
                    numberNum = Math.sqrt(numberNum);
                    break;
                case 'spice':
                    numberNum += 1;
                    break;
                case 'bake':
                    numberNum *= 3;
                    break;
                case 'fillet':
                    numberNum *= 0.8;
                    break;
            }
            console.log(numberNum)
        });

        
}

solve('32', 'chop', 'chop', 'chop', 'chop', 'chop')