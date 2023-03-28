async function loadRepos() {
	const BASE_URL = 'https://api.github.com/users';
	const username = document.getElementById('username');
	const repos = document.getElementById('repos');
	const usernameVal = username.value;

	try {
		const allRepositoriesRes = await fetch(`${BASE_URL}/${usernameVal}/repos`);
		const data = await allRepositoriesRes.json();
		repos.innerHTML = '';
		data
			.forEach(( data ) => {
				const li = document.createElement('li');
				repos.appendChild(li);

				const link = document.createElement('a');
				link.href = data.html_url;
				link.target = '_blank'
				link.textContent = data.full_name;
				li.appendChild(link)
			})
	} catch (err) {
		const li = document.createElement('li');
		li.textContent = err.message;
		repos.appendChild(li);
	}
}