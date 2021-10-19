<?php 
    $conn = new mysqli('localhost:8889','root','root','agenda');
    
    if($conn->connect_error) {
      echo $error = $conn->connect_error;
    }

?>