const divName = document.querySelector('#character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        return response.json();
    })
    .then(data=> {
        divName.textContent = data.name;
    })
    .catch(error => {
        console.error(error)
    })