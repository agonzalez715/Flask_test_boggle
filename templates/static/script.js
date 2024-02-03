// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('guessForm').onsubmit = async function(e) {
        e.preventDefault(); // Prevent form from submitting the traditional way

        let guess = document.querySelector('input[name="guess"]').value;
        let response = await fetch('/guess', {
            method: 'POST',
            body: JSON.stringify({ guess: guess }),
            headers: {
                'Content-Type': 'application/json'
            }
        });
        let result = await response.json();

        // Display feedback based on the response
        alert(result.message);
    };
});
