document.addEventListener('DOMContentLoaded', function() {
    const passwordField = document.getElementById('password');
    const showPasswordCheckbox = document.getElementById('show-password');
    const registerButton = document.querySelector('button[type="submit"]'); // Select the register button
    const form = document.querySelector('form');

    // Show/Hide Password Functionality
    showPasswordCheckbox.addEventListener('change', function() {
        if (showPasswordCheckbox.checked) {
            passwordField.type = "text"; // Show password
        } else {
            passwordField.type = 'password'; // Hide password
        }
    });

    // Register Button Validation
    registerButton.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent the form from submitting immediately

        const username = document.getElementById('uname').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();
        // Simple validation
        if (username === "" || email === "" || password === "") {
            alert("Please fill in all fields.");
        } else {
            form.submit(); // Submit the form if all fields are filled
        }
    });
});

