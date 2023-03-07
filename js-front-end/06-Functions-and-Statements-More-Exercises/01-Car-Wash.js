function carWash(commands) {
    let cleanValue = 0;
    commands.forEach(command => {
        switch (command) {
            case 'soap': cleanValue += 10; break;
            case 'water': cleanValue *= 1.2; break;
            case 'vacuum cleaner': cleanValue *= 1.25; break;
            case 'mud': cleanValue *= 0.9; break;
        }
    });


    return `The car is ${(cleanValue).toFixed(2)}% clean.`
}

console.log(
    carWash(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water'])
);
