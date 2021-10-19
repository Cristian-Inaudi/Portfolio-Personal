<footer class="site-footer">
    <div class="contenedor clearfix">
      <div class="footer-informacion">
        <h3>Sobre <span>gdlwebcamp</span></h3>
        <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sequi, neque, fugiat tempora iusto vitae quas ex hic obcaecati ipsum sit.</p>
      </div>
      <div class="ultimos-tweets">
        <h3>Últimos <span>tweets</span></h3>
        <a class="twitter-timeline" data-height="300" data-theme="light" data-link-color="#fe4918" href="https://twitter.com/CrisInaudi"></a> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
      </div>
      <div class="menu">
        <h3>Redes <span>sociales</span></h3>
        <nav class="redes-sociales">
          <a href="#"><i class="fa fa-facebook" aria-hidden="true"></i></a>
          <a href="#"><i class="fa fa-twitter" aria-hidden="true"></i></a>
          <a href="#"><i class="fa fa-pinterest-p" aria-hidden="true"></i></a>
          <a href="#"><i class="fa fa-youtube-play" aria-hidden="true"></i></a>
          <a href="#"><i class="fa fa-instagram" aria-hidden="true"></i></a>
        </nav>
      </div>
    </div>

    <p class="copyright">Todos los derechos Reservados GDLWEBCAMP 2016.</p>

    <!-- Begin Mailchimp Signup Form -->
    <link href="//cdn-images.mailchimp.com/embedcode/classic-10_7.css" rel="stylesheet" type="text/css">
    <style type="text/css">
      #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; }
      /* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
        We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
    </style>
  <div style="display:none;">
    <div id="mc_embed_signup">
    <form action="https://hotmail.us7.list-manage.com/subscribe/post?u=6c0a0d55b4743724fc0e6b29c&amp;id=be06d0b3a4" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
        <div id="mc_embed_signup_scroll">
      <h2>Suscríbete al Newsletter y no te pierdas nada de este evento</h2>
    <div class="indicates-required"><span class="asterisk">*</span> es obligatorio</div>
    <div class="mc-field-group">
      <label for="mce-EMAIL">Correo obligatorio  <span class="asterisk">*</span>
    </label>
      <input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
    </div>
    <div class="mc-field-group">
      <label for="mce-FNAME">First Name </label>
      <input type="text" value="" name="FNAME" class="" id="mce-FNAME">
    </div>
    <div class="mc-field-group">
      <label for="mce-LNAME">Last Name </label>
      <input type="text" value="" name="LNAME" class="" id="mce-LNAME">
    </div>
      <div id="mce-responses" class="clear">
        <div class="response" id="mce-error-response" style="display:none"></div>
        <div class="response" id="mce-success-response" style="display:none"></div>
      </div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
        <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_6c0a0d55b4743724fc0e6b29c_be06d0b3a4" tabindex="-1" value=""></div>
        <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
        </div>
    </form>
    </div>
    <script type='text/javascript' src='//s3.amazonaws.com/downloads.mailchimp.com/js/mc-validate.js'></script><script type='text/javascript'>(function($) {window.fnames = new Array(); window.ftypes = new Array();fnames[0]='EMAIL';ftypes[0]='email';fnames[1]='FNAME';ftypes[1]='text';fnames[2]='LNAME';ftypes[2]='text';fnames[3]='ADDRESS';ftypes[3]='address';fnames[4]='PHONE';ftypes[4]='phone';}(jQuery));var $mcj = jQuery.noConflict(true);</script>
    <!--End mc_embed_signup-->
  
  </div>

  </footer>

  <?php
    $archivo = basename($_SERVER['PHP_SELF']);
    $pagina = str_replace(".php" , "", $archivo);
    if($pagina == 'invitados' || $pagina == 'index') {
      echo '<script src="js/jquery.colorbox-min.js"></script>';
    } else if($pagina == 'conferencia') {
      echo '<script src="js/lightbox.js"></script>';
    } 
  ?>

  <script src="js/plugins.js"></script>
  <script src="js/jquery.js"></script>
  <script src="js/jquery.animateNumber.js"></script>
  <script src="js/jquery.countdown.min.js"></script>
  <script src="js/main.js"></script>
  <script src="js/cotizador.js"></script>
  <script defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBZOgZOY1LX3z-A8hSWjCOGj8pTYRkHEUM&callback=initMap"></script>


  <!-- Google Analytics: change UA-XXXXX-Y to be your site's ID. -->
  <script>
    /*
    (function(b,o,i,l,e,r){
      b.GoogleAnalysticsObject=l;
      b[l]||{b[l]=function(){
        (b[l].q=b[l].q||[]).push(arguments)
    });
    b[l].l=+new Date;
    e=o.createElement(i);
    r=0.getElementsByTagName(i)[0];
    e.src="https://www.google-analystics.com/analytics.com/analytics.js";
    r.parentNode.insertBefore(e,r)}(window.document,"script","ga"));
    ga("create","UA-XXXXX-X","auto");ga("send", "pageview");
    */
    window.ga = function () { ga.q.push(arguments) }; ga.q = []; ga.l = +new Date;
    ga('create', 'UA-XXXXX-Y', 'auto'); ga('set', 'anonymizeIp', true); ga('set', 'transport', 'beacon'); ga('send', 'pageview')

    </script>
  <script src="https://www.google-analytics.com/analytics.js" async></script>
  <script id="mcjs">!function(c,h,i,m,p){m=c.createElement(h),p=c.getElementsByTagName(h)[0],m.async=1,m.src=i,p.parentNode.insertBefore(m,p)}(document,"script","https://chimpstatic.com/mcjs-connected/js/users/6c0a0d55b4743724fc0e6b29c/1b3ed7344b99b95ce2798ddf5.js");</script>
</body>

</html>