<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Mengambil data dari form
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Validasi email
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
        // Detail email
        $to = "radenmanis123@gmail.com@gmail.com"; // Ganti dengan email penerima
        $subject = "New Message from " . $name;
        $body = "Name: " . $name . "\n";
        $body .= "Email: " . $email . "\n\n";
        $body .= "Message:\n" . $message;
        $headers = "From: " . $email;

        // Mengirim email
        if (mail($to, $subject, $body, $headers)) {
            echo "Message sent successfully!";
        } else {
            echo "Failed to send the message.";
        }
    } else {
        echo "Invalid email format.";
    }
}
?>