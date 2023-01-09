// for error log in validation
var message_ele = document.getElementById("err_mess");

setTimeout(function(){ 
   message_ele.style.display = "none"; 
}, 3000);




// Go to top btn
const toTop = document.querySelector(".gotopbtn");

window.addEventListener("scroll", () => {
   if(window.pageYOffset > 100) {
      toTop.classList.add("active");
   } else {
      toTop.classList.remove("active");
   } 
})



//Reload page when clicking browsers back button
// var perfEntries = performance.getEntriesByType("navigation");

//     if (perfEntries[0].type === "back_forward") {
//         location.reload(true);
//     }

//Masonry



