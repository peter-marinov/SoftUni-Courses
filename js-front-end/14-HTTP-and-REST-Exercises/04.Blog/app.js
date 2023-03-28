function attachEvents() {
    const loadBtn = document.getElementById('btnLoadPosts');
    const viewBtn = document.getElementById('btnViewPost');
    const postsContainer = document.getElementById('posts');
    const postTitle = document.getElementById('post-title');
    const postBody = document.getElementById('post-body');
    const postsComments = document.getElementById('post-comments');
    const POST_URL = 'http://localhost:3030/jsonstore/blog/posts/';
    const COMMENTS_URL = 'http://localhost:3030/jsonstore/blog/comments/'
    let posts = {};

    loadBtn.addEventListener('click', loadHandler);

    async function loadHandler() {
        const allPostsRes = await fetch(POST_URL);
        let allPosts = await allPostsRes.json();
        allPosts = Object.values(allPosts);
        allPosts
            .forEach((post) => {
                const { body, id, title } = post;
                posts[id] = [title, body];
                createElement('option', title, postsContainer, '', '', {value: id});
            });
    } 

    viewBtn.addEventListener('click', viewHandler);

    async function viewHandler() {
        const selectedId = postsContainer.value;
        const allPostsRes = await fetch(COMMENTS_URL);
        let allPosts = await allPostsRes.json();

        postTitle.textContent = posts[selectedId][0];
        postBody.textContent = posts[selectedId][1];
        postsComments.innerHTML = '';

        allPosts = Object.values(allPosts)
            .forEach((post) => {
                const { id, postId, text } = post;
                if (selectedId === postId) {
                    createElement('li', text, postsComments, id);
                }
            })
        
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
    
        if(parentNode) {
            parentNode.appendChild(htmlElement);
        }
        
        return htmlElement;
    }
}

attachEvents();