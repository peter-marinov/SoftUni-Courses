function solve(word, sentence) {
    let words = sentence.split(' ');
    let isFound = false;
    for (let i = 0; i < words.length; i++) {
        if (words[i].toLowerCase() === word.toLowerCase()) {
            isFound = true;
            break;
        }
    }

    if (isFound) {
        console.log(word);
    } else {
        console.log(`${word} not found!`)
    }
}

solve('javascript',

'JavaScript is the best programming language')