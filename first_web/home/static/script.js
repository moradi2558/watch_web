let likes = document.querySelectorAll(".heart");
let btnReplys = document.querySelectorAll(".btn-reply");
let replys = document.querySelectorAll(".replys");
let showMore = document.querySelectorAll(".show-more");
let isliked = false;
likes.forEach(function (like) {
  like.addEventListener("click", function (e) {
    if (isliked) {
      isliked = false;
      e.target.classList.remove("red");
      e.target.classList.add("white");
    } else {
      isliked = true;
      e.target.classList.remove("white");
      e.target.classList.add("red");
    }
  });
});

let reply = false;
btnReplys.forEach(function (btnReply) {
  btnReply.addEventListener("click", function (e) {
    if (reply) {
      reply = false;
      e.target.parentElement.nextElementSibling.nextElementSibling.style.display =
        "none";
    } else {
      reply = true;
      e.target.parentElement.nextElementSibling.nextElementSibling.style.display =
        "block";
    }
  });
});
replys.forEach(function (reply) {
  if (reply.firstElementChild.childElementCount == 0) {
    reply.classList.remove("mt-5", "mb-3");
    reply.lastElementChild.style.display = "none";
  } else if (reply.firstElementChild.childElementCount == 1) {
    reply.lastElementChild.style.display = "none";
    reply.firstElementChild.firstElementChild.style.display = "block";
  } else {
    reply.classList.add("mt-5", "mb-3");
    reply.lastElementChild.style.display = "block";
    reply.firstElementChild.firstElementChild.style.display = "block";
    let isClickMore = false;
    showMore.forEach(function (show) {
      show.addEventListener("click", function (e) {
        let reps = e.target.parentElement.firstElementChild.childNodes;
        if (isClickMore) {
          isClickMore = false;
          show.classList.remove("fa-minus");
          show.classList.add("fa-plus");
          reps.forEach(function (rep) {
            if (rep.style !== undefined) {
              rep.style.display = "none";
            }
          });
           reps[1].style.display = "block"
        } else {
          isClickMore = true;
          show.classList.remove("fa-plus");
          show.classList.add("fa-minus");
          reps.forEach(function (rep) {
            if (rep.style !== undefined) {
              rep.style.display = "block";
            }
          });
        }
      });
    });
  }
});

let mainImg = document.querySelector(".main-img")
let images = document.querySelectorAll(".images")
let next = document.querySelector(".next")
let prev = document.querySelector(".prev")
let srcArray = []
srcIndex = 0
images.forEach(function(img){
let imgSrc =  img.getAttribute("src")
srcArray.push(imgSrc)
img.addEventListener("click",function(e){

   srcIndex = srcArray.findIndex(function(src){
     return src === e.target.getAttribute("src")
   })
 mainImg.setAttribute("src",e.target.getAttribute("src"))
})
})


function nextHandler(){
  if (srcIndex >= srcArray.length - 1) {
    srcIndex = 0
  } else {
    srcIndex++
  }
  mainImg.setAttribute("src",srcArray[srcIndex])
}
function prevHandler(){
  if (srcIndex <= 0) {
    srcIndex = srcArray.length-1
  } else {
    srcIndex--
  }
  mainImg.setAttribute("src",srcArray[srcIndex])
}



next.addEventListener("click",nextHandler)
prev.addEventListener("click",prevHandler)


let btnsCheck = document.querySelectorAll(".btn-check")
let labels = document.querySelectorAll(".label")
let i = 0

btnsCheck.forEach(function(btnCheck){
  btnCheck.nextElementSibling.setAttribute("for", `btnradio${i+1}`)
  btnCheck.nextElementSibling.style.backgroundColor = btnCheck.nextElementSibling.innerHTML
  btnCheck.nextElementSibling.style.width = "2rem"
  btnCheck.nextElementSibling.style.height = "2rem"
  btnCheck.nextElementSibling.innerHTML = ""
  btnCheck.setAttribute("id",`btnradio${i+1}`);
  i++;

  if (btnCheck.getAttribute("checked") != null) {
    btnCheck.nextElementSibling.insertAdjacentHTML("afterbegin",`<i class="fa fa-check text-white"></i>`)
  }
})

let piss = document.querySelectorAll(".piss")
piss.forEach(function(pis){
  if (pis) {
    pis.parentElement.parentElement.classList.add("bg-success")
  }
})

let dis = document.querySelectorAll(".dis")
dis.forEach(function(di){
  if (di) {
    di.parentElement.parentElement.classList.add("bg-danger")
  }
})
