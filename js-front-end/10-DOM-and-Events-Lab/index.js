// function sum() {
//     console.log(5 + 5);
// }

// sum()

const liElements = document.getElementsByTagName('li');
const thirdLi = liElements[2];
thirdLi.textContent += ' This is DOM manipulation'
console.log(liElements)

for (const li of liElements) {
    console.log(li.id);
    li.setAttribute('class', 'list-item')
    li.innerHTML += '<p>Custom paragraph</p>'
    li.style.backgroundColor = 'red'
}

const textInput = document.getElementById('text-input');
console.log(textInput.value)

const html = document.getElementsByTagName('html')[0];
console.log(html)