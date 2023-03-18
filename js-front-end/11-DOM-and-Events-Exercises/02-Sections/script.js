function create(words) {
   const content = document.getElementById('content');
   
   for (const word of words) {
      const newDiv = document.createElement('div');
      const newParagraph = document.createElement('p');
      newParagraph.textContent = word;
      newParagraph.style.display = 'none';

      newDiv.addEventListener('click', () => {
         newParagraph.style.display = 'block';
      })

      // Attaching to DOM tree
      newDiv.appendChild(newParagraph);
      content.appendChild(newDiv);
   }
}



// const divContainer = document.getElementById('content');
// let newDiv = '';
// for (const word of words) {
//    newDiv = document.createElement('div');
//    newDiv.style.backgroundColor = 'lightblue';
//    newDiv.innerHTML = '<p>' + word +'</p>'
//    // newDiv.style.display = 'none'
//    // newDiv.childNodes.addEventListener('click', clickEvent);
//    divContainer.appendChild(newDiv)
// }

// const pElements = Array.from(document.querySelectorAll('div p'));
// pElements.forEach((p) => {
//    p.style.display = 'none'
//    p.addEventListener
// });

// const divOnClick = Array.from(document.querySelectorAll('div div'));
// for (const div of divOnClick) {
//    console.log(div.children[0])
//    div.childNodes.addEventListener('click', clickEvent);
// }
// // console.log(divOnClick)

// function clickEvent(e) {
//    const target = e.currentTarget;
//    target.style.display = 'block'