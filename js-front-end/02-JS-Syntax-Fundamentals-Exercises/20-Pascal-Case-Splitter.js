function solve(pascalCase) {
    let words = [];
    let startIndex = 0;
    let endIndex = 0;
    for (let i = 0; i < pascalCase.length; i++) {
        if (pascalCase[i] === pascalCase[i].toUpperCase()) {
            startIndex = i;
        }
        if (i === pascalCase.length - 1) {
            endIndex = i + 1;
            words.push(pascalCase.slice(startIndex, endIndex))
        } else {
            if (pascalCase[i + 1] === pascalCase[i + 1].toUpperCase()) {
                endIndex = i + 1;
                words.push(pascalCase.slice(startIndex, endIndex))
            }

        }
    }

    console.log(words.join(', '))
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan')