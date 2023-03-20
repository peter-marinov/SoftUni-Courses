function pianist(inputs) {
    let numberOfPieces = Number(inputs.shift());
    let songsDB = {}

    for (let i = 0; i < numberOfPieces; i++) {
        let [piece, composer, key] = inputs.shift().split('|');
        songsDB[piece] = {Composer: composer, Key: key};
    }

    for (const input of inputs) {
        if (input === 'Stop') {
            for (const key in songsDB) {
                console.log(`${key} -> Composer: ${songsDB[key].Composer}, Key: ${songsDB[key].Key}`);
            }
            break;
        }

        let [command] = input.split('|');
        if (command === 'Add') {
            let [_unused, piece, composer, key] = input.split('|');

            if (songsDB.hasOwnProperty(piece)) {
                console.log(`${piece} is already in the collection!`);
            } else {
                songsDB[piece] = {Composer: composer, Key: key};
                console.log(`${piece} by ${composer} in ${key} added to the collection!`)
            }
        } else if (command === 'Remove') {
            let [_unused, piece] = input.split('|');

            if (!songsDB.hasOwnProperty(piece)) {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            } else {
                delete songsDB[piece];
                console.log(`Successfully removed ${piece}!`);
            }
        } else if (command === 'ChangeKey') {
            let [_unused, piece, newKey] = input.split('|');

            if (!songsDB.hasOwnProperty(piece)) {
                console.log(`Invalid operation! ${piece} does not exist in the collection.`);
            } else {
                songsDB[piece].Key = newKey;
                console.log(`Changed the key of ${piece} to ${newKey}!`);
            }
        }
    }
}

pianist([
    '3',
    'Fur Elise|Beethoven|A Minor',
    'Moonlight Sonata|Beethoven|C# Minor',
    'Clair de Lune|Debussy|C# Minor',
    'Add|Sonata No.2|Chopin|B Minor',
    'Add|Hungarian Rhapsody No.2|Liszt|C# Minor',
    'Add|Fur Elise|Beethoven|C# Minor',
    'Remove|Clair de Lune',
    'ChangeKey|Moonlight Sonata|C# Major',
    'Stop'  
  ]
  );