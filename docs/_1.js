function toggleDarkMode(){
    if (document.body.classList.contains('dark')) {
        document.body.classList.remove('dark');

        document.body.style.backgroundColor = 'var(--main-color-dark)';
        let elems=document.getElementsByClassName("box");
        for (let i=0;i<elems.length;i+=1){
            elems[i].style.backgroundColor = 'var(--secondary-color-dark)';
            elems[i].style.color = 'var(--text-color-light)';
        }
    }
    else{
        document.body.classList.add('dark');

        document.body.style.backgroundColor = 'var(--main-color)';
        let elems=document.getElementsByClassName("box");
        for (let i=0;i<elems.length;i+=1){
            elems[i].style.backgroundColor = 'var(--secondary-color)';
            elems[i].style.color = 'var(--text-color-dark)';
        }
    }
}
document.addEventListener('DOMContentLoaded', ()=>{toggleDarkMode();});

async function makeGetRequest(url){
    try{
        const response = await fetch(url);
        const text=await response.json();
        console.log(text);
        return text;
    } catch (error){
        console.log(error);
    }
}
function _makeGetRequest(url){
    return makeGetRequest(url).then((text)=>{
        return text;
    });
}