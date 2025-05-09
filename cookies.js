if (document.cookie == "") {
document.cookie = "background: 0;"
}

function update() {
    if (document.cookie.trim().startsWith("background: 1")) {
        document.body.style.backgroundColor = "#000"
    }
    else {
        document.body.style.backgroundColor = "#fff"

    }
}

function toggleBackground() {
    if (document.cookie.trim().startsWith("background: 0")) {
        document.cookie = "background: 1;"
    }
    else {
        document.cookie = "background: 0;"
    }
    update()
console.log(document.cookie)

}

update()

console.log(document.cookie)