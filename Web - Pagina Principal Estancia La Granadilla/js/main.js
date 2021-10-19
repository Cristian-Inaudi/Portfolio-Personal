var index = 0;

var imagenes = ["img/fondo1.jpg", "img/fondo2.jpg", "img/fondo3.jpg", "img/fondo4.jpg", "img/fondo5.jpg"];




$(function() {

    // Agregar clase a Menú

    $('body.conferencia .navegacion-principal a:contains("Conferencia")').addClass('activo');
    $('body.calendario .navegacion-principal a:contains("Calendario")').addClass('activo');
    $('body.invitados .navegacion-principal a:contains("Invitados")').addClass('activo');

    

    // Menu Responsive

    $(".menu-movil").on("click", function() {
        $(".navegacion-principal").slideToggle();
    });

    //Cambiar automaticamente imagen de fondo
    setInterval(changeImage, 5000);

});

function changeImage() {
    $('div.contenido-principal').css("background-image", 'url(' + imagenes[index] + ')');
    index++;

    if(index == 4) {
        index = 0;
    }
}