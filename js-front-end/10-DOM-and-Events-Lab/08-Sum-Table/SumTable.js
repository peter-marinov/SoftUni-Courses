function sumTable() {
    const prices = Array.from(document.querySelectorAll('table tbody tr:not(:last-child) td:nth-child(even)'));
    const result = document.getElementById('sum');
    let sum = 0;
    for (const iterator of prices) {
        sum += Number(iterator.textContent);
    }

    result.textContent = sum;
    
    
}