document.addEventListener('DOMContentLoaded', function() {  
    const passwordField = document.getElementById('password');  
    const showPasswordCheckbox = document.getElementById('show-password');  
    const registerButton = document.querySelector('button[type="submit"]'); // Select the register button  
    const form = document.querySelector('form');  

    // Toggle password visibility  
    showPasswordCheckbox.addEventListener('change', function() {  
        passwordField.type = showPasswordCheckbox.checked ? 'text' : 'password'; // Show or hide password  
    });  

    // Validate form fields before submission  
    registerButton.addEventListener('click', function(event) {  
        event.preventDefault(); // Prevent immediate form submission  
        
        const username = document.getElementById('uname').value.trim();  
        const email = document.getElementById('email').value.trim();  
        const password = document.getElementById('password').value.trim();  

        // Simple validation for empty fields  
        if (username === "" || email === "" || password === "") {  
            alert("Please fill in all fields.");  
            return; // Exit the function early if any field is empty  
        }  

        // Validate email  
        if (!isValidEmail(email)) {  
            alert("Please enter a valid email address, including '@'.");  
            return; // Exit the function if the email is invalid  
        }  

        form.submit(); // Submit the form if all fields are valid  
    });  

    // Function to check if the email is valid  
    function isValidEmail(email) {  
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex  
        return regex.test(email);  
    }  
});