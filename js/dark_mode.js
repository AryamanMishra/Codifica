var body = document.querySelector('body')
function toggleTheme() {
    if (body.classList.contains('darkTheme')) {
        body.classList.remove('darkTheme')
        localStorage.removeItem('theme','darkTheme')
    }
    else {
        body.classList.add('darkTheme')
        localStorage.setItem('theme','darkTheme')
    }
}
(function(){
    if (localStorage.getItem('theme') == 'darkTheme') {
        body.classList.add('darkTheme')
        localStorage.setItem('theme','darkTheme')
        document.getElementById('slider').checked = false;
    }
    else {
        body.classList.remove('darkTheme')
        localStorage.removeItem('theme','darkTheme')
        document.getElementById('slider').checked = true;
    }
})()