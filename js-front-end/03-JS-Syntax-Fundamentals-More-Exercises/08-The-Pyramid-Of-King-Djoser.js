function solve(baseWidth, length) {
    let stones = 0;
    let marbles = 0;
    let lapises = 0;
    let golds = 0;
    let steps = 0;
    let pyramidHeight = 0
    for (let width = baseWidth; width >= 1; width -= 2) {
        steps++;

        if (width - 2 < 1) {
            golds += width ** 2;
        } else {
            stones += (width - 2) ** 2;
            if (steps % 5 === 0) {
                lapises += width * 4 - 4;
            } else {
                marbles += width * 4 - 4;
            }
        }
        // console.log(`steps: ${steps} width: ${width} stones: ${stones} marbles: ${marbles} lapises: ${lapises} golds: ${golds}`)
    }

    stones = Math.ceil(stones * length);
    marbles = Math.ceil(marbles * length);
    lapises = Math.ceil(lapises * length);
    golds = Math.ceil(golds * length);
    pyramidHeight = Math.floor(steps * length);

    console.log(`Stone required: ${stones}`);
    console.log(`Marble required: ${marbles}`);
    console.log(`Lapis Lazuli required: ${lapises}`);
    console.log(`Gold required: ${golds}`);
    console.log(`Final pyramid height: ${pyramidHeight}`)
    
}

solve(11, 1);