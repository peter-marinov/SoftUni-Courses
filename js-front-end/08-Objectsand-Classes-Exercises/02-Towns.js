function towns(input) {
    let townsData = [];
    for (const line of input) {
        let [town, latitude, longitude] = line.split(' | ');
        latitude = Number(latitude).toFixed(2);
        longitude = Number(longitude).toFixed(2);
        townsData.push({town, latitude, longitude});
    }

    for (const town of townsData) {
        console.log(town);
    }

}

towns(['Sofia | 42.696552 | 23.32601',

'Beijing | 39.913818 | 116.363625']);