function asciiCharsInRange(firstSymbol, secondSymbol) {
    let resultArray = [];
    let startIndex = 0;
    let endIndex = 0;

    if (firstSymbol.charCodeAt(0) < secondSymbol.charCodeAt(0)){
        startIndex = firstSymbol.charCodeAt(0) + 1;
        endIndex = secondSymbol.charCodeAt(0);
    } else if (firstSymbol.charCodeAt(0) > secondSymbol.charCodeAt(0)){
        startIndex = secondSymbol.charCodeAt(0) + 1;
        endIndex = firstSymbol.charCodeAt(0);
    }
    
    for (let i = startIndex; i < endIndex; i++){
        resultArray.push(String.fromCharCode(i));
    }
    return resultArray.join(' ')
}

console.log(asciiCharsInRange('a', 'd'))