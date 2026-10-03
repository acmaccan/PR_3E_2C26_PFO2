const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        clearErrors(['usuario', 'contraseña']);

        const usuario = document.getElementById('usuario').value;
        const contraseña = document.getElementById('contraseña').value;

        try {
            const response = await fetch('/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ usuario, contraseña })
            });

            if (response.ok) {
                window.location.href = '/tareas';
            } else {
                showError('usuario', 'Usuario o contraseña incorrectos');
            }
        } catch (error) {
            showError('usuario', 'Error al conectar con el servidor');
        }
    });
}

const registerForm = document.getElementById('registerForm');
if (registerForm) {
    registerForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        clearErrors(['usuario', 'contraseña', 'confirmar']);

        const usuario = document.getElementById('usuario').value;
        const contraseña = document.getElementById('contraseña').value;
        const confirmar = document.getElementById('confirmar').value;

        let hasError = false;

        if (!usuario.trim()) {
            showError('usuario', 'El usuario no puede estar vacío');
            hasError = true;
        }

        if (!contraseña.trim()) {
            showError('contraseña', 'La contraseña no puede estar vacía');
            hasError = true;
        } else if (contraseña.length < 6) {
            showError('contraseña', 'Mínimo 6 caracteres');
            hasError = true;
        }

        if (contraseña !== confirmar) {
            showError('confirmar', 'Las contraseñas no coinciden');
            hasError = true;
        }

        if (hasError) return;

        try {
            const response = await fetch('/registro', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ usuario, contraseña })
            });

            if (response.ok) {
                alert('Cuenta creada correctamente');
                window.location.href = '/login';
            } else {
                const data = await response.json();
                showError('usuario', data.message || 'Error al crear la cuenta');
            }
        } catch (error) {
            showError('usuario', 'Error al conectar con el servidor');
        }
    });
}
