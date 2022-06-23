const btnScrollToTop = document.querySelector('.btnScrollToTop')
const navToggle = document.querySelector('.nav-toggle')
const navLinks = document.querySelectorAll('.nav__link')
const btnNext = document.getElementById('portfolio__button--next')
const btnPrev = document.getElementById('portfolio__button--prev')

btnScrollToTop.addEventListener('click', () => {
    window.scrollTo(0, 0);
});

navToggle.addEventListener('click', () => {
	document.body.classList.toggle('nav-open');
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
    });
});

window.addEventListener('scroll', () => {
    if (pageYOffset >= 200) {
        document.querySelector('.btnScrollToTop').style.visibility = 'visible';
    } else {
        document.querySelector('.btnScrollToTop').style.visibility = 'hidden';
    }
})

let slidePosition = 0;
const slides = document.querySelectorAll('.portfolio__item');
const totalSlides = slides.length;

btnNext.addEventListener("click", () => {
    moveToNextSlide();
})

btnPrev.addEventListener("click", () => {
    moveToPrevSlide();
})

function updateSlidePosition() {
    for (let slide of slides) {
        slide.classList.remove('portfolio__item--visible');
        slide.classList.add('portfolio__item--hidden');
    }

    slides[slidePosition].classList.add('portfolio__item--visible')
}

function moveToNextSlide() {

    if (slidePosition === totalSlides - 1) {
        slidePosition = 0;
    } else {
        slidePosition++;
    }

    updateSlidePosition();
}

function moveToPrevSlide() {

    if (slidePosition === 0) {
        slidePosition = totalSlides - 1;
    } else {
        slidePosition--;
    }

    updateSlidePosition();
}

