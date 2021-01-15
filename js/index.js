var btn = document.getElementById('themeChanger')
var body = document.querySelector('body')
btn.addEventListener('click',onImgClick) 
function onImgClick() {
    if (body.classList.contains('darkTheme')) {
        body.classList.remove('darkTheme')
    }
    else {
        body.classList.add('darkTheme')
    }
    if (btn.src.match("/images/sun.png")) {
        btn.src = "/images/moon.png"
        btn.style.width = "50px"
    }
    else {
        btn.src = "/images/sun.png"
        btn.style.width = "60px"
    }
}
// dark mode to stay on refresh, need to use cookies