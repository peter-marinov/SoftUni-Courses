window.addEventListener("load", solve);

function solve() {
    const userInputs = {
        title: document.getElementById('task-title'),
        category: document.getElementById('task-category'),
        content: document.getElementById('task-content'),
    }

    const publishBtn = document.getElementById('publish-btn');
    const reviewContainer = document.getElementById('review-list');
    const publishedContainer = document.getElementById('published-list');
    let currentId = 0;
    let tasksDB = {};

    publishBtn.addEventListener('click', publishBtnHandler);

    function publishBtnHandler() {
        if (!userInputs.title.value || !userInputs.category.value || !userInputs.content.value) {
            return
        }

        currentId++;

        const li = createElement('li', '', reviewContainer, `id-${currentId}`, ['rpost']);
        const article = createElement('article', '', li);
        createElement('h4', userInputs.title.value, article);
        createElement('p', `Category: ${userInputs.category.value}`, article);
        createElement('p', `Content: ${userInputs.content.value}`, article);
        const editBtn = createElement('button', 'Edit', li, '', ['action-btn', 'edit']);
        const postBtn = createElement('button', 'Post', li, '', ['action-btn', 'post']);

        tasksDB[`id-${currentId}`] = {
            title: userInputs.title.value,
            category: userInputs.category.value,
            content: userInputs.content.value,
        }

        clearInputs();

        editBtn.addEventListener('click', editBtnHandler);
        postBtn.addEventListener('click', postBtnHandler);
    }

    function editBtnHandler() {
        const taskId = this.parentNode.id;
        const child = this.parentNode;
        
        for (const key in userInputs) {
            userInputs[key].value = tasksDB[taskId][key];
        }

        reviewContainer.removeChild(child);
        delete tasksDB[taskId];
    }

    function postBtnHandler() {
        const taskId = this.parentNode.id;
        const child = this.parentNode;
        const buttons = Array.from(child.querySelectorAll('button'));
        buttons
            .forEach(button => child.removeChild(button));

        publishedContainer.appendChild(child);

    }

    function clearInputs() {
        for (const key in userInputs) {
            userInputs[key].value = '';
        }
    }

    function createElement(type, content, parentNode, id, classes, attributes, useInnerHtml) {
        const htmlElement = document.createElement(type);


        if (content && useInnerHtml) {
            htmlElement.innerHTML = content;
        } else {
            if (content && type !== 'input') {
                htmlElement.textContent = content;
            }
            if (content && type === 'input') {
                htmlElement.value = content;
            }
        }

        if (id) {
            htmlElement.id = id;
        }

        if (classes) {
            htmlElement.classList.add(...classes);
        }

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key]);
            }
        }
        return htmlElement;
    }
}