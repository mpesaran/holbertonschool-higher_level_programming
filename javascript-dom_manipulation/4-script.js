const addItemDiv = document.querySelector('#add_item');

const myList = document.querySelector('.my_list');


addItemDiv.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';

    myList.appendChild(newItem);
});
