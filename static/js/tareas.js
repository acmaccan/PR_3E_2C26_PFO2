function logout() {
    if (confirm('¿Estás seguro de que querés cerrar sesión?')) {
        window.location.href = '/login';
    }
}
