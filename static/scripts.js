document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('menuIcon');
    const menu = document.getElementById('menu');

    menuIcon.addEventListener('click', function() {
        if (menu.style.display === 'block') {
            menu.style.display = 'none';
        } else {
            menu.style.display = 'block';
        }
    });

    // Optional: Close the menu when clicking outside of it
    document.addEventListener('click', function(event) {
        if (!menu.contains(event.target) && event.target !== menuIcon) {
            menu.style.display = 'none';
        }
    });
});
