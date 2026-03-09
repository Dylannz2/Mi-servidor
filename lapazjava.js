let index = 0;

const slides = document.querySelectorAll(".slide");
const slider = document.getElementById("slider");

function showSlide() {

    index++;

    if(index >= slides.length){
        index = 0;
    }

    slider.style.transform = "translateX(" + (-index * 100) + "%)";
}

setInterval(showSlide, 5000);