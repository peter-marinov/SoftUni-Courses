function focused() {
    const allInputs = Array.from(document.getElementsByTagName('input'));
    
    for (const input of allInputs) {
        input.addEventListener('focus', handleFocus);
        input.addEventListener('blur', handleBlur);
    }

    function handleFocus(event) {
        const currentInput = event.target;
        const parentDiv = currentInput.parentElement;
        parentDiv.classList.add('focused');
    }

    function handleBlur(event) {
        const currentInput = event.target;
        const parentDiv = currentInput.parentElement;
        parentDiv.classList.remove('focused');
    }
}