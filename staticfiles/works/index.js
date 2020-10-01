document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#games').addEventListener('click', ()=>loadGames());
    document.querySelector('#models').addEventListener('click', ()=>loadModels());
    loadGames();
});

function loadGames() {
    document.querySelector('#allgames').style.display = 'block';
    document.querySelector('#allmodels').style.display = 'none';
}

function loadModels() {
    document.querySelector('#allgames').style.display = 'none';
    document.querySelector('#allmodels').style.display = 'block';
}