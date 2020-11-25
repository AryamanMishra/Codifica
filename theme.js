document.getElementById('themeChange').addEventListener('click',function() {
    let darkThemeEnabled = document.body.classList.toggle('darkTheme');
    localStorage.setItem('dark-theme-enabled',darkThemeEnabled)
});

if (localStorage.getItem('dark-theme-enabled')) {
    document.body.classList.add('darkTheme');
}