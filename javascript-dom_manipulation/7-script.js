const my_list = document.querySelector('#list_movies')

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data=> {
    data.results.forEach(movie => {
        const newItem = document.createElement('li');
        newItem.textContent = movie.title;
        my_list.appendChild(newItem)
    });
})
.catch(error => {
    console.error(error)
})