const menu = document.getElementById("nav-links")
const handleMenu = document.getElementById("handle-menu")


handleMenu.addEventListener("click", ()=>{
    console.log("clicked")
    menu.classList.toggle("hidden")
})