var body = document.querySelector('body')
if (localStorage.getItem('themeChanger')=='darkTheme') {
    body.classList.add('darkTheme')
    localStorage.setItem('themeChanger','darkTheme')
}
else {
    body.classList.remove('darkTheme')
    localStorage.removeItem('themeChanger','darkTheme')
}