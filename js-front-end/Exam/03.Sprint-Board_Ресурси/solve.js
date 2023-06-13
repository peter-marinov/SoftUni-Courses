// TODO:
function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/tasks/';

    const userTitle = document.getElementById('title');
    const userDescription = document.getElementById('description');

    const loadBoardBtn = document.getElementById('load-board-btn');
    const addTaskBtn = document.getElementById('create-task-btn');

    const toDoList = document.querySelector('#todo-section .task-list');
    const inProgressList = document.querySelector('#in-progress-section .task-list');
    const codeReviewList = document.querySelector('#code-review-section .task-list');
    const doneList = document.querySelector('#done-section .task-list');

    loadBoardBtn.addEventListener('click', loadBoardHandler);
    addTaskBtn.addEventListener('click', addTaskHandler);

    async function loadBoardHandler() {
        const allDataRes = await fetch(BASE_URL);
        let allData = await allDataRes.json();
        
        toDoList.innerHTML = '';
        inProgressList.innerHTML = '';
        codeReviewList.innerHTML = '';
        doneList.innerHTML = '';

        allData = Object.values(allData);
        allData
            .forEach(element => {
                const { title, description, status, _id } = element;
                if (status === 'ToDo') {
                    const li = createElement('li', '', toDoList, _id, ['task']);
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const todoBtn = createElement('button', 'Move to In Progress', li);

                    todoBtn.addEventListener('click', todoBtnHandler);
                } else if (status === 'In Progress') {
                    const li = createElement('li', '', inProgressList, _id, ['task']);
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const inProgressBtn = createElement('button', 'Move to Code Review', li);

                    inProgressBtn.addEventListener('click', inProgressBtnHandler);
                } else if (status === 'Code Review') {
                    const li = createElement('li', '', codeReviewList, _id, ['task']);
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const codeReviewBtn = createElement('button', 'Move to Done', li);

                    codeReviewBtn.addEventListener('click', codeReviewBtnHandler);
                } else {
                    const li = createElement('li', '', doneList, _id, ['task']);
                    createElement('h3', title, li);
                    createElement('p', description, li);
                    const doneBtn = createElement('button', 'Close', li);

                    doneBtn.addEventListener('click', doneBtnHandler);
                }
            });
    }

    async function todoBtnHandler(event) {
        const id = this.parentNode.id;
        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({status: 'In Progress'})
        }
        const changeStatus = await fetch(`${BASE_URL}${id}`, httpHeaders);
        loadBoardHandler();
    }

    async function inProgressBtnHandler() {
        const id = this.parentNode.id;
        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({status: 'Code Review'})
        }
        const changeStatus = await fetch(`${BASE_URL}${id}`, httpHeaders);
        loadBoardHandler();
    }

    async function codeReviewBtnHandler() {
        const id = this.parentNode.id;
        const httpHeaders = {
            method: 'PATCH',
            body: JSON.stringify({status: 'Done'})
        }
        const changeStatus = await fetch(`${BASE_URL}${id}`, httpHeaders);
        loadBoardHandler();
    }

    async function doneBtnHandler() {
        const id = this.parentNode.id;
        const httpHeaders = {
            method: 'DELETE',
        }
        const changeStatus = await fetch(`${BASE_URL}${id}`, httpHeaders);
        loadBoardHandler();
    }

    async function addTaskHandler() {
        const title = userTitle.value;
        const description = userDescription.value;
        const status = 'ToDo';
        const htmlHeaders = {
            method: "POST",
            body: JSON.stringify({ title, description, status })
        }

        const addNewData = await fetch(BASE_URL, htmlHeaders);

        loadBoardHandler();

        userTitle.value = '';
        userDescription.value = '';
    }

    function createElement(type, content, parentNode, id, classes, attributes, htmlInner) {
        const htmlElement = document.createElement(type);
    
        if (content && type !== 'input') {
            htmlElement.textContent = content;
        }
    
        if (content && type === 'input') {
            htmlElement.value = content;
        }
    
        if (id) {
            htmlElement.id = id;
        }
    
        // ['list', ]
        if (classes) {
            htmlElement.classList.add(...classes);
        }
    
    
        // { src: 'link'}
        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key])
            }
        }
    
        if (htmlInner) {
            htmlElement.innerHTML = htmlInner;
        }
    
        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }
    
        return htmlElement;
    }
}

attachEvents();