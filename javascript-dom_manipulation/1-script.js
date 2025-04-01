const redDiv = document.querySelector('#red_header');

const header = document.querySelector('header');

redDiv.addEventListener('click', () => {
    header.style.color = '#FF0000'
})