const express = require("express");
const app = express();

// Endpoint untuk callback
app.get("/callback", (req, res) => {
    const authCode = req.query.code; // Mendapatkan kode otorisasi dari query
    if (authCode) {
        res.send(`Kode Otorisasi: ${authCode}`);
    } else {
        res.send("Kode otorisasi tidak ditemukan!");
    }
});

// Jalankan server
app.listen(3000, () => {
    console.log("Server berjalan di https://fankyxd.xyz/callback"); // Pastikan URL callback benar
});

module.exports = app;
