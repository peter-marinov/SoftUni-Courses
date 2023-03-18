function extract(content) {
    const pElement = document.getElementById('content');
    const pattern = /(?<=[\(])([A-Za-z0-9\s]+)(?=\))/gm;
    let result = pElement.textContent.match(pattern);

    return result.join(', ');
}