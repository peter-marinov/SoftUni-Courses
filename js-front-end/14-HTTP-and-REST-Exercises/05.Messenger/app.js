function attachEvents() {
    const BASE_URL = 'http://localhost:3030/jsonstore/messenger/';
    const textarea = document.getElementById('messages');
    const nameInput = document.getElementsByName('author')[0];
    const messageInput = document.getElementsByName('content')[0];
    const sendBtn = document.getElementById('submit');
    const refreshBtn = document.getElementById('refresh');

    sendBtn.addEventListener('click', sendHandler);

    async function sendHandler() {
        const author = nameInput.value;
        const content = messageInput.value;
        const htmlHeaders = {
            method: "POST",
            body: JSON.stringify({ author, content })
        };

        const dataRes = await fetch(BASE_URL, htmlHeaders);
        nameInput.value = '';
        messageInput.value = '';

    }

    refreshBtn.addEventListener('click', refreshHandler);

    async function refreshHandler() {
        textarea.value = '';
        const result = [];
        console.log('123')
        const allMessagesRes = await fetch(BASE_URL);
        let allMessages = await allMessagesRes.json();
        allMessages = Object.values(allMessages);
        allMessages
            .forEach((message) => {
                const { author, content } = message;
                result.push(`${author}: ${content}`);
            });

        textarea.value = result.join('\n');
    }
}

attachEvents();