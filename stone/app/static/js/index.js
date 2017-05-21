function sucesso() {
    var url = window.location.href;
    //testa se a url contain a slug mensagem enviada
    if(url.split("mensagem_enviada").length > 1) {
        $('#success').html("<div class='alert alert-success'>");
        $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
        $('#success > .alert-success')
            .append("<strong>Sua Mensagem Foi Enviada. </strong>");
        $('#success > .alert-success')
            .append('</div>');

        //clear all fields
        $('#contactForm').trigger("reset");
    }


}