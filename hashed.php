<?php
$input = trim(fgets(STDIN));
echo password_hash($input, PASSWORD_DEFAULT);
echo "\n";
?>
