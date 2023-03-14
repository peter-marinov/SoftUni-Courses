function inventory(input) {
    let heroDB = [];
    for (const line of input) {
        let [Hero, level, items] = line.split(' / ');
        level = Number(level);
        heroDB.push({Hero, level, items});
    }
    
    heroDB.sort((a, b) => {
        let result = a.level - b.level;
        
        if (result === 0) {
            return a.Hero.localeCompare(b.Hero);
        }

        return result;
    });

    for (const currentHero of heroDB) {
        console.log(`Hero: ${currentHero.Hero}`);
        console.log(`level => ${currentHero.level}`);
        console.log(`items => ${currentHero.items}`);
        
    }
}

inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ])