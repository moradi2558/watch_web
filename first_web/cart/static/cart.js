let minusIcons = document.querySelectorAll(".fa-minus")

minusIcons.forEach(function (minus) {
    let Qty = minus.parentElement.nextElementSibling.firstElementChild.innerHTML;
    if(Qty == 1){
        minus.classList.remove("fa-minus")
        minus.classList.add("fa-trash")
        minus.classList.add("text-danger")
        minus.style.fontSize = "medium"
    }
})


let $ = document

const continu = $.querySelector('.continue')
const modalParent = $.querySelector('.modal-parent')
const x = $.querySelector('.X')
const sectionElem = $.querySelector('.section')

console.log(window.innerWidth)

function showModal() {
    modalParent.style.display = 'block'
    sectionElem.style.filter = 'blur(10px)'
    window.addEventListener("resize",function(){
        if (window.innerWidth > 767) {
            sectionElem.style.filter = 'blur(0px)'
        }else{
            if (modalParent.style.display == 'block') {   
                sectionElem.style.filter = 'blur(10px)'
            }
        }
    })
}

function hideModalWithX() {
    modalParent.style.display = 'none'
    sectionElem.style.filter = 'blur(0px)'
}

function hideModalWithEsc(event) {
    if (event.keyCode === 27) {
        modalParent.style.display = 'none'
        sectionElem.style.filter = 'blur(0px)'
    }
}

continu.addEventListener('click', showModal)
x.addEventListener('click', hideModalWithX)
document.body.addEventListener('keyup', hideModalWithEsc)