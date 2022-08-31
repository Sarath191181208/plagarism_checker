let toTopBtn = document.getElementById("scroll-to-top-btn");
let toggleViewBtn = $("#toggle-view-btn");
// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 60) {
        toTopBtn.style.opacity = 1;
        toggleViewBtn.css("opacity", 1);
    } else {
        toTopBtn.style.opacity = 0;
        toggleViewBtn.css("opacity", 0);
    }
}

// When the user clicks on the button, scroll to the top of the document
function toTopFn() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}