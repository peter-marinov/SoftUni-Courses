function extractText() {
    const liElements = Array.from(document.querySelectorAll('#items > li'));
    const result = document.getElementById('result');
    liElements
        .forEach((li) => {
            result.textContent += li.textContent + '\n';
        })
    
}

    // const liElements = document.getElementsByTagName('li');
    // const result = document.getElementById('result');
    // let text = '';
    
    // for (const iterator of liElements) {
    //     text += iterator.textContent + '\n';
    // }

    // result.textContent = text;