const BASE_URL = 'http://localhost:3030/jsonstore/grocery/';
const inputFields = {
    product: document.getElementById('product'),
    count: document.getElementById('count'),
    price: document.getElementById('price'),
}
const addProductBtn = document.getElementById('add-product');
const updateProductBtn = document.getElementById('update-product');
const loadProductBtn = document.getElementById('load-product');
const tableContainer = document.getElementById('tbody');
let allCurrentProducts = {};
let currentId = null;

loadProductBtn.addEventListener('click', loadProductsHandler);
addProductBtn.addEventListener('click', addProductHandler);
updateProductBtn.addEventListener('click', submitUpdateProductHandler);

async function loadProductsHandler(event) {
    if (event) {
        event.preventDefault();
    }
    tableContainer.innerHTML = '';
    allCurrentProducts = {};

    const allProductsRes = await fetch(BASE_URL);
    const allProducts = await allProductsRes.json();
    Object.values(allProducts)
        .forEach((singleProduct) => {
            const { product, count, price, _id } = singleProduct;
            const row = createElement('tr', '', tableContainer, _id);
            createElement('td', product, row, '', ['name']);
            createElement('td', count, row, '', ['count-product']);
            createElement('td', price, row, '', ['product-price']);
            const buttons = createElement('td', '', row, '', ['btn']);
            const updateBtn = createElement('button', 'Update', buttons, '', ['update']);
            const deleteBtn = createElement('button', 'Delete', buttons, '', ['delete']);

            deleteBtn.addEventListener('click', removeProductHandler);
            updateBtn.addEventListener('click', updateProductHandler);

            allCurrentProducts[_id] = { product, count, price };
        })

    // addProductBtn.disabled = false;
    // updateProductBtn.disabled = true;

}

async function addProductHandler(event) {
    if (event) {
        event.preventDefault();
    }
    const product = inputFields.product.value;
    const count = inputFields.count.value;
    const price = inputFields.price.value;

    const htmlHeaders = {
        method: "POST",
        body: JSON.stringify({ product, count, price })
    }

    const addedProductRes = await fetch(BASE_URL, htmlHeaders);

    for (const key in inputFields) {
        inputFields[key].value = '';
    }

    loadProductsHandler();
}

async function removeProductHandler() {
    const id = this.parentNode.parentNode.id;
    const htmlHeaders = {
        method: "DELETE",
    }

    const deleteRes = await fetch(`${BASE_URL}${id}`, htmlHeaders);
    loadProductsHandler();
}

function updateProductHandler() {
    const id = this.parentNode.parentNode.id;
    addProductBtn.disabled = true;
    updateProductBtn.disabled = false;
    for (const field in inputFields) {
        inputFields[field].value = allCurrentProducts[id][field];
    }

    currentId = id;

}

async function submitUpdateProductHandler(event) {
    if (event) {
        event.preventDefault();
    }
    console.log(currentId)
    const product = inputFields.product.value;
    const count = inputFields.count.value;
    const price = inputFields.price.value;
    const htmlHeaders = {
        method: "PATCH",
        body: JSON.stringify({ product, count, price })
    }
    console.log(`${BASE_URL}${currentId}`)
    console.log(htmlHeaders)
    const patchRes = await fetch(`${BASE_URL}${currentId}`, htmlHeaders);

    loadProductsHandler();

    addProductBtn.disabled = false;
    updateProductBtn.disabled = true;

    for (const key in inputFields) {
        inputFields[key].value = '';
    }
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