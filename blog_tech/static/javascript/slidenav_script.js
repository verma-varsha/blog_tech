function openNav1() {
    document.getElementById("categorySidenav").style.width = "250px";
    document.getElementById("post").style.marginRight = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav1() {
    document.getElementById("categorySidenav").style.width = "0";
    document.getElementById("post").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}

function openNav2() {
    document.getElementById("recentSidenav").style.width = "250px";
    document.getElementById("post").style.marginRight = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav2() {
    document.getElementById("recentSidenav").style.width = "0";
    document.getElementById("post").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}

$(document).ready(function() {
    // This will fire when document is ready:
    $(window).resize(function() {
        // This will fire each time the window is resized:
        if($(window).width() <= 1024) {
            // if smaller or equal
            $('.post').addClass("mobile");
        } else {
            // if larger
            
        }
    }).resize(); // This will simulate a resize to trigger the initial run.
});