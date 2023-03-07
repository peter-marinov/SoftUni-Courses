function radioCrystals(inputValues) {
    const cut = (a) => a / 4;
    const lap = (a) => a * 0.8;
    const grind = (a) => a - 20;
    const etch = (a) => a - 2;
    const xray = (a) => a + 1;

    function transportingAndWashing(a) {
        console.log('Transporting and washing');
        return Math.floor(a);
    }

    let neededValue = inputValues[0];
    let crystalsToFix = inputValues.slice(1);

    for (let i = 0; i < crystalsToFix.length; i++) {
        let operationsCut = 0;
        let operationsLap = 0;
        let operationsGrind = 0;
        let operationsEtch = 0;
        let operationsXray = 0;
        let crystal = crystalsToFix[i];

        console.log(`Processing chunk ${crystal} microns`)

        while (cut(crystal) >= neededValue) {
            crystal = cut(crystal);
            operationsCut += 1
        }

        if (operationsCut > 0) {
            console.log(`Cut x${operationsCut}`)
            crystal = transportingAndWashing(crystal);    
        }

        if (crystal === neededValue) {
            console.log(`Finished crystal ${neededValue} microns`);
            continue;
        }
        
        while (lap(crystal) >= neededValue) {
            crystal = lap(crystal);
            operationsLap += 1
        }

        if (operationsCut > 0) {
            console.log(`Lap x${operationsLap}`)
            crystal = transportingAndWashing(crystal);    
        }

        if (crystal === neededValue) {
            console.log(`Finished crystal ${neededValue} microns`);
            continue;
        }

        while (grind(crystal) >= neededValue) {
            crystal = grind(crystal);
            operationsGrind += 1
        }

        if (operationsCut > 0) {
            console.log(`Grind x${operationsGrind}`)
            crystal = transportingAndWashing(crystal);    
        }

        if (crystal === neededValue) {
            console.log(`Finished crystal ${neededValue} microns`);
            continue;
        }

        if ((crystal - neededValue) % 2 !== 0) {
            crystal = xray(crystal);
            operationsXray += 1;
        }

        while (etch(crystal) >= neededValue) {
            crystal = etch(crystal);
            operationsEtch += 1
        }

        if (operationsCut > 0) {
            console.log(`Etch x${operationsEtch}`)
            crystal = transportingAndWashing(crystal);    
        }

        if (crystal === neededValue && operationsXray === 0) {
            console.log(`Finished crystal ${neededValue} microns`);
            continue;
        }
        
        if(operationsXray === 1) {
            console.log(`X-ray x${operationsXray}`)
        }

       

        if (crystal === neededValue) {
            console.log(`Finished crystal ${neededValue} microns`);
            continue;
        }



    }
}

radioCrystals([1375, 50000])