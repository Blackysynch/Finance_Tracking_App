// Get the form element
const form = document.getElementById('profilepageform');

// Add an event listener to the form's submit event
form.addEventListener('submit', (e) => {
    // Prevent the default form submission behavior
    e.preventDefault();

    // Get the input fields
    const name = document.getElementById('name');
    const email = document.getElementById('email');
    const telephone = document.getElementById('telephone');
    const location = document.getElementById('location');
    const country = document.getElementById('country');
    const budgetmonthly = document.getElementById('budgetmonthly');
    const sourceOfIncome = document.getElementById('source_of_income');
    const otherSources = document.getElementById('other_sources');

    // Validate the input fields
    if (name.value.trim() === '') {
        alert('Please enter your name');
        name.focus();
        return;
    }

    if (email.value.trim() === '') {
        alert('Please enter your email');
        email.focus();
        return;
    }

    if (telephone.value.trim() === '') {
        alert('Please enter your phone number');
        telephone.focus();
        return;
    }

    if (location.value.trim() === '') {
        alert('Please enter your location');
        location.focus();
        return;
    }

    if (country.value.trim() === '') {
        alert('Please enter your country');
        country.focus();
        return;
    }

    // Create a FormData object to store the form data
    const formData = new FormData();
    formData.append('name', name.value);
    formData.append('email', email.value);
    formData.append('telephone', telephone.value);
    formData.append('location', location.value);
    formData.append('country', country.value);
    formData.append('budgetmonthly', budgetmonthly.value);
    formData.append('source_of_income', sourceOfIncome.value);
    formData.append('other_sources', otherSources.value);

    // Send the form data to the server using AJAX
    fetch('/profilepage/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});