window.onload = function(){
    slideThree();
    slideFour();
}

let sliderThree = document.getElementById("slider-3");
let sliderFour = document.getElementById("slider-4");
let displayValThree = document.getElementById("range3");
let displayValFour = document.getElementById("range4");
let minGap2 = 0;
let sliderTrack2 = document.querySelector(".slider-track2");
let sliderMaxValue2 = document.getElementById("slider-3").max;

function slideThree(){
    if(parseInt(sliderFour.value) - parseInt(sliderThree.value) <= minGap2){
        sliderThree.value = parseInt(sliderFour.value) - minGap2;
    }
    displayValThree.textContent = sliderThree.value;
    fillColor2();
}
function slideFour(){
    if(parseInt(sliderFour.value) - parseInt(sliderThree.value) <= minGap2){
        sliderFour.value = parseInt(sliderThree.value) + minGap2;
    }
    displayValFour.textContent = sliderFour.value;
    fillColor2();
}
function fillColor2(){
    percent3 = (sliderThree.value / sliderMaxValue2) * 100;
    percent4 = (sliderFour.value / sliderMaxValue2) * 100;
     sliderTrack2.style.background = `linear-gradient(to right, #dadae5 ${percent3}% , #000000 ${percent3}% , #000000 ${percent4}%, #dadae5 ${percent4}%)`;
}

let inputSearchs = document.querySelectorAll("#id_search")
inputSearchs.forEach(function(inputSearch){
inputSearch.setAttribute("placeholder","Search...")
})