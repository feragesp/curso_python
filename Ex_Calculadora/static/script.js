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
    fetch('/calculate', {
        method: POST,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ expression }) //({"expresion": 7*6 })
    })
    .then(response => response.json()) //{"result": 42 }
    .then(data => {
        display.textContent = data.result;
    })
}



