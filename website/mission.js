function mission() {
    item.innerHTML = `<h1>Our Mission</h1>
    <br><br>
    CastAway is the team behind the CastAway satelite, our skybreaking attempt to prove that 
    the sky is indeed the limit. Consisting of six multitalented junior individuals, we have 
    designed a satelite to conduct various science experiments, while still meeting the design 
    criteria set by ESERO. The satelite is set to perform the following science experiments:
    <br><br>
    <ul>
        <li>Measure the air pressure in various points of the atmosphere, and attempt to infer 
        altitude from it.</li>
        <li>Measure the temperature of the air at various points of the atmosphere.</li>
        <li>Measure the quantity of different gases at various points of the atmosphere.</li>
        <li>Measure the light intensity for both visible and ultraviolet light that the satelite 
        experiences at different points of the atmosphere.</li>
        <li>Measure the strength and direction of Earth's magnetic field.</li>
        <li>Measure the direction and magnetude of orientation, rotation and direction of the 
        satelite.</li>
        <li>Measure the GPS position of the satelite relative to Earth in three dimensions.</li>
        <li>Take pretty pictures!</li>
    </ul>
    <br>
    We need to have a near-constant steam of data sent to us over radio, and be able to recover 
    the satelite in a state where we can recover more data, and use it again.<br>

    Another one of our objectives is to raise public awareness about our project, which we 
    are trying to achieve by:
    <ul>
        <li>Making this website.</li>
        <li>Giving presentations to the local education community.</li>
        <li>Making flyers.</li>
        <li>Gaining local media coverage.</li>
    </ul>
`
    if (!mobileView) {
        document.getElementById("credits").innerHTML = "Credits";
        document.getElementById("credits").setAttribute( "onClick", "javascript: credits();" );
    }
    menuOpen = false;
    document.getElementById("myDropdown").style.display = "none";
    scroll(0, 0);
    credit = false
    close()
}