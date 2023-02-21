function solve(sentence, word) {
    let sentenceArray = sentence.split(' ');
    let counter = 0;
    for (let w of sentenceArray) {
        if (w === word) {
            counter++;
        }
    }
    console.log(counter)
}

solve('This is a word and it also is a sentence',

'is')