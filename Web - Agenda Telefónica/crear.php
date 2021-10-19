<?php

  function peticion_ajax() {
    return isset($_SERVER['HTTP_X_REQUESTED_WITH']) && $_SERVER['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest';
  }

  $nombre = htmlspecialchars( $_POST['nombre'] );
  $telefono = htmlspecialchars( $_POST['telefono'] );
   
  try {
      require_once('funciones/bd_conexion.php');
      $sql = "INSERT INTO `contactos` (`id`, `nombre`, `telefono`) VALUES (NULL, '{$nombre}', '{$telefono}');";
    
      $resultado = $conn->query($sql);

      if(peticion_ajax() ) {
        echo json_encode(array(
          'respuesta' => $resultado,
          'nombre' => $nombre,
          'telefono' => $telefono,
          'id' => $conn->insert_id
        ));
      } else {
        exit;
      }
  } catch (Exception $e) {
      $error = $e->getMessage();
  }

    $conn->close();
?>
