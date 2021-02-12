var body = document.querySelector('body')
var icon = document.getElementById('themeChanger')
var navbar = document.querySelector('nav')
var editor = document.getElementById('editor')

// this function gets called on every click on the moon/sun icon
function toggleTheme() {
    if (body.classList.contains('darkTheme')) {
        body.classList.remove('darkTheme')
        icon.src = "images/night.png"
        localStorage.removeItem('theme','darkTheme')
        navbar.classList.remove('navbar-dark','bg-dark')
        navbar.classList.add('navbar-light','bg-light')
        editor.setTheme("ace/theme/eclipse")
        localStorage.removeItem("editorTheme","twilight")
    }
    else {
        body.classList.add('darkTheme')
        icon.src = "images/sunny.png"
        localStorage.setItem('theme','darkTheme')
        navbar.classList.add('navbar-dark','bg-dark')
        navbar.classList.remove('navbar-light','bg-light')
        editor.setTheme("ace/theme/twilight")
        localStorage.setItem("editorTheme","twilight")
    }
} 

// this function executes on every reload
(function() {
    if (localStorage.getItem('theme') == 'darkTheme') {
        body.classList.add('darkTheme')
        icon.src = "images/sunny.png"
        localStorage.setItem('theme','darkTheme')
        navbar.classList.add('navbar-dark','bg-dark')
        navbar.classList.remove('navbar-light','bg-light')
    }
    else {
        body.classList.remove('darkTheme')
        icon.src = "images/night.png"
        localStorage.removeItem('theme','darkTheme')
        navbar.classList.remove('navbar-dark','bg-dark')
        navbar.classList.add('navbar-light','bg-light')
    }
})()