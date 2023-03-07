function solve(words, sentence) {
    let keyWords = words.split(', ')
    let replacedText = ''

    for (let i = 0; i < keyWords.length; i++) {
        replacedText = sentence.replace('*'.repeat(keyWords[i].length), keyWords[i]);
        sentence = replacedText;
    }
    console.log(replacedText)
}

solve('great, learning', 'softuni is ***** place for ******** new programming languages')