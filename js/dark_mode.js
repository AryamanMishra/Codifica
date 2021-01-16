var btn = document.getElementById('themeChanger')
var body = document.querySelector('body')
btn.addEventListener('click',onImgClick) 
function onImgClick() {
    if (body.classList.contains('darkTheme')) {
        body.classList.remove('darkTheme')
        localStorage.removeItem('themeChanger','darkTheme')
    }
    else {
        body.classList.add('darkTheme')
        localStorage.setItem('themeChanger','darkTheme')
    }
}