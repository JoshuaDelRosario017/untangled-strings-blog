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

const spinnerBox = document.getElementById('spinner-box')
const dataBox = document.getElementById('data-box')

// $.ajax({
//    type: 'GET',
//    url: '{% url "uintangled"%}',
//    success: function(res) {
//       setTimeout(()=>{
//          spinnerBox.classList.add('spinner-not-visible')
//          console.log("success")
//          dataBox.innerHTML += `{% block content %} {% endblock %}`
//       }, 500)
      
//    },
//    error: function(er) {
//       console.log("error")
//    },
// })


  




//Reload page when clicking browsers back button
// var perfEntries = performance.getEntriesByType("navigation");

//     if (perfEntries[0].type === "back_forward") {
//         location.reload(true);
//     }

//Masonry



