function toggleDarkMode(){
    if (document.body.classList.contains('dark')) {
        document.body.classList.remove('dark');

        document.body.style.backgroundColor = 'var(--main-color-dark)';
        let elems=document.getElementsByClassName("box");
        for (let i=0;i<elems.length;i+=1){
            elems[i].style.backgroundColor = 'var(--secondary-color-dark)';
            elems[i].style.color = 'var(--text-color-light)';
        }
        document.getElementById("nav-menu-content-inner").style.backgroundColor = 'var(--secondary-color-dark)';
        let nav_items=document.getElementById("nav-menu-content-inner").children;
        for (let i=0;i<nav_items.length;i+=1){
            nav_items[i].style.color = 'var(--text-color-light)';
            nav_items[i].style.backgroundColor = 'var(--tertiary-color-dark)';
        }
        document.body.style.color='var(--text-color-light)';
    }
    else{
        document.body.classList.add('dark');

        document.body.style.backgroundColor = 'var(--main-color)';
        let elems=document.getElementsByClassName("box");
        for (let i=0;i<elems.length;i+=1){
            elems[i].style.backgroundColor = 'var(--secondary-color)';
            elems[i].style.color = 'var(--text-color-dark)';
        }
        document.getElementById("nav-menu-content-inner").style.backgroundColor = 'var(--secondary-color)';
        let nav_items=document.getElementById("nav-menu-content-inner").children;
        for (let i=0;i<nav_items.length;i+=1){
            nav_items[i].style.color = 'var(--text-color-dark)';
            nav_items[i].style.backgroundColor = 'var(--tertiary-color)';
        }
        document.body.style.color='var(--text-color-dark)';
    }
}
document.addEventListener('DOMContentLoaded', ()=>{toggleDarkMode();});



//const asdfjkl=()=>{const url = 'https://api.openai.com/v1/completions';const headers = {'Content-Type': 'application/json', Authorization: 'Bearer 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',};const body = {model: 'text-davinci-003', prompt: 'Say this is a test', temperature: 0.5, max_tokens: 100,};fetch(url, {method: 'POST', headers: headers, body: JSON.stringify(body),}).then((response) => response.json()).then((data) => console.log(data['choices'][0]['text']));}