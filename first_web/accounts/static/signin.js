let passwordInput = document.querySelector("#id_password_1")
passwordInput.insertAdjacentHTML("afterend", `<p style="height:20px;display:none;font-size:.9rem" class="m-0 text-danger fw-normal opacity-100" id="text-err"><i class="fa-solid fa-circle-info fa-beat-fade" style="--fa-beat-fade-opacity: 0.67; --fa-beat-fade-scale: 1.075;" ></i> Password must be more than 8 characters</p>`)
let textErr = document.querySelector("#text-err")
let signinBtn = document.querySelector("#signin")
passwordInput.addEventListener("input",function(){
    if (passwordInput.value.length < 8) {
        textErr.style.display = "block"
        signinBtn.classList.add("disabled")
    }else{
        textErr.style.display = "none"
        signinBtn.classList.remove("disabled")
    }
})