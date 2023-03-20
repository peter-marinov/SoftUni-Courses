window.addEventListener("load", solve);

function solve() {
  const firstName = document.getElementById('first-name');
  const lastName = document.getElementById('last-name');
  const age = document.getElementById('age');
  const storyTitle = document.getElementById('story-title');
  const genre = document.getElementById('genre');
  const storyText = document.getElementById('story');
  const btnPublish = document.getElementById('form-btn');
  const previewList = document.getElementById('preview-list');
  const mainDiv = document.getElementById('main');

  let informationDB = {};

  btnPublish.addEventListener('click', publishHandler);

  console.log(mainDiv)
  function publishHandler() {
    if (firstName.value === '' || lastName.value === '' || age.value === ''
      || storyTitle.value === '' || storyText.value === '') {
      return;
    }

    btnPublish.disabled = true;
   
    const storyInfo = createElement('li', '', previewList, '', ['story-info']);
    const previewArticle = createElement('article', '', storyInfo);
    const previewName = createElement('h4', `Name: ${firstName.value} ${lastName.value}`, previewArticle);
    const previewAge = createElement('p', `Age: ${age.value}`, previewArticle);
    const previewTitle = createElement('p', `Title: ${storyTitle.value}`, previewArticle);
    const previewGenre = createElement('p', `Genre: ${genre.value}`, previewArticle);
    const previewStoryText = createElement('p', storyText.value, previewArticle);
    const previewBtnSave = createElement('button', `Save Story`, storyInfo, '', ['save-btn']);
    const previewBtnEdit = createElement('button', `Edit Story`, storyInfo, '', ['edit-btn']);
    const previewBtnDelete = createElement('button', `Delete Story`, storyInfo, '', ['delete-btn']);
    
    informationDB = {
      firstName: firstName.value,
      lastName: lastName.value,
      age: age.value,
      title: storyTitle.value,
      genre: genre.value,
      storyText: storyText.value
    }

    firstName.value = '';
    lastName.value = '';
    age.value = '';
    storyTitle.value = '';
    genre.value = 'Disturbing';
    storyText.value = '';


    previewBtnSave.addEventListener('click', saveHandler);
    previewBtnEdit.addEventListener('click', editHandler);
    previewBtnDelete.addEventListener('click', deleteHandler);
  }

  function saveHandler() {
    mainDiv.innerHTML = '<h1>Your scary story is saved!</h1>';
  }

  function editHandler(e) {
    
    btnPublish.disabled = false;
    firstName.value = informationDB.firstName;
    lastName.value = informationDB.lastName;
    age.value = informationDB.age;
    storyTitle.value = informationDB.title;
    genre.value = informationDB.genre;
    storyText.value = informationDB.storyText;
    removeInfo();
  }

  function deleteHandler() {
    btnPublish.disabled = false;
    removeInfo();
  }

  function removeInfo() {
    previewList.innerHTML = '<h3>Preview</h3>';
  }

  function createElement(type, content, parentNode, id, classes, attributes) {
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

    if(parentNode) {
        parentNode.appendChild(htmlElement);
    }
    
    return htmlElement;
  }
}


