function oddOccurrences(input) {
    let words = input.split(' ');
    let wordsDB = {};
    let result = [];
    for (let word of words) {
        word = '_' + String(word).toLowerCase();
        if (!wordsDB.hasOwnProperty(word)) {
            wordsDB[word] = 0;
        }
        wordsDB[word] += 1;
    }

    for (const key in wordsDB) {
        if (wordsDB[key] % 2 !== 0) {
            result.push(key.slice(1));
        }
    }

    console.log(...result)



}

oddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#')