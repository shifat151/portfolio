document.addEventListener("DOMContentLoaded", function(event) {
    if( navigator.userAgent.match(/Android/i)
 || navigator.userAgent.match(/webOS/i)
 || navigator.userAgent.match(/iPhone/i)
 || navigator.userAgent.match(/iPad/i)
 || navigator.userAgent.match(/iPod/i)
 || navigator.userAgent.match(/BlackBerry/i)
 || navigator.userAgent.match(/Windows Phone/i)){
    document.getElementById('pdf').style.display="none"
 }

 else{
     document.getElementById('pdf-notice').style.display="none"
 }


});