const display = document.getElementById('display');

// Append number to display
function appendNumber(num) {
    if (display.value === '0' && num !== '.') {
        display.value = num;
    } else if (num === '.' && display.value.includes('.')) {
        return; // Prevent multiple decimal points
    } else {
        display.value += num;
    }
}

// Append operator to display
function appendOperator(op) {
    if (display.value === '' && op !== '.') return;
    
    // Prevent multiple operators in a row
    const lastChar = display.value[display.value.length - 1];
    if (['+', '-', '*', '/'].includes(lastChar) && op !== '.') {
        display.value = display.value.slice(0, -1) + op;
        return;
    }
    
    display.value += op;
}

// Delete last character
function deleteLastChar() {
    display.value = display.value.slice(0, -1);
    if (display.value === '') {
        display.value = '0';
    }
}

// Clear display
function clearDisplay() {
    display.value = '0';
}

// Calculate result
function calculate() {
    try {
        // Remove any spaces
        const expression = display.value.trim();
        
        // Validate expression
        if (expression === '' || /[+\-*/.]$/.test(expression)) {
            display.value = 'Error';
            return;
        }
        
        // Evaluate the expression
        let result = eval(expression);
        
        // Round to avoid floating point errors
        result = Math.round(result * 10000000000) / 10000000000;
        
        display.value = result;
    } catch (error) {
        display.value = 'Error';
    }
}

// Keyboard support
document.addEventListener('keydown', (e) => {
    const key = e.key;
    
    // Number keys
    if (key >= '0' && key <= '9') {
        appendNumber(key);
    }
    // Operators
    else if (key === '+' || key === '-' || key === '*' || key === '/') {
        e.preventDefault();
        appendOperator(key);
    }
    // Decimal point
    else if (key === '.') {
        e.preventDefault();
        appendNumber('.');
    }
    // Enter or =
    else if (key === 'Enter' || key === '=') {
        e.preventDefault();
        calculate();
    }
    // Backspace
    else if (key === 'Backspace') {
        e.preventDefault();
        deleteLastChar();
    }
    // Escape to clear
    else if (key === 'Escape') {
        clearDisplay();
    }
});

// Initialize display
window.addEventListener('load', () => {
    display.value = '0';
});
