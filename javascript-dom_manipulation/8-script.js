document.addEventListener('DOMContentLoaded', () => {
    const div = document.querySelector('#hello');
  
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then (res => res.json())
        .then (data => {
            div.textContent = data['hello']
        })
  });