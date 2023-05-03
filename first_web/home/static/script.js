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
  console.log();
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
