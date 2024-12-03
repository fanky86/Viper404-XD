// Import library yang diperlukan
const express = require('express');
const axios = require('axios');
const app = express();

// Endpoint callback yang menerima parameter dari Facebook
app.get('/callback', (req, res) => {
    const accessToken = req.query.access_token; // Ambil token akses dari URL parameter

    // Cek apakah token akses ada
    if (accessToken) {
        // URL untuk mengambil data pengguna dari Graph API Facebook
        const graphUrl = `https://graph.facebook.com/me?access_token=${accessToken}&fields=id,name,email`;

        // Kirim request ke Facebook Graph API untuk mendapatkan data pengguna
        axios.get(graphUrl)
            .then(response => {
                // Tanggapan dari Facebook, kirimkan data pengguna ke client
                res.json({
                    message: 'Login successful',
                    userData: response.data
                });
            })
            .catch(error => {
                // Jika ada error saat mengambil data pengguna
                res.status(500).json({
                    message: 'Error fetching user data',
                    error: error.message
                });
            });
    } else {
        // Jika token akses tidak ada
        res.status(400).json({
            message: 'No access token received'
        });
    }
});

// Jalankan server di port 3000
app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});
