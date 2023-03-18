function validate() {
    const input = document.getElementById('email');
    input.addEventListener('change', emailCheck);
    function emailCheck(e) {
        const fullEmail = e.currentTarget;
        const usernamePattern = /[a-z]+(?=\@)/gm;
        const domainPattern = /(?<=\@)[a-z]+(?=\.)/gm;
        const extensionPattern = /(?<=\.)[a-z]+/gm;
        let username = fullEmail.value.match(usernamePattern);
        let domain = fullEmail.value.match(domainPattern);
        let extension = fullEmail.value.match(extensionPattern);
        
        if (username && domain && extension) {
            fullEmail.className = '';
        } else {
            fullEmail.className = 'error';
        }
        
    }
}