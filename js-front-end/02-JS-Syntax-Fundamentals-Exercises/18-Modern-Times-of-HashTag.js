function solve(sentence) {
    let words = sentence.split(' ')
    for (let i = 0; i < words.length; i++) {
        // if (words[i][0] === '#' && words[i].slice(1).match(/^[A-Za-z]*$/)) {
        if (words[i].length > 1 && words[i].match(/^#[A-Za-z]*$/)) {
            console.log(words[i].slice(1))
        }
    }
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia')