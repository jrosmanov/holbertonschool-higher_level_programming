const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const div = document.querySelector('#character');
fetch(url)
    .then(response => response.json())
    .then(data => {
        div.textContent = data['name'];
    })
