// JavaScript para funcionalidades adicionales
document.addEventListener('DOMContentLoaded', function() {
    // Tooltip de Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Animación de contador para precios (efecto decorativo)
    const priceElements = document.querySelectorAll('.price-tag');
    priceElements.forEach(element => {
        const finalValue = parseFloat(element.textContent.replace('$', ''));
        let currentValue = 0;
        const duration = 2000; // 2 segundos
        const steps = 50;
        const increment = finalValue / steps;
        const stepTime = duration / steps;

        const timer = setInterval(() => {
            currentValue += increment;
            if (currentValue >= finalValue) {
                currentValue = finalValue;
                clearInterval(timer);
            }
            element.textContent = `$${Math.round(currentValue)}`;
        }, stepTime);
    });

    // Validación básica del formulario
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            let isValid = true;
            const inputs = this.querySelectorAll('input[required], textarea[required], select[required]');

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('is-invalid');
                } else {
                    input.classList.remove('is-invalid');
                }
            });

            if (!isValid) {
                event.preventDefault();
                event.stopPropagation();

                // Mostrar alerta de error
                const alertDiv = document.createElement('div');
                alertDiv.className = 'alert alert-danger alert-dismissible fade show mt-3';
                alertDiv.innerHTML = `
                    Por favor, completa todos los campos obligatorios.
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                `;
                this.appendChild(alertDiv);
            }
        });
    }

    // Efecto parallax para el hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            heroSection.style.backgroundPosition = 'center ' + rate + 'px';
        });
    }
});