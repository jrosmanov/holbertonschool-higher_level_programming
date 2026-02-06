const header = document.querySelector('header');
const btn = document.querySelector('#update_header');

btn.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
})