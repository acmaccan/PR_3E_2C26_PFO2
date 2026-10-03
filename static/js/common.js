function togglePassword(fieldId) {
    const input = document.getElementById(fieldId);
    const btn = event.target;

    if (input.type === 'password') {
        input.type = 'text';
        btn.textContent = 'OCULTAR';
    } else {
        input.type = 'password';
        btn.textContent = 'VER';
    }
}

function clearErrors(errorIds) {
    errorIds.forEach(id => {
        const errorEl = document.getElementById(id);
        if (errorEl) {
            errorEl.classList.remove('show');
        }
    });
}

function showError(fieldId, message) {
    const errorEl = document.getElementById(fieldId + 'Error');
    if (errorEl) {
        errorEl.textContent = message;
        errorEl.classList.add('show');
    }
}
