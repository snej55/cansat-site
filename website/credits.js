function credits() {

    item.innerHTML = `<h1>Credits</h1>

    <h3>landing gear design:</h3>
    Dylan greenwood <br>
    Nathan yin <br><br>

   <h3>logo design:</h3>
    Nick zyuzin <br>
    Sebastian thornton <br><br>

   <h3>web design:</h3>
    Jan Lukasiak <br>
    Jens kromdijk <br>
    Dylan greenwood <br>
    Sebastian thornton <br><br>

   <h3> parachute design:</h3>
    Sebastian thornton <br>
    Dylan greenwood <br><br>

   <h3> prototyping:</h3>
    Dylan greenwood <br>
    Nathan yin <br><br>
    <br>
   <h3> code for satelite:</h3>
    Nathan yin <br>
    Jens kromdijk <br>
    Jan Lukasiak <br>
    <br>
    <h3>testing:</h3>
    Dylan greenwood <br>
    Sebastian thornton<br>
    <br>
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