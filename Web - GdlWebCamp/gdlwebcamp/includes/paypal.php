<?php

require 'paypal/autoload.php';


define('URL_SITIO', 'http://localhost:7888/gdlwebcamp');

$apiContext = new \PayPal\Rest\ApiContext(
    new \PayPal\Auth\OAuthTokenCredential(
       
        'Ae2aRqGfi4uganenfOtaKUkHMCybFjQDTbys-jSJh5yYB1R4bAv6VSW74g1Fi2u8xQ4SE-w713Nf1jnu',   //ClienteID
       
        'EH6WDgLblbIf0CarU69FgEZsIC8RK-LftTDSeLng40xezKsBRchxwC0d94WxEu8cNDndm8YjNk_jcnw5'    //Secret
    )
);



?>