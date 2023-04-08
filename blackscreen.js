// change the document background color to black when an element with class "black" is in viewport
function checkLDM(){
    const blackscreen = document.getElementsByClassName("black");
    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {document.body.style.backgroundColor = 'black';}
            else {document.body.style.backgroundColor = 'white';}});
    });
    for (let i=0;i<blackscreen.length;i+=1){observer.observe(blackscreen[i]);}
}


document.addEventListener('scroll', checkLDM);
document.addEventListener('DOMContentLoaded', checkLDM)