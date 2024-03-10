document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#sidebar-darkmode').addEventListener('click', function () {
        this.classList.add('rotate360');
        setTimeout(() => {
            this.classList.remove('rotate360');
        }, 350);
    });
});