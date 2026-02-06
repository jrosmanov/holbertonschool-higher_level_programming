const list = document.querySelector('.my_list');
const btn = document.querySelector('#add_item');

btn.addEventListener('click', function() {
    const li = document.createElement('li');
    li.textContent = 'Item'
    list.appendChild(li)
})
