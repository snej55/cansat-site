function credits() {

    item.innerHTML = `<h1>Credits</h1><br>

    <h3>Logo Design:</h3>
    Nick Zyuzin <br>
    Sebastian Thornton <br><br>

    <h3>Website:</h3>
    Jan Lukasiak <br>
    Jens kromdijk <br>
    Dylan Greenwood <br>
    Sebastian Thornton <br><br>

    <h3>Prototyping:</h3>
    Nathan yin <br>
    Dylan greenwood <br><br>
    
    <h3> code for satelite:</h3>
    Nathan yin <br>
    Jens kromdijk <br>
    Jan Lukasiak <br><br>

    <h3>3d modeling and printing:</h3>
    Nathan yin <br>
    Dylan greenwood <br>
`
    if (!mobileView) {
        document.getElementById("credits").innerHTML = "Home";
        document.getElementById("credits").setAttribute( "onClick", "javascript: home();" );
    }
    menuOpen = false;
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
    credit = true
    close()
}