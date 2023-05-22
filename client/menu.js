document.addEventListener('scroll',()=>{
    if (window.scrollY > 100) {
        document.body.classList.add('scrolled')
    } else {
        document.body.classList.remove('scrolled')
    }
})