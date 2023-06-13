const BASE_URL = 'http://localhost:3030/jsonstore/tasks/'

const inputFields = {
    title: document.getElementById('course-name'),
    type: document.getElementById('course-type'),
    description: document.getElementById('description'),
    teacher: document.getElementById('teacher-name'),
}

const addCourseBtn = document.getElementById('add-course');
const editCourseBtn = document.getElementById('edit-course');

const loadCoursesBtn = document.getElementById('load-course');
const coursesContainer = document.getElementById('list');

let coursesDB = {};
let editID = null;

addCourseBtn.addEventListener('click', addCourseBtnHandler);
loadCoursesBtn.addEventListener('click', loadCoursesBtnHandler);

async function loadCoursesBtnHandler() {
    const allCoursesRes = await fetch(BASE_URL);
    const allCourses = await allCoursesRes.json();

    coursesContainer.innerHTML = '';
    coursesDB = {};

    Object.values(allCourses)
    .forEach((singleCourse) => {
        const { title, type, description, teacher, _id } = singleCourse;
        console.log( title, type, description, teacher, _id )
        const div = createElement('div', '', coursesContainer, _id, ['container']);
        createElement('h2', title, div);
        createElement('h3', teacher, div);
        createElement('h3', type, div);
        createElement('h4', `"${description}"`, div);
        const editBtn = createElement('button', 'Edit Course', div, '', ['edit-btn']);
        const finishBtn = createElement('button', 'Finish Course', div, '', ['finish-btn']);

        coursesDB[_id] = { title, type, description, teacher };
        
        editBtn.addEventListener('click', editBtnHandler);
        finishBtn.addEventListener('click', finishBtnHandler);
    })

    console.log(coursesDB)
}

async function finishBtnHandler() {
    const removeId = this.parentNode.id;
    const parent = this.parentNode;

    const htmlHeaders = {
        method: "DELETE"
    }

    const removeCourse = await fetch(`${BASE_URL}${removeId}`, htmlHeaders);
    coursesContainer.removeChild(parent);
    
    loadCoursesBtnHandler();
}

function editBtnHandler() {
    const currentId = this.parentNode.id;
    const parent = this.parentNode;
    editID = currentId;

    addCourseBtn.disabled = true;
    editCourseBtn.disabled = false;
    console.log(parent)
    coursesContainer.removeChild(parent);
    for (const key in inputFields) {
        console.log(key)
        console.log(coursesDB[currentId][key])
        console.log(inputFields[key].value)
        inputFields[key].value = coursesDB[currentId][key];
    }

    editCourseBtn.addEventListener('click', editCourseBtnHandler);

}

async function editCourseBtnHandler(event) {
    if (event) {
        event.preventDefault();
    }

    const title = inputFields.title.value;
    const type = inputFields.type.value;
    const description = inputFields.description.value;
    const teacher = inputFields.teacher.value;

    const htmlHeaders = {
        method: 'PUT',
        body: JSON.stringify({ title, type, description, teacher })
    };

    const editCourse = await fetch(`${BASE_URL}${editID}`, htmlHeaders);

    clearFields();
    loadCoursesBtnHandler();
    

    addCourseBtn.disabled = false;
    editCourseBtn.disabled = true;


}

async function addCourseBtnHandler(event) {
    if (event) {
        event.preventDefault();
    }
    if (inputFields.type.value === 'Long' || inputFields.type.value === 'Medium' || inputFields.type.value === 'Short') {
        const title = inputFields.title.value;
        const type = inputFields.type.value;
        const description = inputFields.description.value;
        const teacher = inputFields.teacher.value;

        const htmlHeaders = {
            method: 'POST',
            body: JSON.stringify({ title, type, description, teacher })
        };

        const addedNewCourse = await fetch(BASE_URL, htmlHeaders);

        clearFields();
        loadCoursesBtnHandler();

        
    }
}

function clearFields() {
    for (const key in inputFields) {
        inputFields[key].value = '';
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