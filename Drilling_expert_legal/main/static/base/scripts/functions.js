

const activePage = window.location.pathname;
document.querySelectorAll('nav a').forEach(link => {
    if(link.href.includes(`${activePage}`)){
        link.classList.add('active')
    };
});

// When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  console.log(document.getElementById("navbar").offsetHeight);
  if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {

    document.getElementById("navbar").style.padding = "0px 80px";
    //document.getElementById("logo").style.fontSize = "25px";
  } else {
    document.getElementById("navbar").style.padding = "12px 80px";
    // document.getElementById("logo").style.fontSize = "35px";
  }
}

