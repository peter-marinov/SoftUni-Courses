window.addEventListener('load', solve);

function solve() {
    const genreElement = document.getElementById('genre');
    const nameElement = document.getElementById('name');
    const authorElement = document.getElementById('author');
    const dateElement = document.getElementById('date');
    const addBtnElement = document.getElementById('add-btn');
    const collectionSongs = document.getElementsByClassName('all-hits-container')[0];
    const collectionSaved = document.getElementsByClassName('saved-container')[0];
    const totalLikes = Array.from(document.querySelectorAll('#total-likes .likes > p'))[0];

    addBtnElement.type = 'button';
    addBtnElement.addEventListener('click', addSongHandler);

    function addSongHandler() {
        if (genreElement.value === '' || nameElement.value === '' ||
            authorElement.value === '' || dateElement.value === '') {
            return;
        }

        const newSong = createElement('div', '', collectionSongs, '', ['hits-info']);
        const newSongImg = createElement('img', '', newSong, '', '', {src: './static/img/img.png'});
        const newSongGenre = createElement('h2', `Genre: ${genreElement.value}`, newSong);
        const newSongName = createElement('h2', `Name: ${nameElement.value}`, newSong);
        const newSongAuthor = createElement('h2', `Author: ${authorElement.value}`, newSong);
        const newSongDate = createElement('h3', `Date: ${dateElement.value}`, newSong);
        const newSongSaveBtn = createElement('button', 'Save song', newSong, '', ['save-btn']);
        const newSongLikeBtn = createElement('button', 'Like song', newSong, '', ['like-btn']);
        const newSongDeleteBtn = createElement('button', 'Delete', newSong, '', ['delete-btn']);
        
        genreElement.value = '';
        nameElement.value = '';
        authorElement.value = '';
        dateElement.value = '';

        newSongSaveBtn.addEventListener('click', saveBtnHandler);

        function saveBtnHandler(e) {
            const currentSaveBtn = e.currentTarget;
            const currentSaveBtnParent =  currentSaveBtn.parentElement;
            const likeBtn = Array.from(currentSaveBtnParent.getElementsByClassName('like-btn'))[0];
            const saveBtn = Array.from(currentSaveBtnParent.getElementsByClassName('save-btn'))[0];
            
            currentSaveBtnParent.removeChild(likeBtn);
            currentSaveBtnParent.removeChild(saveBtn);
            collectionSaved.appendChild(currentSaveBtnParent);
        }

        newSongLikeBtn.addEventListener('click', likeBtnHandler);

        function likeBtnHandler(e) {
            const currentBtn = e.currentTarget;
            const lastIndex = totalLikes.textContent.length - 1;
            let likes = Number(totalLikes.textContent[lastIndex]) + 1;
            totalLikes.textContent = "Total Likes: " + likes;
            currentBtn.disabled = true;
        }

        newSongDeleteBtn.addEventListener('click', deleteBtnHandler);

        function deleteBtnHandler(e) {
            const currentDeleteBtn = e.currentTarget;
            currentDeleteBtn.parentElement.remove();
        };

    }

    function createElement(type, content, parentNode, id, classes, attributes) {
        const htmlElement = document.createElement(type);

        if (content && (type !== 'input' && type !== 'textarea')) {
            htmlElement.textContent = content;
        }

        if (content && (type === 'input' || type === 'textarea')) {
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

        if (parentNode) {
            parentNode.appendChild(htmlElement);
        }

        return htmlElement;
    }
}