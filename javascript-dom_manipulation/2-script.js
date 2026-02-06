const div = document.getElementById('red_header');
const header = document.querySelector('header');

div.addEventListener('click', () => header.setAttribute('class', 'red'));