<?php
$destinatario = "astrabazaar@gmail.com";
$asunto = "Prueba de correo desde PHP";
$mensaje = "Este es un correo de prueba enviado desde PHP.";

if (mail($destinatario, $asunto, $mensaje)) {
    echo "El correo ha sido enviado correctamente.";
} else {
    echo "Error al enviar el correo.";
}
?>

