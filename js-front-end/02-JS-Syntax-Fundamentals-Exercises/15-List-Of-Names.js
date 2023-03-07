function solve(names) {
    // names.sort((a, b) => a.localeCompare(b));
    // if (names.length > 0) {
    //     for (let i = 0; i < names.length; i++) {
    //         console.log(`${i + 1}.${names[i]}`)
    //     }
    // }

    return [...names]
        .sort((aName, bName) => aName.localeCompare(bName))
        .map((name, index) => `${index + 1}.${name}`)
        .join('\n');
    
}



console.log(solve(["John", "Bob", "Christina", "Ema"]))