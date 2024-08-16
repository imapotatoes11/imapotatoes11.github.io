const msg1 = 'This page looks better in Dark Mode';
const msg2 = 'My projects';

const update = function() {
    var isDark = localStorage.getItem('isDark');
    var headButton = document.getElementById('head-button');
    if (isDark === 'true') {
        // alert('adjskflsadf')
        headButton.innerText = msg2;
    } else {
        // alert('bb')
        headButton.innerText = msg1;
    }
}

document.addEventListener('DOMContentLoaded', update)
document.addEventListener('click', update)

function headButtonClick() {
    var isDark = localStorage.getItem('isDark');
    if (isDark === 'true') {
        var projectsSection = document.getElementById('projects');
        if (projectsSection) {
            projectsSection.scrollIntoView({behavior: "smooth"});
        }
    } else {
        toggle();
    }
}