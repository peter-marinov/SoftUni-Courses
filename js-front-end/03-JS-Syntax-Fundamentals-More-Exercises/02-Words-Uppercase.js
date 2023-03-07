function solve(sentence) {
    let pattern = /\w+/g;

    let result = sentence.match(pattern);
    
    console.log(result.map(word => word.toUpperCase()).join(', '));
}

solve('Hi, how are you?');