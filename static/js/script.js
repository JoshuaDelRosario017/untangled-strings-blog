// for error log in validation
// var message_ele = document.getElementById("err_mess");

// setTimeout(function(){ 
//    message_ele.style.display = "none"; 
// }, 3000);


// Go to top btn
const toTop = document.querySelector(".gotopbtn");

window.addEventListener("scroll", () => {
   if(window.pageYOffset > 100) {
      toTop.classList.add("active");
   } else {
      toTop.classList.remove("active");
   } 
})

let input = document.getElementById("inputTags");
let listArr = [];
input.addEventListener('keyup', (e) => {
   if(e.keyCode === 13) {
      if(input.value != '') {
         let inValue = e.target.value;
         listArr.push(inValue.replace(/\s/g, ''));
         let newTagLi = '';
         listArr.forEach((element, index) => {
            newTagLi += `<span id="tagValue" class="tag text-dark"># ${element} <i class="fa fa-times ml-2 mr-2" onclick="ondelete(${index})"></i></span>`;
         });
         document.querySelector('.div-tags').innerHTML = newTagLi;
         input.value = '';
      } else {
         alert('Please input something');
      }
   }
})

function ondelete(index) {
   listArr.splice(index, 1);
   let newTagLi = '';
   listArr.forEach((element, index) => {
      newTagLi += `<span name="tags" class="tag text-dark"># ${element} <i class="fa fa-times ml-2 mr-2" onclick="ondelete(${index})"></i></span>`;
   });
   document.querySelector('.div-tags').innerHTML = newTagLi;

}





