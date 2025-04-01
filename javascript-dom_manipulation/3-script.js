const header = document.querySelector('header');

const div_toggle = document.querySelector('#toggle_header');

div_toggle.addEventListener('click', () => {

    if (header.classList.contains('green')) {
        header.classList.replace('green', 'red')
    } else {
        header.classList.replace('red', 'green')
    }
})