function solve(golds) {
    const bitcoinPrice = 11949.16;
    const goldPerGramPrice = 67.51;
    let totalBitcoins = 0;
    let bitcoins = 0;
    let days = 0;
    let money = 0;
    let isFirstBitcoinGain = false;
    for (let i = 0; i < golds.length; i++) {
        if ((i + 1) % 3 === 0) {
            money += golds[i] * goldPerGramPrice * 0.7;
        } else {
            money += golds[i] * goldPerGramPrice;
        };
        
        if (money / bitcoinPrice > 1) {
            bitcoins = Math.floor(money / bitcoinPrice);
            totalBitcoins += bitcoins;
            money -= bitcoins * bitcoinPrice;
            if (isFirstBitcoinGain === false) {
                days = i + 1;
                isFirstBitcoinGain = true;
            }
        }
    }

    console.log(`Bought bitcoins: ${totalBitcoins}`);
    if (bitcoins > 0) {
        console.log(`Day of the first purchased bitcoin: ${days}`);
    }
    console.log(`Left money: ${money.toFixed(2)} lv.`)
}

solve([100, 200, 300])