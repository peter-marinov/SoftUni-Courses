function solve() {
    const inputNumber = document.getElementById('input');
    const btn = document.querySelector('button');
    const result = document.getElementById('result');
    const selectMenuTo = document.getElementById('selectMenuTo');

    const optionBinary = createChild('option', 'binary', 'Binary', selectMenuTo);
    const optionHexadecimal = createChild('option', 'hexadecimal', 'Hexadecimal', selectMenuTo);

    btn.addEventListener('click', convertor);

    
    function convertor() {
        let num = Number(inputNumber.value);
        if (optionBinary.selected) {
            result.value = num.toString(2);
        } else if (optionHexadecimal.selected) {
            result.value = num.toString(16).toLocaleUpperCase();
        }
        
        console.log(document.querySelectorAll('#result')[0].value)
    }


    function createChild(type, value, content, parent) {
        const newChild = document.createElement(type);

        if (value) {
            newChild.value = value;
        }

        if (content) {
            newChild.textContent = content;
        }

        if (parent) {
            parent.appendChild(newChild);
        }

        return newChild;
    }
}