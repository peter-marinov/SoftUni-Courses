function solve(fights, helmetPrice, swordPrice, shieldPrice, armorPrice) {
    let brokenHelmets = Math.floor(fights / 2);
    let brokenSwords = Math.floor(fights / 3);
    let brokenShields = Math.floor(fights / 6);
    let brokenArmors = Math.floor(fights / 12);
    let totalPrice = brokenHelmets * helmetPrice + brokenSwords * swordPrice + brokenShields * shieldPrice + brokenArmors * armorPrice;
    // console.log(brokenHelmets);
    // console.log(brokenSwords);
    // console.log(brokenShields);
    // console.log(brokenArmors);

    console.log(`Gladiator expenses: ${totalPrice.toFixed(2)} aureus`)
}

solve(7,

    2,
    
    3,
    
    4,
    
    5)