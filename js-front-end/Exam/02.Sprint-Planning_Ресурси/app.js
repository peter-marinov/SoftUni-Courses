window.addEventListener('load', solve);

function solve() {
    const userInput = {
        title: document.getElementById('title'),
        description: document.getElementById('description'),
        label: document.getElementById('label'),
        estimatedPoints: document.getElementById('points'),
        assignee: document.getElementById('assignee'),
    }

    const createTaskBtn = document.getElementById('create-task-btn');
    const deleteTaskBtn = document.getElementById('delete-task-btn');
    const tasksSection = document.getElementById('tasks-section');
    const sprintPoints = document.getElementById('total-sprint-points');
    const hiddenTaskId = document.getElementById('task-id');

    const codeMapper = {
        Feature: '&#8865',
        'Low Priority Bug': '&#9737',
        'High Priority Bug': '&#9888'
    }
    const classMapper = {
        Feature: 'feature',
        'Low Priority Bug': 'low-priority',
        'High Priority Bug': 'high-priority'
    }

    let task_id = 0;
    let currentPoints = 0;
    let tasksDB = {};

    createTaskBtn.addEventListener('click', createTaskBtnHandler);
    deleteTaskBtn.addEventListener('click', deleteTaskBtnHandler);

    deleteTaskBtn.disabled = true;

    function createTaskBtnHandler() {
        if (!userInput.title.value || !userInput.description.value || !userInput.label.value || !userInput.estimatedPoints.value || !userInput.assignee.value) {
            return
        }
        task_id += 1;

        const article = createElement('article', '', tasksSection, `task-${task_id}`, ['task-card']);
        createElement('div', `${userInput.label.value} ${codeMapper[userInput.label.value]}`, article, '', ['task-card-label', classMapper[userInput.label.value]], '', true);
        createElement('h3', userInput.title.value, article, '', ['task-card-title']);
        createElement('p', userInput.description.value, article, '', ['task-card-description']);
        createElement('div', `Estimated at ${userInput.estimatedPoints.value} pts`, article, '', ['task-card-points']);
        createElement('div', `Assigned to: ${userInput.assignee.value}`, article, '', ['task-card-assignee']);
        const div = createElement('div', '', article, '', ['task-card-actions']);
        const deleteBtn = createElement('button', 'Delete', div);

        currentPoints += Number(userInput.estimatedPoints.value);
        sprintPoints.innerHTML = `Total Points ${currentPoints}pts`;

        tasksDB[`task-${task_id}`] = {
            title: userInput.title.value,
            description: userInput.description.value,
            label: userInput.label.value,
            estimatedPoints: userInput.estimatedPoints.value,
            assignee: userInput.assignee.value,
        }

        for (const key in userInput) {
            userInput[key].value = '';
        }
        userInput['label'].value = 'Feature'
        hiddenTaskId.value = '';

        deleteBtn.addEventListener('click', deleteBtnHandler);

    }


    

    function deleteTaskBtnHandler() {
        idToRemove = hiddenTaskId.value;
        currentPoints -= Number(userInput.estimatedPoints.value);
        sprintPoints.innerHTML = `Total Points ${currentPoints}pts`;
        
        tasksSection.removeChild(document.getElementById(idToRemove));
        delete tasksDB[idToRemove];

        for (const key in userInput) {
            userInput[key].value = '';
            userInput[key].disabled = false;
        }
        userInput['label'].value = 'Feature'
        hiddenTaskId.value = '';

        createTaskBtn.disabled = false;
        deleteTaskBtn.disabled = true;
    }
    
    function deleteBtnHandler() {
        parentId = this.parentNode.parentNode.id;

        createTaskBtn.disabled = true;
        deleteTaskBtn.disabled = false;

        for (const key in userInput) {
            userInput[key].value = tasksDB[parentId][key];
            userInput[key].disabled = true;
        }

        hiddenTaskId.value = parentId;

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