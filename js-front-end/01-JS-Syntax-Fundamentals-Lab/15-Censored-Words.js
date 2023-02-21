function solve(sentence, word) {
    let replaceWord = '';
    for (let i = 0; i < word.length; i++) {
        replaceWord += '*'
    }
    while (sentence.includes(word)) {
        sentence = sentence.replace(word, replaceWord)
    }
    console.log(sentence)
}

solve('Find the hidden word', 'hidden')