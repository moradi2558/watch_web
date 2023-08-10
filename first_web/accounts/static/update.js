let allLabel = document.querySelectorAll("label")
allLabel.forEach(function(lable){
lable.innerHTML = lable.innerHTML.slice(0,lable.innerHTML.length-1)
})
let phone = document.querySelector("#id_phone_0")
phone.removeAttribute("size")
phone.insertAdjacentHTML("beforebegin",`<label for="id_phone_0">Phone</label>`)
let address = document.querySelector("#id_address")
address.insertAdjacentHTML("beforebegin",`<label for="id_address">Address</label>`)

let allp = document.querySelectorAll("p")
allp.forEach(function(p){
p.className = "col-8 col-md-8 col-lg-7"
})