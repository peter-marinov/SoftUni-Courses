function solve(source) {
    let spiceAmount = 0;
    let crewConsummation = 26;
    let days = 0;
    while (source >= 100) {
        spiceAmount += source;
        source -= 10;
        spiceAmount -= crewConsummation;
        days++;
    }

    if (spiceAmount - crewConsummation < 0) {
        spiceAmount = 0;
    } else {
        spiceAmount -= crewConsummation;
    }

    console.log(days);
    console.log(spiceAmount);
}

solve(111);
solve(450);