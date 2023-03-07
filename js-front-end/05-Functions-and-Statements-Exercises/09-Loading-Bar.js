function loadingBar(number) {
    const bar = (num) => '[' + '%'.repeat(number/10) +
        '.'.repeat(10 - number/10) + ']';
    if (number === 100) {
        console.log('100% Complete!');
        console.log(bar(number));
    } else {
        console.log(`${number}% ${bar(number)}`);
        console.log('Still loading...')
    }
}

loadingBar(30)