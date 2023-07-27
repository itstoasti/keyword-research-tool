```javascript
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('scrape_button').addEventListener('click', startScrape);
});

function startScrape() {
    fetch('/start_scrape')
    .then(response => response.json())
    .then(data => {
        if (data.status === 'scrape_complete') {
            displayData();
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function displayData() {
    fetch('/get_data')
    .then(response => response.json())
    .then(data => {
        let dataDisplay = document.getElementById('data_display');
        dataDisplay.innerHTML = JSON.stringify(data, null, 2);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
```