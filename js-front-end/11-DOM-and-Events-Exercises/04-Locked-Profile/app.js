function lockedProfile() {
    const moreInformation = Array.from(document.querySelectorAll('.profile div'));
    const buttonElements = Array.from(document.getElementsByTagName('button'));
    document.getElementsByName
    for (const button of buttonElements) {
        button.style.cursor = 'pointer';
        button.addEventListener('click', showHide);
    }

    function showHide(e) {
        const element = e.currentTarget;
        const divShowHide = element.parentElement.getElementsByTagName('div')[0];
        const lockUnlock = element.parentElement.querySelectorAll('input[value=unlock]')[0];
        if (lockUnlock.checked) {
            if (element.textContent === 'Show more') {
                element.textContent = 'Hide it';
                divShowHide.style.display = 'block';
            } else {
                element.textContent = 'Show more';
                divShowHide.style.display = 'none';
            }
        }
        
   
    }
}