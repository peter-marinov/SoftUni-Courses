// function attachEvents() {
//   const firstNameInput = document.getElementsByName('firstName')[0];
//   const lastNameInput = document.getElementsByName('lastName')[0];
//   const facultyNumberInput = document.getElementsByName('facultyNumber')[0];
//   const gradeInput = document.getElementsByName('grade')[0];
  
//   const submitBtn = document.getElementById('submit');
//   const tableBody = document.querySelector('#results > tbody');
//   const BASE_URL = 'http://localhost:3030/jsonstore/collections/student/'

//   submitBtn.addEventListener('click', submitHandler);
  
//   async function submitHandler() {
//     const firstName = firstNameInput.value;
//     const lastName = lastNameInput.value;
//     const facultyNumber = facultyNumberInput.value;
//     const grade = gradeInput.value;
//     if (!checkIfInputsAreOkay()) {
//       return;
//     }

//     const htmlHeaders = {
//       method: "POST",
//       body: JSON.stringify({ firstName, lastName, facultyNumber, grade })
//     };

//     const dataRes = await fetch(BASE_URL, htmlHeaders);

//     const row = createElement('tr', '', tableBody);
//     console.log(row)
//     createElement('td', firstName, row);
//     createElement('td', lastName, row);
//     createElement('td', facultyNumber, row);
//     createElement('td', grade, row);

//     firstNameInput.value = '';
//     lastNameInput.value = '';
//     facultyNumberInput.value = '';
//     gradeInput.value = '';
    
//   }

//   function checkIfInputsAreOkay() {
//     if (firstNameInput.value.trim() === '' || lastNameInput.value.trim() === '' || 
//       facultyNumberInput.value.trim() === '' || gradeInput.value.trim() === '') {
//         return false
//       }
      
//     return true
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
  const baseURL = "http://localhost:3030/jsonstore/collections/students";
  const tbody = document.querySelector("tbody");
  const submitButtonElement = document.getElementById("submit");
  const inputElements = Array.from(document.querySelectorAll(".inputs input"));
  submitButtonElement.addEventListener("click", enrollStudent);
  loadStudents();
  async function loadStudents() {
    try {
      const response = await fetch(baseURL);
      const data = await response.json();
      Object.values(data).forEach((x) => {
        const grade = Number(x.grade);
        const tableRow = createHTMLElement("tr", "", tbody, "");
        createHTMLElement("td", x.firstName, tableRow, "");
        createHTMLElement("td", x.lastName, tableRow, "");
        createHTMLElement("td", x.facultyNumber, tableRow, "");
        createHTMLElement("td", `${grade.toFixed(2)}`, tableRow, "");
      });
    } catch (error) {
      console.error(error);
    }
  }

  async function enrollStudent() {
    let values = inputElements.map((input) => input.value);
    if (values.filter((word) => word === "").length > 0) {
      return;
    }
    let bodyObject = {
      firstName: values[0],
      lastName: values[1],
      facultyNumber: values[2],
      grade: values[3],
    };
    try {
      await fetch(baseURL, {
        method: "POST",
        "Content-type": "application/json",
        body: JSON.stringify(bodyObject),
      }).then(() => {
        tbody.textContent = "";
        loadStudents();
      });
    } catch (error) {
      console.error(error);
    }
  }
  function createHTMLElement(typeOfElement, content, parent, classList) {
    const element = document.createElement(typeOfElement);
    if (content) {
      element.textContent = content;
    }
    if (parent) {
      parent.appendChild(element);
    }
    if (classList) {
      element.classList.add(classList);
    }
    return element;
  }
}

attachEvents();