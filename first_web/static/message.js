let remove = document.querySelector(".fa-remove")
remove.addEventListener("click",function(e){
e.target.parentElement.parentElement.parentElement.remove()
})