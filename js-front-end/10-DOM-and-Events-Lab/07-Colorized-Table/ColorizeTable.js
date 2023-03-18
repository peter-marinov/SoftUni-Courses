function colorize() {
    const rows = Array.from(document.querySelectorAll('table tr:nth-child(even)'));
    rows.forEach((td) => {
        td.style.backgroundColor = 'Teal';
    })
}