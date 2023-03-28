// function loadCommits() {
//     const BASE_URL = 'https://api.github.com/repos/';
//     const username = document.getElementById('username');
//     const repo = document.getElementById('repo');
//     const commits = document.getElementById('commits');
//     const loader = document.getElementById('loader');
//     const usernameVal = username.value;
//     const repoVal = repo.value;


//     fetch(`${BASE_URL}${usernameVal}/${repoVal}/commits`)
//         .then((res) => res.json())
//         .then((data) => {
//             loader.style.display = 'none'
//             data
//                 .forEach(({commit}) => {
//                     const li = document.createElement('li');
//                     li.textContent = `${commit.author.name}: ${commit.message}`;
//                     commits.appendChild(li);
//                 });
//         })
//         .catch((err) => {
//             const li = document.createElement('li');
//             li.textContent = err.message;
//             commits.appendChild(li);
//         })
// }


async function loadCommits() {
    const BASE_URL = 'https://api.github.com/repos/';
    const username = document.getElementById('username');
    const repo = document.getElementById('repo');
    const commits = document.getElementById('commits');
    const loader = document.getElementById('loader');
    const usernameVal = username.value;
    const repoVal = repo.value;


    try {
        loader.style.display = 'block';
        const allCommitsRes = await fetch(`${BASE_URL}${usernameVal}/${repoVal}/commits`);
        const data = await allCommitsRes.json();
        loader.style.display = 'none'
        data
            .forEach(({ commit }) => {
                const li = document.createElement('li');
                li.textContent = `${commit.author.name}: ${commit.message}`;
                commits.appendChild(li);
            })
    } catch (err) {
        const li = document.createElement('li');
        li.textContent = err.message;
        commits.appendChild(li);
    }
    
}