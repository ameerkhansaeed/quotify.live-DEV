// Get all page buttons
const pageButtons = document.querySelectorAll('.page');

// Add click event listeners to each button
pageButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Remove 'active' class from all buttons
    pageButtons.forEach(btn => btn.classList.remove('active'));

    // Add 'active' class to the clicked button
    button.classList.add('active');
  });
});

// Function to change the active page
function changePage(offset) {
  const activeButton = document.querySelector('.page.active');
  if (activeButton) {
    const currentIndex = Array.from(pageButtons).indexOf(activeButton);
    const newIndex = currentIndex + offset;

    // Check if the new index is within bounds
    if (newIndex >= 0 && newIndex < pageButtons.length) {
      // Remove 'active' class from the current active button
      activeButton.classList.remove('active');

      // Add 'active' class to the new active button
      pageButtons[newIndex].classList.add('active');
    }
  }
}