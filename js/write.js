var chooseSite = document.getElementById('chooseSite')
chooseSite.addEventListener('change',function(event){
    if (event.target.value === 'codechef') {
        // codechef scrapping vali script add karni hei yahan
        console.log('CODECHEF')
    }
    else if (event.target.value === 'codeforces') {
        // codeforces scrapping vali script add karni hei yahan
        console.log('CODEFORCES')
    }
    else {
        alert('Select a Website')
    }
})

// for input validation, we will be adding the eventListener as
// ('input',function(event){
//      here, we can use event.target.value and verify the latest entered 
//      character is according to us or not
// })
