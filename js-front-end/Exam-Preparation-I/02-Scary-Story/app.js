// window.addEventListener("load", solve);

// function solve() {
//   const firstName = document.getElementById('first-name');
//   const lastName = document.getElementById('last-name');
//   const age = document.getElementById('age');
//   const storyTitle = document.getElementById('story-title');
//   const genre = document.getElementById('genre');
//   const storyText = document.getElementById('story');
//   const btnPublish = document.getElementById('form-btn');
//   const previewList = document.getElementById('preview-list');
//   const mainDiv = document.getElementById('main');

//   let informationDB = {};

//   btnPublish.addEventListener('click', publishHandler);

//   console.log(mainDiv)
//   function publishHandler() {
//     if (firstName.value === '' || lastName.value === '' || age.value === ''
//       || storyTitle.value === '' || storyText.value === '') {
//       return;
//     }

//     btnPublish.disabled = true;
   
//     const storyInfo = createElement('li', '', previewList, '', ['story-info']);
//     const previewArticle = createElement('article', '', storyInfo);
//     const previewName = createElement('h4', `Name: ${firstName.value} ${lastName.value}`, previewArticle);
//     const previewAge = createElement('p', `Age: ${age.value}`, previewArticle);
//     const previewTitle = createElement('p', `Title: ${storyTitle.value}`, previewArticle);
//     const previewGenre = createElement('p', `Genre: ${genre.value}`, previewArticle);
//     const previewStoryText = createElement('p', storyText.value, previewArticle);
//     const previewBtnSave = createElement('button', `Save Story`, storyInfo, '', ['save-btn']);
//     const previewBtnEdit = createElement('button', `Edit Story`, storyInfo, '', ['edit-btn']);
//     const previewBtnDelete = createElement('button', `Delete Story`, storyInfo, '', ['delete-btn']);
    
//     informationDB = {
//       firstName: firstName.value,
//       lastName: lastName.value,
//       age: age.value,
//       title: storyTitle.value,
//       genre: genre.value,
//       storyText: storyText.value
//     }

//     firstName.value = '';
//     lastName.value = '';
//     age.value = '';
//     storyTitle.value = '';
//     genre.value = 'Disturbing';
//     storyText.value = '';


//     previewBtnSave.addEventListener('click', saveHandler);
//     previewBtnEdit.addEventListener('click', editHandler);
//     previewBtnDelete.addEventListener('click', deleteHandler);
//   }

//   function saveHandler() {
//     mainDiv.innerHTML = '<h1>Your scary story is saved!</h1>';
//   }

//   function editHandler(e) {
    
//     btnPublish.disabled = false;
//     firstName.value = informationDB.firstName;
//     lastName.value = informationDB.lastName;
//     age.value = informationDB.age;
//     storyTitle.value = informationDB.title;
//     genre.value = informationDB.genre;
//     storyText.value = informationDB.storyText;
//     removeInfo();
//   }

//   function deleteHandler() {
//     btnPublish.disabled = false;
//     removeInfo();
//   }

//   function removeInfo() {
//     previewList.innerHTML = '<h3>Preview</h3>';
//   }

//   function createElement(type, content, parentNode, id, classes, attributes) {
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

//     if(parentNode) {
//         parentNode.appendChild(htmlElement);
//     }
    
//     return htmlElement;
//   }
// }


window.addEventListener('load', solve);

function solve() {
  const storyState = {
    firstName: null,
    lastName: null,
    age: null,
    title: null,
    genre: null,
    story: null,
  };

  const inputDOMselectors = {
    firstName: document.getElementById('first-name'),
    lastName: document.getElementById('last-name'),
    age: document.getElementById('age'),
    title: document.getElementById('story-title'),
    genre: document.getElementById('genre'),
    story: document.getElementById('story'),
  };

  const otherDOMSelectors = {
    publishBtn: document.getElementById('form-btn'),
    previewList: document.getElementById('preview-list'),
    mainContainer: document.getElementById('main'),
  };

  otherDOMSelectors.publishBtn.addEventListener('click', publishStoryHandler);
  
  function publishStoryHandler(event) {
    const allFieldsHaveValue = Object.values(inputDOMselectors)
      .every((input) => input.value !== '');

    if (!allFieldsHaveValue) {
      console.log('Empty fields')
      return;
    }

    const { firstName, lastName, age, title, genre, story } = inputDOMselectors;
    const li = createElement('li', otherDOMSelectors.previewList, null, ['story-info']);
    const article = createElement('article', li);
    createElement('h4', article, `Name: ${firstName.value} ${lastName.value}`);
    createElement('p', article, `Age: ${age.value}`);
    createElement('p', article, `Title: ${title.value}`);
    createElement('p', article, `Genre: ${genre.value}`);
    createElement('p', article, story.value);
    const saveBtn = createElement('button', li, 'Save Story', ['save-btn']);
    const editBtn = createElement('button', li, 'Edit Story', ['edit-btn']);
    const deleteBtn = createElement('button', li, 'Delete Story', ['delete-btn']);

    saveBtn.addEventListener('click', saveStoryHandler);
    editBtn.addEventListener('click', editStoryHandler);
    deleteBtn.addEventListener('click', deleteStoryHandler);

    for (const key in inputDOMselectors) {
      storyState[key] = inputDOMselectors[key].value;
    }

    clearAllInputs();
    otherDOMSelectors.publishBtn.setAttribute('disabled', true);
  }

  function editStoryHandler() {
    for (const key in inputDOMselectors) {
      inputDOMselectors[key].value = storyState[key];
    }

    otherDOMSelectors.publishBtn.removeAttribute('disabled');
    otherDOMSelectors.previewList.innerHTML = '';
    createElement('h3', otherDOMSelectors.previewList, 'Preview');
  }

  function deleteStoryHandler() {
    const liItem = this.parentNode;
    liItem.remove();
    otherDOMSelectors.publishBtn.removeAttribute('disabled');
  }

  function saveStoryHandler() {
    otherDOMSelectors.mainContainer.innerHTML = '';
    createElement('h1', otherDOMSelectors.mainContainer, 'Your scary story is saved!')
  }

  function clearAllInputs() {
    Object.values(inputDOMselectors)
      .forEach((input) => {
        input.value = '';
      })
  }

  function createElement(type, parentNode, content, classes, id, attributes, useInnerHtml) {
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

        if (classes) {
            htmlElement.classList.add(...classes);
        }

        if (id) {
            htmlElement.id = id;
        }

        if (attributes) {
            for (const key in attributes) {
                htmlElement.setAttribute(key, attributes[key]);
            }
        }

        if(parentNode) {
            parentNode.appendChild(htmlElement);
        }

        return htmlElement;
  }
}