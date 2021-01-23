var body = document.querySelector('body')
var navbar = document.querySelector('nav')

// this function is called directly from HTML checkbox
function toggleTheme() {
    if (body.classList.contains('darkTheme')) {
        body.classList.remove('darkTheme')
        localStorage.removeItem('theme','darkTheme')
        navbar.classList.remove('navbar-dark','bg-dark')
        navbar.classList.add('navbar-light','bg-light')
    }
    else {
        body.classList.add('darkTheme')
        localStorage.setItem('theme','darkTheme')
        navbar.classList.add('navbar-dark','bg-dark')
        navbar.classList.remove('navbar-light','bg-light')
    }
}

// checking theme on reload and while browsing to other pages
(function(){
    if (localStorage.getItem('theme') == 'darkTheme') {
        body.classList.add('darkTheme')
        localStorage.setItem('theme','darkTheme')
        document.getElementById('slider').checked = false;
        navbar.classList.add('navbar-dark','bg-dark')
        navbar.classList.remove('navbar-light','bg-light')
    }
    else {
        body.classList.remove('darkTheme')
        localStorage.removeItem('theme','darkTheme')
        document.getElementById('slider').checked = true;
        navbar.classList.remove('navbar-dark','bg-dark')
        navbar.classList.add('navbar-light','bg-light')
    }
})()