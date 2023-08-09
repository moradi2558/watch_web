let allLabel = document.querySelectorAll("label")
allLabel.forEach(function(lable){
lable.innerHTML = lable.innerHTML.slice(0,lable.innerHTML.length-1)
})

let allp = document.querySelectorAll("p");
allp.forEach(function(p){
    p.insertAdjacentHTML("beforeend",`<i class="fas fa-eye"></i>`)
})

let allIcon = document.querySelectorAll(".fa-eye")
allIcon.forEach(function(icon){
let flagIcon = false
icon.addEventListener("click",function(e){
    if (flagIcon) {
        e.target.classList.add("fa-eye")
        e.target.classList.remove("fa-eye-slash")
        e.target.previousElementSibling.setAttribute("type","password")
        flagIcon = false
    } else {
        e.target.classList.add("fa-eye-slash")
        e.target.classList.remove("fa-eye")
        e.target.previousElementSibling.setAttribute("type","text")
        flagIcon = true
    }
})
})