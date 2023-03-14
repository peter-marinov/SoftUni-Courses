function armies(input) {
    let leaders = {};

    for (const line of input) {
        if (line.includes('arrives')) {
            let newLeader = line.split(' arrives')[0];
            leaders[newLeader] = {};
            continue
        }

        if (line.includes('defeated')) {
            let leaderToRemove = line.split(' defeated')[0];
            if (leaders.hasOwnProperty(leaderToRemove)) {
                delete leaders[leaderToRemove];
            }
            continue
        }

        if (line.includes(':')) {
            let [leader, armies] = line.split(': ');
            let [armyName, armyCount] = armies.split(', ')
            if (leaders.hasOwnProperty(leader)) {
                leaders[leader][armyName] = Number(armyCount);
            }
            continue
        }

        if (line.includes('+')) {
            let [armyName, armyCount] = line.split(' + ');
            for (const leader in leaders) {
                if(leaders[leader].hasOwnProperty(armyName)) {
                    leaders[leader][armyName] += Number(armyCount);
                    break;
                }
            }
        }
    }

    let leadersArmy = [];
    for (const leader in leaders) {
        let sum = 0;
        for (const key in leaders[leader]) {
            sum += Number(leaders[leader][key]);
        }
        leadersArmy.push([leader, sum])
    }
    leadersArmy.sort((a, b) => b[1] - a[1]);

    for (const info of leadersArmy) {
        let [leader, armySize] = info;
        let sortedArmies = [];
        console.log(`${leader}: ${armySize}`)
        for (const key in leaders[leader]) {
            sortedArmies.push([key, leaders[leader][key]]);
            // console.log(`>>> ${key} - ${leaders[leader][key]}`)
        }

        sortedArmies.sort((a, b) => b[0].localeCompare(a[0]));
        for (const iterator of sortedArmies) {
            console.log(`>>> ${iterator[0]} - ${iterator[1]}`)
        }
    }

}

armies(
    ['Rick Burr arrives', 'Findlay arrives', 
    'Rick Burr: Juard, 1500',
    'Wexamp arrives', 
    'Findlay: Wexamp, 34540', 
    'Wexamp + 340', 'Wexamp: Britox, 1155', 
    'Wexamp: Juard, 43423']
)

// armies(
//     ['Rick Burr arrives',
//         'Fergus: Wexamp, 30245',
//         'Rick Burr: Juard, 50000',
//         'Findlay arrives',
//         'Findlay: Britox, 34540',
//         'Britox + 4500',
//         'Porter arrives',
//         'Porter: Legion, 55000',
//         'Rick Burr defeated',
//         'Porter: Retix, 3205']
// )

// armies(
//     ['Rick Burr arrives',
//         'Fergus: Wexamp, 30245',
//         'Rick Burr: Juard, 50000',
//         'Findlay arrives',
//         'Findlay: Britox, 34540',
//         'Wexamp + 6000',
//         'Juard + 1350',
//         'Britox + 4500',
//         'Porter arrives',
//         'Porter: Legion, 55000',
//         'Legion + 302',
//         'Rick Burr defeated',
//         'Porter: Retix, 3205']
// )