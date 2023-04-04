// function attachEvents() {
//   const titleInput = document.getElementById('title');
//   const addBtn = document.getElementById('add-button');
//   const loadBtn = document.getElementById('load-button');
//   const listContainer = document.getElementById('todo-list');
//   const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
//   let currentData = {};

//   loadBtn.addEventListener('click', loadHandler);
//   addBtn.addEventListener('click', addHandler);

//   async function loadHandler(event) {
//     event.preventDefault();
    
//     const allDataRes = await fetch(BASE_URL);
//     const allData = await allDataRes.json();
//     let allDataArray = Object.values(allData);
//     listContainer.innerHTML = '';

//     allDataArray
//         .forEach((data) => {
//             const { name, _id } = data;
//             const li = createElement('li', '', listContainer);
//             createElement('span', name, li);
//             const removeBtn = createElement('button', 'Remove', li, _id);
//             const editBtn = createElement('button', 'Edit', li, );

//             removeBtn.addEventListener('click', removeHandler);
//             editBtn.addEventListener('click', editHandler);
//         })

//         async function removeHandler(event) {
//             const id = this.id;
//             const htmlHeaders = {
//                 method: 'DELETE'
//               };
            
//             const removedData = await fetch(`${BASE_URL}${id}`, htmlHeaders);
//             loadHandler(event);
//         }

//         async function editHandler(event) {
//             const currentBtn = event.currentTarget;
//             const liParent = this.parentNode;
//             const rmvBtn = Array.from(liParent.querySelectorAll('li button'))[0];
//             const currentId = rmvBtn.id;
//             if (currentBtn.textContent === 'Edit') {
                
//                 const spanElement = liParent.querySelector('li > span');
//                 const inputField = document.createElement('input');
//                 inputField.value = spanElement.textContent;
//                 liParent.removeChild(spanElement);
//                 liParent.insertBefore(inputField, liParent.firstChild);
//                 currentBtn.textContent = 'Submit';
//             } else {
//                 const textInput = liParent.querySelector('li > input');
//                 const htmlHeaders = {
//                     method: "PATCH",
//                     body: JSON.stringify({name: textInput.value})
//                 }
//                 const resData = await fetch(`${BASE_URL}${currentId}`, htmlHeaders);
//                 console.log(currentId);
//                 loadHandler(event);
//             } 
//         }
//   }

//   async function addHandler(event) {
//     event.preventDefault();
//     const name = titleInput.value;
//     const htmlHeaders = {
//         method: "POST",
//         body: JSON.stringify({name})
//     }

//     const dataRes = await fetch(BASE_URL, htmlHeaders);
//     loadHandler(event);

//     titleInput.value = '';
//   }

//   function createElement(type, content, parentNode, id, classes, attributes, htmlInner) {
//     const htmlElement = document.createElement(type);

//     if (content && type !== 'input') {
//         htmlElement.textContent = content;
//     }

//     if (content && type === 'input') {
//         htmlElement.value = content;
//     }

//     if (id) {
//         htmlElement.id = id;
//     }

//     // ['list', ]
//     if (classes) {
//         htmlElement.classList.add(...classes);
//     }


//     // { src: 'link'}
//     if (attributes) {
//         for (const key in attributes) {
//             htmlElement.setAttribute(key, attributes[key])
//         }
//     }

//     if (htmlInner) {
//         htmlElement.innerHTML = htmlInner;
//     }

//     if(parentNode) {
//         parentNode.appendChild(htmlElement);
//     }
    
//     return htmlElement;
// }

// }

// attachEvents();



function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';
    const titleInput = document.getElementById('title');
    const addBtn = document.getElementById('add-button');
    const loadBtn = document.getElementById('load-button');
    const todoListContainer = document.getElementById('todo-list');

    loadBtn.addEventListener('click',loadTaskHandler);
    addBtn.addEventListener('click', addTaskHandler);

    function loadTaskHandler(event) {
        // event?.preventDefault();
        if (event) {
            event.preventDefault();
        }

        todoListContainer.innerHTML = '';
        fetch(BASE_URL)
            .then((data) => data.json())
            .then((tasksRes) => {
                const tasks = Object.values(tasksRes);

                for (const { _id, name } of tasks) {
                    const li = document.createElement('li');
                    const span = document.createElement('span');
                    const removeBtn = document.createElement('button');
                    const editBtn = document.createElement('button');

                    li.id = _id;
                    span.textContent = name;
                    removeBtn.textContent = 'Remove';
                    editBtn.textContent = 'Edit';

                    editBtn.addEventListener('click', loadEditFormHandler);
                    removeBtn.addEventListener('click', removeTaskHandler);
                    li.append(span, removeBtn, editBtn);
                    todoListContainer.appendChild(li);
                }
            })
            .catch((err) => {
                console.error(err);
            })
    }

    function loadEditFormHandler(event) {
        const liParent = event.currentTarget.parentNode;
        const [ span, _removeBtn, editBtn ] = Array.from(liParent.children);
        const editInput = document.createElement('input');

        editInput.value = span.textContent;
        liParent.prepend(editInput);

        const submitBtn = document.createElement('button');
        submitBtn.textContent = 'Submit';
        submitBtn.addEventListener('click', submitTaskHandler);
        liParent.appendChild(submitBtn);
        span.remove();
        editBtn.remove();
    }

    function submitTaskHandler(event) {
        const liParent = event.currentTarget.parentNode;
        const id = liParent.id;
        const [ input ] = Array.from(liParent.children);
        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({ name: input.value })
        };

        fetch(`${BASE_URL}${id}`, httpHeaders)
            .then(() => loadTaskHandler())
            .catch((err) => {
                console.error(err);
            })
    }

    function addTaskHandler(event) {
        if (event) {
            event.preventDefault();
        }
        const name = titleInput.value;
        const htmlHeaders = {
            method: 'POST',
            body: JSON.stringify({ name })
        }

        fetch(BASE_URL, htmlHeaders)
            .then(() => {
                loadTaskHandler();
                titleInput.value = '';
            })
            .catch((err) => {
                console.error(err);
            })
    }

    function removeTaskHandler(event) {
        const id = event.currentTarget.parentNode.id;
        const htmlHeaders = {
            method: 'DELETE'
        }

        fetch(`${BASE_URL}${id}`, htmlHeaders)
            .then(() => loadTaskHandler())
            .catch((err) => {
                console.error(err);
            })
    }
  }

attachEvents();