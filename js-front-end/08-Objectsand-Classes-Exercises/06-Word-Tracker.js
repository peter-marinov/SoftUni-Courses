function wordsTracker(input) {
    let wordsDB = {};
    let words = input[0].split(' ');
    let otherWords = input.slice(1);
    let sorted = [];
    for (const word of words) {
        wordsDB[word] = 0;
    }

    for (const word of otherWords) {
        if (wordsDB.hasOwnProperty(word)) {
            wordsDB[word] += 1;
        }
    }

    for (const key in wordsDB) {
        sorted.push([key, wordsDB[key]]);
    }

    sorted.sort((a, b) => b[1] - a[1]);

    for (const word of sorted) {
        console.log(`${word[0]} - ${word[1]}`);
    }

}

wordsTracker([
    'this sentence',
    'In', 'this', 'sentence', 'you', 'have',
    'to', 'count', 'the', 'occurrences', 'of',
    'the', 'words', 'this', 'and', 'sentence',
    'because', 'this', 'is', 'your', 'task'
    ])