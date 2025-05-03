document.addEventListener('DOMContentLoaded', function() {
  const saveButton = document.getElementById('saveButton');
  const statusDiv = document.getElementById('status');

  saveButton.addEventListener('click', async () => {
    try {
      // Get the current tab
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      
      if (!tab.url) {
        throw new Error('No URL found');
      }

      // Send the URL to the API
      const response = await fetch('http://localhost/api/process', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'PUT, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type'
        },
        mode: 'cors',
        body: JSON.stringify({
          content: tab.url
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      // Show success message
      statusDiv.textContent = 'Page saved successfully!';
      statusDiv.className = 'success';
      statusDiv.style.display = 'block';

    } catch (error) {
      // Show error message
      statusDiv.textContent = `Error: ${error.message}`;
      statusDiv.className = 'error';
      statusDiv.style.display = 'block';
    }

    // Hide the status message after 3 seconds
    setTimeout(() => {
      statusDiv.style.display = 'none';
    }, 3000);
  });
}); 