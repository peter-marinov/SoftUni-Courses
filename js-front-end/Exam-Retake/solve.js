function solve(input) {
    let currentPositions = input.shift().split('|');
    // console.log(currentPositions)

    while (input.length > 0) {
        
        let currentCommand = input.shift().split(' ');
        let action = currentCommand[0];

        // console.log(`${currentCommand} -> ${currentPositions}`)

        if (action === 'Finish') {
            let winner = currentPositions[currentPositions.length - 1];
            console.log(currentPositions.join('->'));
            console.log(`The winner is: ${winner}`)

            break;
        } else if (action === 'Retake') {
            let overtakingHorse = currentCommand[1];
            let overtakenHorse = currentCommand[2];
            let overtakingHorseIndex = currentPositions.indexOf(overtakingHorse);
            let overtakenHorseIndex = currentPositions.indexOf(overtakenHorse);

            if (overtakingHorseIndex < overtakenHorseIndex) {
                currentPositions[overtakingHorseIndex] = overtakenHorse;
                currentPositions[overtakenHorseIndex] = overtakingHorse;

                console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
                
            }
            

        } else if (action === 'Trouble') {
            let horseName = currentCommand[1];
            let horseNameIndex = currentPositions.indexOf(horseName);
            if (horseNameIndex > 0) {
                let horseForward = currentPositions[horseNameIndex - 1];
                currentPositions[horseNameIndex] = horseForward;
                currentPositions[horseNameIndex - 1] = horseName;

                console.log(`Trouble for ${horseName} - drops one position.`);
            }

        } else if (action === 'Rage') {
            let horseName = currentCommand[1];
            let horseNameIndex = currentPositions.indexOf(horseName);
            if (horseNameIndex < currentPositions.length - 1) {
                if (horseNameIndex === currentPositions.length - 2) {
                    let horseForward = currentPositions[horseNameIndex + 1];
                    currentPositions[horseNameIndex] = horseForward;
                    currentPositions[horseNameIndex + 1] = horseName;
                } else {
                    let horseFirst = currentPositions[horseNameIndex + 1];
                    let horseFirstIndex = currentPositions.indexOf(horseFirst);

                    let horseSecond = currentPositions[horseNameIndex + 2];
                    let horseSecondIndex = currentPositions.indexOf(horseSecond);
                    currentPositions[horseNameIndex] = horseFirst;
                    currentPositions[horseNameIndex + 1] = horseSecond;
                    currentPositions[horseNameIndex + 2] = horseName;
                     
                }
            }

            console.log(`${horseName} rages 2 positions ahead.`)

        } else if (action === 'Miracle') {
            let lastHorse = currentPositions[0];
            let fistHorse = currentPositions[currentPositions.length - 1];

            currentPositions[0] = fistHorse;
            currentPositions[currentPositions.length - 1] = lastHorse;
            if (currentPositions.length > 1) {
                console.log(`What a miracle - ${lastHorse} becomes first.`);  
            }
            
        }
    }
}

solve(['Onyx|Domino|Sugar|Fiona',
'Trouble Onyx',
'Retake Onyx Sugar',
'Rage Domino',
'Miracle',
'Finish']);