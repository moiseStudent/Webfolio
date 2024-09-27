// JavaScript para animaciones
document.addEventListener('DOMContentLoaded', function () {
const fadeElements = document.querySelectorAll('.fade-in');

function checkFade() {
    fadeElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementBottom = element.getBoundingClientRect().bottom;

        if (elementTop < window.innerHeight && elementBottom > 0) {
            element.classList.add('visible');
        }
    });
}

// Verificar en la carga inicial
checkFade();

// Verificar al hacer scroll
window.addEventListener('scroll', checkFade);

// Animación de hover para los elementos info-item
const infoItems = document.querySelectorAll('.info-item');
infoItems.forEach(item => {
    item.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
    });
    item.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
    });
 });
});