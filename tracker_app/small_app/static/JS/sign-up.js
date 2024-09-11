/*
function extractFormData(){
    let nameInput = document.getElementById('uname');
    let emailInput = document.getElementById('email');
    let passwordInput = document.getElementById('password');

    let name = nameInput.value;
    let email = emailInput.value;
    let password = passwordInput.value;

    const formData = new URLSearchParams();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('password', 'password');

    fetch('/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: formData.toString()
    })
    .then(response => Response.text())
    .then(data => {
            console.log(data); //Handle response from dj
    })
    .catch(error => {
        console.error('Error: ', error);
    });

    return false
}

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
*/

function getCookie(name) {  
    let cookieValue = null;  
    if (document.cookie && document.cookie !== '') {  
        const cookies = document.cookie.split(';');  
        for (let i = 0; i < cookies.length; i++) {  
            const cookie = cookies[i].trim();  
            // Check if this cookie string begins with the name we want  
            if (cookie.startsWith(name + '=')) {  
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));  
                break;  
            }  
        }  
    }  
    return cookieValue;  
}  

function extractFormData() {  
    let nameInput = document.getElementById('uname');  
    let emailInput = document.getElementById('email');  
    let passwordInput = document.getElementById('password');  

    let name = nameInput.value;  
    let email = emailInput.value;  
    let password = passwordInput.value;  

    const formData = new URLSearchParams();  
    formData.append('uname', name);  
    formData.append('email', email);  
    formData.append('password', password);  

    fetch('/signup/', { // Ensure your endpoint matches your Django URL pattern  
        method: 'POST',  
        headers: {  
            'Content-Type': 'application/x-www-form-urlencoded',  
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token  
        },  
        body: formData.toString(),  
    })  
    .then(response => response.json()) // Expecting JSON response  
    .then(data => {  
        console.log(data); // Handle response from server  
        if (data.error) {  
            alert(data.error); // Alert error message from server  
        } else {  
            alert(data.message); // Alert success message  
            setTimeout(() => {  
                window.location.href = '/login/'; // Redirect to login after success  
            }, 1000);  
        }  
    })  
    .catch(error => {  
        console.error('Error: ', error);  
        alert('An unexpected error occurred. Please try again.'); // General error alert  
    });  

    return false; // Prevent any default form submission  
}  

document.addEventListener('DOMContentLoaded', function() {  
    const passwordField = document.getElementById('password');  
    const showPasswordCheckbox = document.getElementById('show-password');  
    const registerButton = document.querySelector('button[type="submit"]');  

    // Toggle password visibility  
    showPasswordCheckbox.addEventListener('change', function() {  
        passwordField.type = showPasswordCheckbox.checked ? 'text' : 'password';  
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
            alert("Please enter a valid email address.");  
            return; // Exit the function if the email is invalid  
        }  

        // If validation is successful, call extractFormData to handle form submission  
        extractFormData();  
    });  

    // Function to check if the email is valid  
    function isValidEmail(email) {  
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex  
        return regex.test(email);  
    }  
});