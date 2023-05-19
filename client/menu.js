document.addEventListener('scroll',()=>{
    if (window.scrollY > 100) {
        document.body.classList.add('menu-open')
    } else {
        document.body.classList.remove('menu-open')
    }
})