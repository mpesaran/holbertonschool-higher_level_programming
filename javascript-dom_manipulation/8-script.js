fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
.then(response => response.json())
.then(data => {
    
    helloTranslate = data.hello;
    const helloDiv = document.querySelector('#hello');
    helloDiv.textContent = helloTranslate;
})
.catch(error => {
    console.error('Error fetching data:', error);
})