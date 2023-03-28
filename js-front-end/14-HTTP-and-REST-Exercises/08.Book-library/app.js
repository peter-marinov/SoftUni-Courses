function attachEvents() {
  const loadBooks = document.getElementById('loadBooks');
  const bookContainer = document.querySelector('table > tbody');
  const [ titleInput, authorInput ] = Array.from(document.querySelectorAll('#form > input'));
  const submitBtn = document.querySelector('#form > button');
  const formHeader = document.querySelector('#form > h3 ')
  
  const BASE_URL = 'http://localhost:3030/jsonstore/collections/books/';



  let allBooks = {};
  let editBookId = null;

  loadBooks.addEventListener('click', loadAllBooksHandler);
  submitBtn.addEventListener('click', submitFormHandler);
  

  async function loadAllBooksHandler() {
    bookContainer.innerHTML = '';
    console.log(bookContainer.innerHTML)

    const booksRes = await fetch(BASE_URL);
    const booksData = await booksRes.json();
    allBooks = booksData;

    for (const bookId in booksData) {
      const { author, title } = booksData[bookId];

      const tableRow = document.createElement('tr');
      const titleColumn = document.createElement('td');
      const authorColumn = document.createElement('td');
      const buttonsColumn = document.createElement('td');
      const editBtn = document.createElement('button');
      const deleteBtn = document.createElement('button');

      titleColumn.textContent = title;
      authorColumn.textContent = author;
      editBtn.textContent = 'Edit';
      deleteBtn.textContent = 'Delete';
      deleteBtn.id = bookId;
      
      editBtn.addEventListener('click', () => {
        editBookId = bookId;
        formHeader.textContent = 'Edit Form';
        submitBtn.textContent = 'Save';
        titleInput.value = title;
        authorInput.value = author;
      });

      deleteBtn.addEventListener('click', deleteBookHandler)

      // DOM Manipulations
      tableRow.appendChild(titleColumn);
      tableRow.appendChild(authorColumn);
      buttonsColumn.appendChild(editBtn);
      buttonsColumn.appendChild(deleteBtn);
      tableRow.appendChild(buttonsColumn);
      bookContainer.appendChild(tableRow);
    }

  }

  async function submitFormHandler(event) {
    event.preventDefault(); // prevents a form to refresh the page
    const title = titleInput.value;
    const author = authorInput.value;
    const httpHeaders = {
      method: 'POST',
      body: JSON.stringify({ title, author })
    }

    let url = BASE_URL

    if (submitBtn.textContent === 'Save') {
      httpHeaders.method = 'PUT';
      url += editBookId;
    }
    console.log(url, httpHeaders)
    const resData = await fetch(url, httpHeaders);
    loadAllBooksHandler();
    if (submitBtn.textContent === 'Save') {
      submitBtn.textContent = 'Submit';
      formHeader.textContent = 'FORM';
    }
    titleInput.value = '';
    authorInput.value = '';
  }

  async function deleteBookHandler() {
    const id = this.id;
    const httpHeaders = {
      method: 'DELETE'
    };
    console.log(BASE_URL + id)
    await fetch(BASE_URL + id, httpHeaders);
    loadAllBooksHandler();
  }
} 

attachEvents();