let menuOpen = false

if (document.cookie == "") {
document.cookie = "background: 0;"
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

function update() {
    if (document.cookie.trim().startsWith("background: 1")) {
        document.body.style.backgroundColor = "#333"
        document.getElementById("content").style.color = "#fff"
    }
    else {
        document.body.style.backgroundColor = "#fff"
        document.getElementById("content").style.color = "#000"
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
}

update()