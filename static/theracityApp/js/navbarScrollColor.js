const windowHeight = window.innerHeight;
const navBar = document.querySelector("nav");

document.addEventListener("scroll", () => {
    let scrollHeight = window.scrollY;

    if (scrollHeight >= windowHeight - 100) {
        navBar.classList.add("bgColorChange");
    } else {
        navBar.classList.remove("bgColorChange");
    }
})