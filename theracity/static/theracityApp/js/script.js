$('#menu-btn').click(function() {
    $('nav .navigation ul').addClass('active')
});
$('#menu-close').click(function() {
    $('nav .navigation ul').removeClass('active')
});

// JavaScript to handle highlighting and creating IDs for search bar
document.addEventListener('DOMContentLoaded', function() {
    const searchContainer = document.querySelector('.search');
    const searchBar = document.getElementById('search-bar');
    const suggestionsContainer = document.querySelector('.suggestions')
    const pharmacies = document.getElementById('pharmacies');
    const medicines = document.getElementById('medicines');

    pharmacies.addEventListener('click', function() {
        if (medicines.classList.contains('active')) {
            inactivateSearchOptionItem(medicines);
        }
        
        if (pharmacies.classList.contains('active')) {
            inactivateSearchOptionItem(pharmacies);
        } else {
            pharmacies.classList.add('active');
            setSearchPlaceholder("Search for pharmacies");
            searchContainer.classList.remove('hidden');
            suggestionsContainer.classList.remove('hidden');
        }
    });
  
    medicines.addEventListener('click', function() {
        if (pharmacies.classList.contains('active')) {
            suggestionsContainer.innerHTML = '';
            inactivateSearchOptionItem(pharmacies);

        }
        
        if (medicines.classList.contains('active')) {
            suggestionsContainer.innerHTML = '';
            inactivateSearchOptionItem(medicines);
        } else {
            medicines.classList.add('active');
            setSearchPlaceholder("Search for medicines");
            searchContainer.classList.remove('hidden');
            suggestionsContainer.classList.remove('hidden');
            suggestionsContainer.innerHTML = '';
        }
    });

    function inactivateSearchOptionItem(item) {
        item.classList.remove('active');
        setSearchPlaceholder("");

        if (!searchContainer.classList.contains('hidden')) {
            searchContainer.classList.add('hidden');
        }

        if (!suggestionsContainer.classList.contains('hidden')) {
            var suggestions = suggestionsContainer.querySelectorAll('.suggestion');

            suggestions.forEach(element => {
                element.remove();
            })

            suggestionsContainer.classList.add('hidden');
        }

        if (searchBar.value) {
            searchBar.value = "";
        }  
    }

    function setSearchPlaceholder(placeholderText) {
        searchBar.placeholder = placeholderText;
    }  
});

// Search Autosuggestion Implementation
const searchBar = document.getElementById('search-bar');
const suggestionsContainer = document.querySelector('.suggestions');
const pharmacies = document.getElementById('pharmacies');
const medicines = document.getElementById('medicines');

// Add an event listener to detect changes in the input field
searchBar.addEventListener('input', function() {
  // Get the current value of the input field
  const term = searchBar.value.trim();

  // Make an AJAX request to fetch pharmacy autosuggestions
  if (pharmacies.classList.contains('active') && term) {
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

          suggestionDiv.classList.add('suggestion');

          suggestionPharmacyName.textContent = suggestion.pharmacy_name;
          suggestionPharmacyName.classList.add('pharmacy-name');

          suggestionPharmacyAddress.textContent = suggestion.address;
          suggestionPharmacyAddress.classList.add('pharmacy-address');

          suggestionDiv.appendChild(suggestionPharmacyName);
          suggestionDiv.appendChild(suggestionPharmacyAddress);

          // On pharmacy click, redirect to new page, sending the pharmacy id as query string
          suggestionDiv.addEventListener('click', () => {
            console.log(suggestion.pharmacy_id)
            const pharmacyId = suggestion.pharmacy_id;

            window.location.href = `/search/pharmacy/${pharmacyId}`;
          });

          suggestionsContainer.appendChild(suggestionDiv);
        });
      })
      .catch(error => console.error('Error fetching autosuggestions:', error));
  } else {
    // Clear suggestions if input field is empty
    suggestionsContainer.innerHTML = '';
  }

  // Make an AJAX request to fetch medicine autosuggestions
  if (medicines.classList.contains('active') && term) {
    fetch(`/search/medicine/suggest/${term}/`)
      .then(response => response.json())
      .then(data => {
        // Clear previous suggestions
        suggestionsContainer.innerHTML = '';

        console.log(data.autosuggestions)
        // Render new suggestions
        data.autosuggestions.forEach(suggestion => {
          const suggestionDiv = document.createElement('div');
          const suggestionMedicineName = document.createElement('p');

          suggestionDiv.classList.add('suggestion');

          suggestionMedicineName.textContent = suggestion.medicine_name;
          suggestionMedicineName.classList.add('medicine-name');

          suggestionDiv.appendChild(suggestionMedicineName);

          /* // On medicine click, redirect to new page, sending the pharmacy id as query string
          suggestionDiv.addEventListener('click', () => {
            const medicineId = suggestion.pharmacy_id;

            window.location.href = `/search/pharmacy/${pharmacyId}`;
          });
 */
          suggestionsContainer.appendChild(suggestionDiv);
        });
      })
      .catch(error => console.error('Error fetching autosuggestions:', error));
  } else {
    // Clear suggestions if input field is empty
    suggestionsContainer.innerHTML = '';
  }
});
