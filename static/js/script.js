/// Alerta de la version pre beta ///
//alert("Pre Beta");
console.log('Version Prebeta');

// Script para abrir y cerrar el botón desplegable del menu en smartphone //
function open_close_menu(){

    var btn_blog = document.getElementById('menu_blog');

    var menu = document.getElementById('menu');
    var btn_menu = document.getElementById('btn_menu');

    if ( menu.style.display == 'none' ){
        
        menu.style.display = 'flex';
        btn_blog.style.display = 'none';

    }else if ( menu.style.display = 'flex' ){

        menu.style.display = 'none';
    }

    if ( menu.style.display == 'flex' ){

        btn_menu.style.display = 'none';

    }else if ( menu.style.display = 'none' ) {

        btn_menu.style.display = 'block';
        btn_blog.style.display = 'block';

    }




}
