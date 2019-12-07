function solonumeros(e){

   key=e.keycode || e.wich;
   teclado=string.fromCharCode(key);
   numeros="0123456789"
   especiales="8-37-38-46";
   teclado_especial=false; 
   for(var i in especiales){
     if(key==especiales[i]){
       teclado_especial=true;
     }
   }
   if(numeros.index(teclado)==-1 && !teclado_especial){
     return false;

   }
 }