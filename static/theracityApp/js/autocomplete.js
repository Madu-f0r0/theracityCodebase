// Get the input field and suggestions container
const input = document.getElementById('searchInput');
const suggestionsContainer = document.getElementById('suggestions');

// Add an event listener to detect changes in the input field
input.addEventListener('input', function() {
  // Get the current value of the input field
  const term = input.value.trim();

  // Make an AJAX request to fetch pharmacy autosuggestions
  if (term) {
    fetch(`/search/pharmacy/suggest/${term}/`)
      .then(response => response.json())
      .then(data => {
        // Clear previous suggestions
        suggestionsContainer.innerHTML = '';

        // Render new suggestions
        data.autosuggestions.forEach(suggestion => {
          const suggestionDiv = document.createElement('div');
          const suggestionPharmacyName = document.createElement('p');
          const suggestionPharmacyAddress = document.createElement('p');

          suggestionPharmacyName.textContent = suggestion.pharmacy_name;
          suggestionPharmacyAddress.textContent = suggestion.address;

          suggestionDiv.appendChild(suggestionPharmacyName);
          suggestionDiv.appendChild(suggestionPharmacyAddress);

          suggestionsContainer.appendChild(suggestionDiv);
        });
      })
      .catch(error => console.error('Error fetching autosuggestions:', error));
  } else {
    // Clear suggestions if input field is empty
    suggestionsContainer.innerHTML = '';
  }
});