let menuOpen = false
let mobileView = false

if (document.cookie == "") {
document.cookie = 'background: 0;'
}

document.getElementById("myDropdown").style.display = "none";


function menu() {
    if (menuOpen) {
        menuOpen = false;
        document.getElementById("myDropdown").style.display = "none";
    }
    else {
        menuOpen = true;
        document.getElementById("myDropdown").style.display = "flex"
    }
}

function close() {
    menuOpen = false;
    document.getElementById("myDropdown").style.display = "none";
}

function update() {
    if (document.cookie.trim().startsWith("background: 1")) {
        document.body.style.backgroundColor = "var(--main-dark-grey)"
        document.getElementById("myDropdown").style.color = "#fff"
        document.getElementById("myDropdown").style.border = "var(--main-blue) solid 2px"
        document.getElementById("myDropdown").style.backgroundColor = "var(--main-dark-grey)"
        document.getElementById("header").style.backgroundColor = "var(--main-blue)"
        document.getElementsByTagName("footer")[0].style.backgroundColor = "var(--main-blue)"
        document.getElementById("content").style.color = "#fff"
        document.getElementsByClassName("menu-item")[1].style.border = "none"
        document.getElementsByClassName("menu-item")[0].style.border = "#888 solid 3px"
        document.getElementById("credits").style.color = "#fff"
        document.documentElement.style.setProperty('--link-color', 'var(--main-light-grey)')
    }
    else {
        document.body.style.backgroundColor = "var(--main-white)"
        document.getElementById("myDropdown").style.color = "#000"
        document.getElementById("myDropdown").style.border = "var(--main-dark-grey) solid 2px"
        document.getElementById("myDropdown").style.backgroundColor = "var(--main-white)"
        document.getElementById("header").style.backgroundColor = "var(--main-dark-grey)"
        document.getElementsByTagName("footer")[0].style.backgroundColor = "var(--main-dark-grey)"
        document.getElementById("content").style.color = "#000"
        document.getElementsByClassName("menu-item")[1].style.border = "#888 solid 3px"
        document.getElementsByClassName("menu-item")[0].style.border = "none"
        document.getElementById("credits").style.color = "#000"
        document.documentElement.style.setProperty('--link-color', 'var(--main-orange)')
    }
    if (mobileView) {
        document.getElementById("options").innerHTML = ``
    }
    else {
        document.getElementById("options").innerHTML = `            
            <li><a onclick="home()">Home</a></li>
            <li><a onclick="mission()">Our mission</a></li>
            <li><a onclick="docs()">Documentation</a></li>`
    }
}

function toggleBackground() {
    if (document.cookie.trim().startsWith("background: 0")) {
        document.cookie = "background: 1;"
    }
    else {
        document.cookie = "background: 0;"
    }
    update();
    close()
}

update()



addEventListener("resize", (event) => { 
    console.log(window.innerWidth)

    if (window.innerWidth  <= 700) {
        mobileView = true
    }
    else {
        mobileView = false
    }
    console.log(mobileView)
    update()
})