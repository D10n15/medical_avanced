document.addEventListener("DOMContentLoaded", function () {
    const appointmentForm = document.querySelector("#appointment-form");
    const submitButton = document.querySelector("#submit-btn");
    const notification = document.createElement("div");
    
    notification.classList.add("notification");
    document.body.appendChild(notification);
    
    // Efecto de apertura del formulario
    if (appointmentForm) {
        appointmentForm.style.opacity = 0;
        appointmentForm.style.transform = "scale(0.9)";
        setTimeout(() => {
            appointmentForm.style.opacity = 1;
            appointmentForm.style.transform = "scale(1)";
            appointmentForm.style.transition = "all 0.3s ease-in-out";
        }, 100);
    }
    
    // Efecto en botón
    submitButton.addEventListener("mouseenter", () => {
        submitButton.style.transform = "scale(1.1)";
        submitButton.style.transition = "transform 0.2s";
    });
    
    submitButton.addEventListener("mouseleave", () => {
        submitButton.style.transform = "scale(1)";
    });
    
    // Notificación al enviar
    appointmentForm.addEventListener("submit", function (e) {
        e.preventDefault();
        showNotification("✅ Cita agendada correctamente!");
    });
    
    function showNotification(message) {
        notification.textContent = message;
        notification.style.opacity = 1;
        notification.style.top = "20px";
        setTimeout(() => {
            notification.style.opacity = 0;
            notification.style.top = "0";
        }, 3000);
    }
    
});
