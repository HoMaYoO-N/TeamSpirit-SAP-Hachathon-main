function checkout() {
    console.log("checkout:", document.getElementById("BtnCheckout") )
    
    document.getElementById("BtnCheckout").style.display = 'none';
    document.getElementById("BtnCheckin").style.display = 'inline';
}

function checkin() {
    console.log("checkin")
    document.getElementById("BtnCheckout").style.display = 'inline';
    document.getElementById("BtnCheckin").style.display = 'none';
}