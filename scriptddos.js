let userAgentList = [];

// Fungsi untuk memuat user agent dari file
async function loadUserAgents() {
    try {
        const response = await fetch('ua.txt');
        if (!response.ok) throw new Error('Network response was not ok');
        userAgentList = await response.text();
        userAgentList = userAgentList.split('\n').map(agent => agent.trim()).filter(agent => agent);
    } catch (error) {
        console.error('Error loading user agents:', error);
    }
}

async function sendRequest(url, threadId) {
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'User-Agent': userAgentList[Math.floor(Math.random() * userAgentList.length)],
                'Cache-Control': 'no-cache'
            }
        });
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
    const threadCount = parseInt(document.getElementById('threads').value);
    const duration = parseInt(document.getElementById('duration').value);
    
    const endTime = Date.now() + duration * 1000;

    for (let i = 0; i < threadCount; i++) {
        if (Date.now() < endTime) {
            sendRequest(url, i + 1);
        }
    }
}

// Muat user agents saat halaman dimuat
window.onload = loadUserAgents;
