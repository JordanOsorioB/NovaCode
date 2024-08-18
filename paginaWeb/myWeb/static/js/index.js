//const cardWidth = document.querySelector('.proyecto-card').offsetWidth;
//document.querySelector('.proyectos-next').addEventListener('click', function () {
//    document.querySelector('.proyectos-slider').scrollBy({
//        left: cardWidth,
//        behavior: 'smooth'
//    });
//});
//
//document.querySelector('.proyectos-prev').addEventListener('click', function () {
//    document.querySelector('.proyectos-slider').scrollBy({
//        left: -cardWidth,
//        behavior: 'smooth'
//    });
//});

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const requiredFields = ['nombre_contacto', 'apellidos_contacto', 'email', 'telefono'];

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevenir el envío por defecto
        
        let allFieldsFilled = true;
        
        // Validar que todos los campos requeridos estén llenos
        requiredFields.forEach(function(field) {
            const inputField = document.getElementById('id_' + field);
            const errorDiv = inputField.parentElement.querySelector('.text-danger');
            
            if (inputField.value.trim() === '') {
                allFieldsFilled = false;
                if (!errorDiv) {
                    const errorElement = document.createElement('div');
                    errorElement.classList.add('text-danger');
                    errorElement.textContent = 'Este campo es obligatorio.';
                    inputField.parentElement.appendChild(errorElement);
                }
            } else {
                if (errorDiv) {
                    errorDiv.remove();
                }
            }
        });

        // Si todos los campos están llenos, permitir el envío del formulario
        if (allFieldsFilled) {
            form.submit(); // Procede a enviar el formulario al backend
        }
    });
});


document.addEventListener('DOMContentLoaded', function () {
    let carouselItems = document.querySelectorAll('.carousel-item');

    carouselItems.forEach((item, index) => {
        if (index === 0 || index === 1) {
            item.classList.add('active');
        }
    });
    
    const carousel = document.querySelector('#projectCarousel');
    carousel.addEventListener('slide.bs.carousel', function (e) {
        let items = carousel.querySelectorAll('.carousel-item');
        items.forEach((item, index) => {
            if (index !== e.to) {
                item.classList.remove('active');
            }
        });
    });
});
