window.addEventListener('load', solve);

function solve() {
    const userInputs = {
        title: document.getElementById('title'),
        description: document.getElementById('description'),
        label: document.getElementById('label'),
        estimatedPoints: document.getElementById('points'),
        assignee: document.getElementById('assignee'),
    }

    const createTaskBtn = document.getElementById('create-task-btn');
    const deleteTaskBtn = document.getElementById('delete-task-btn');

    const pointsContainer = document.getElementById('total-sprint-points');
    const tasksContainer = document.getElementById('tasks-section');

    const taskId = document.getElementById('task-id');

    createTaskBtn.addEventListener('click', addTaskHandler);
    deleteTaskBtn.addEventListener('click', deleteTasksBtnHandler);
    let articleID = 0;
    let currentPoints = 0;

    let tasksDB = {};

    function addTaskHandler() {
        if (userInputs.title.value === '' || userInputs.description.value === '' || 
            userInputs.estimatedPoints.value === '' || userInputs.assignee.value === '') {
            return
        }
        articleID += 1;
        let taskPriority = '';
        let priority = '';
        if (label.value === 'Feature') {
            taskPriority = '&#8865';
            priority = 'feature';
        } else if (label.value === 'Low Priority Bug') {
            taskPriority = '&#9737';
            priority = 'low-priority';
        } else {
            taskPriority = '&#9888';
            priority = 'high-priority';
        }
        console.log(userInputs)
        const article = createElement('article', '', tasksContainer, `task-${articleID}`, ['task-card']);
        const element = createElement('div', '', article, '', ['task-card-label', priority], '', `${label.value} ${taskPriority}`);
        // Проверката от втория zero test
        console.log(document.querySelector("#tasks-section > article > .task-card-label").textContent === 'Low Priority Bug ☉');

        createElement('h3', userInputs.title.value, article, '', ['task-card-title']);
        createElement('p', userInputs.description.value, article, '', ['task-card-description']);
        createElement('div', `Estimated at ${userInputs.estimatedPoints.value}pts`, article, '', ['task-card-points']);
        createElement('div', `Assigned to: ${userInputs.assignee.value}`, article, '', ['task-card-assignee']);
        const divAction = createElement('div', '', article, '', ['task-card-actions']);
        const deleteBtn = createElement('button', 'Delete', divAction);
        
        handlePoints('add', Number(userInputs.estimatedPoints.value));

        deleteBtn.addEventListener('click', deleteTaskHandler);

        tasksDB[`task-${articleID}`] = {
            title: userInputs.title.value,
            description: userInputs.description.value,
            label: userInputs.label.value,
            estimatedPoints: userInputs.estimatedPoints.value,
            assignee: userInputs.estimatedPoints.value
        }

        for (key in userInputs) {
            userInputs[key].value = '';
        }
        userInputs.label.value = 'Feature';
        
    }

    function deleteTaskHandler(event) {
        const currentParent = event.currentTarget.parentNode.parentNode;
        const id = currentParent.id;

        for (key in userInputs) {
            userInputs[key].value = tasksDB[id][key];
            userInputs[key].disabled = true;
        }

        // delete tasksDB[id];
        // tasksContainer.removeChild(currentParent);
        createTaskBtn.disabled = true
        deleteTaskBtn.disabled = false

        taskId.value = id;

    }

    function deleteTasksBtnHandler() {
        const articleToRemove = document.getElementById(taskId.value);
        console.log(taskId)
        console.log(articleToRemove)
        tasksContainer.removeChild(articleToRemove);
        delete tasksDB[taskId.value];

        createTaskBtn.disabled = false
        deleteTaskBtn.disabled = true

        handlePoints('remove', userInputs.estimatedPoints.value);

        for (key in userInputs) {
            userInputs[key].value = '';
        }
        userInputs.label.value = 'Feature';
    }

    function handlePoints(argument, points) {
        if (argument === 'add') {
            currentPoints += Number(points);
        } else {
            currentPoints -= Number(points);
        }

        pointsContainer.textContent = `Total Points ${currentPoints}pts`
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
