document.addEventListener('DOMContentLoaded', function() {
    const passwordField = document.getElementById('password');
    const showPasswordCheckbox = document.getElementById('show-password');

    showPasswordCheckbox.addEventListener('change', function() {
        if (showPasswordCheckbox.checked) {
            passwordField.type = "text"; // Show password
        } else {
            passwordField.type = 'password'; // Hide password
        }
    });
});