document.addEventListener('DOMContentLoaded', () => {
    const teamMembers = document.querySelectorAll('.team-member');
    const imageDisplay = document.getElementById('image-display');
    const teamImageContainer = document.getElementById('team-image');
    const closeImageContainer = document.querySelector('.close-btn');
    const BackImageContainer = document.querySelector('.wrapper-image');

    teamMembers.forEach(member => {
        member.addEventListener('click', () => {
            const imageUrl = member.getAttribute('data-image');
            imageDisplay.src = imageUrl;
            console.log(imageDisplay);
            BackImageContainer.style.display = 'flex'; // Show the image container
        });
    });

    closeImageContainer.addEventListener('click', () => {
        BackImageContainer.style.display = 'none'; // Hide the image container
    });
});