const list = document.querySelector('#list_movies');
const element = document.createElement('li');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(res => res.json())
  .then(data => {
    data.results.forEach(film => {
        const element = document.createElement('li')
        element.textContent = film.title
        list.appendChild(element)
})});