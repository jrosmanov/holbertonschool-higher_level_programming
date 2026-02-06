const div = document.getElementById('toggle_header');
const header = document.querySelector('header');

function checker () {
    let class_name = header.className
    if (class_name == "red") {
        header.className = 'green';
    } else if (class_name == 'green') {
        header.className = 'red';
    } else {
        header.className = 'red';
    }
}

div.addEventListener('click', () => checker());