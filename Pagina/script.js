function addBackgroundImage() {
var div = document.getElementById('background-image');
div.style.backgroundImage = 'url("Pagina/Imagem.jpg")';
div.style.backgroundSize = 'cover';
div.style.backgroundPosition = 'center';
div.style.width = '100%';
div.style.height = '100vh';
div.style.position = 'fixed';
div.style.top = '0';
div.style.left = '0';
div.style.zIndex = '-1';


}

addBackgroundImage();