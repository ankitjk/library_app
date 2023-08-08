document.addEventListener('DOMContentLoaded', () => {
    // Add your JavaScript logic here
    const searchInput = document.getElementById('search-bar');
    const alphaButton = document.getElementById('btn-alpha');
    const lowToHighButton = document.getElementById('btn-low-to-high');
    const highToLowButton = document.getElementById('btn-high-to-low');

    // Add event listeners and implement the logic for filtering and displaying books

    // Event listener for search input
    searchInput.addEventListener('input', () => {
        const searchText = searchInput.value.trim();
        // Implement search functionality here
    });

    // Event listener for alphabetical sorting button
    alphaButton.addEventListener('click', () => {
        // Implement alphabetical sorting logic here
    });

    // Event listener for ratings low to high button
    lowToHighButton.addEventListener('click', () => {
        // Implement ratings low to high sorting logic here
    });

    // Event listener for ratings high to low button
    highToLowButton.addEventListener('click', () => {
        // Implement ratings high to low sorting logic here
    });
});
