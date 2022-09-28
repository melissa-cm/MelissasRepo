const btn = document.getElementById("btn");
const nav = document.getElementById("nav");

btn.addEventListener("click", () =>{
    nav.classList.toggle("active");
    btn.classList.toggle("active");
});

const text = document.querySelector('.myname');
//console.log(text)
const strText = text.textContent;
//console.log(strText);
const splitText = strText.split("");
//console.log(splitText);
text.textContent = "";

for(let i=0 ; i < splitText.length; i++ ){
    text.innerHTML += "<span>"+ splitText[i] + "</span>";
 }

 let char = 0;
 let timer = setInterval(onTick, 50);

 function onTick(){
    const span = text.querySelectorAll("span")[char];
    span.classList.add("fade");
    char++
    if(char === splitText.length){
        complete();
        return;
    }
 }

 function complete(){
    clearInterval(timer);
    timer = null;
 }


 let mybutton = document.getElementById("myBtn");

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}