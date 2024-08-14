function pruebaFor ( numero ) {
    const lista = [];
    for ( let num = 1; num <= numero; num++ ) {
        lista.push( num );
    }
    return lista;
}

function pruebaWhile ( numero ) {
    const lista = [];
    let contador = 1;
    while ( contador <= numero ) {
        lista.push( contador );
        contador++;
    }
    return lista;
}

// Medir el tiempo para pruebaFor
console.time( 'pruebaFor' );
pruebaFor( 10 );
console.timeEnd( 'pruebaFor' );

// Imprimir separación
console.log( "Intermedio" );

// Medir el tiempo para pruebaWhile
console.time( 'pruebaWhile' );
pruebaWhile( 10 );
console.timeEnd( 'pruebaWhile' );
