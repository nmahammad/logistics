document.addEventListener('DOMContentLoaded', function () {
    // Get the form element
    const form = document.querySelector('form');
  
    // Add a submit event listener to the form
    form.addEventListener('submit', function (event) {
      // Prevent the default form submission
      event.preventDefault();
  
      // Collect form data
      const formData = {
        sender: {
          name: document.getElementById('inputSenderName').value,
          surname: document.getElementById('inputSenderSurname').value,
          address: document.getElementById('inputSenderAddress').value,
          email: document.getElementById('inputSenderEmail').value,
          phone: document.getElementById('inputSenderPhone').value,
        },
        receiver: {
          name: document.getElementById('inputReceiverName').value,
          surname: document.getElementById('inputReceiverSurname').value,
          address: document.getElementById('inputReceiverAddress').value,
        },
        orderDate: new Date().toLocaleString()
      };
  
      // Make a POST request to the server API
      fetch('your-api-endpoint', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      })
        .then(response => {
          if (response.ok) {
            // Redirect to the success page if the POST request is successful
            window.location.href = 'success.html';
          } else {
            window.location.href = 'error.html';
            throw new Error('Failed to send shipment details');
          }
        })
        .catch(error => {
          // Handle errors here, e.g., display an error message to the user
          console.error('Error:', error);
        });
    });
  });
  