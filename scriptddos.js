async function sendRequest(url, threadId) {
    const proxyUrl = 'https://cors-anywhere.herokuapp.com/'; // Proxy CORS
    const finalUrl = proxyUrl + url; // Tambahkan proxy ke URL

    try {
        const response = await fetch(finalUrl);
        const resultText = `Thread ${threadId}: Kode Respons: ${response.status}`;
        displayResult(resultText);
    } catch (error) {
        const resultText = `Thread ${threadId}: Error - ${error.message}`;
        displayResult(resultText);
    }
}

function displayResult(result) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML += `<p>${result}</p>`;
}

function startTesting() {
    const url = document.getElementById('url').value;
    const numThreads = parseInt(document.getElementById('threads').value);
    const duration = parseInt(document.getElementById('duration').value);
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Clear previous results

    // Start sending requests for the specified duration
    const endTime = Date.now() + duration * 1000;

    for (let i = 0; i < numThreads; i++) {
        const threadId = i + 1;
        const interval = setInterval(() => {
            if (Date.now() < endTime) {
                sendRequest(url, threadId);
            } else {
                clearInterval(interval);
            }
        }, 1000); // Send a request every second
    }
}
