const display = document.getElementById('display');
let currentInput = '';
let justCalculated = false;

document.querySelectorAll('.btn').forEach(button => {
    button.addEventListener('click', () => {
        const value = button.dataset.value;

        if (button.id === 'clear') {
            currentInput = '';
            display.textContent = '0';
            justCalculated = false;
        } else if (button.id === 'equals') {
            sendToServer(currentInput);
        } else {
            if (justCalculated && !isNaN(value)){
                //Si acabamos de calcular y ahora viene un nº, reiniciamos
                currentInput = value;
            } else {
                currentInput += value;
            }

            display.textContent = currentInput;
            justCalculated = false;
        }
    });
});

//Funcion de conexion Python y JavaScript
function sendToServer(expression) {
    //Hace peticiones HTTP desde JS
    fetch('/calculate', { // Ruta del server que espera la peticion
        method: 'POST', //Metodo de envío
        headers: {
            'Content-Type': 'application/json' // Dice al server que tipo de archivo vamos a trabajar
        },
        //Construye la expresion
        body: JSON.stringify({ expression }) //({"expresion": 7*6 })
    })
    //Respuesta del servidor
    .then(response => response.json()) //{"result": 42 }
    //Maneja el resultado
    .then(data => {
        display.textContent = data.result; // Muestra el resultado por pantalla
        currentInput = data.result.toString(); // Guarda el resultado para seguir calculando
        justCalculated = true; // Acabamos de ejecutar
    })
    //Captura el error y lo saca por consola
    .catch(err => { 
        display.textContent = 'Error';
        console.error(err);
    });
}



