const activePage = window.location.pathname;
document.querySelectorAll('nav a').forEach(link => {
    if(link.href.includes(`${activePage}`)){
        link.classList.add('active')
    };
});

hamburger = document.querySelector(".hamburger");
hamburger.onclick = function() {
  navbar = document.querySelector(".nav-bar");
  navbar.classList.toggle("active");
}

//const hamburger

// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
// window.onscroll = function() {scrollFunction()};

// function scrollFunction() {
//   console.log(document.getElementById("navbar").offsetHeight);
//   if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {

//     document.getElementById("navbar").style.padding = "0px";
//     //document.getElementById("logo").style.fontSize = "25px";
//   } else {
//     document.getElementById("navbar").style.padding = "20px";
//     // document.getElementById("logo").style.fontSize = "35px";
//   }
// }

