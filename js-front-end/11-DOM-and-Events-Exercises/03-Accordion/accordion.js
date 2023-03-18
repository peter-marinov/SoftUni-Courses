function toggle() {
    const button = document.getElementsByClassName('button')[0];
    const moreInfo = document.getElementById('extra');
    let string = button.textContent;
    if (string === 'More') {
        moreInfo.style.display = 'block';
        button.textContent = 'Less';
    } else {
        moreInfo.style.display = 'none';
        button.textContent = 'More';
    }
}