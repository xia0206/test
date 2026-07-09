const display = document.getElementById("display");
const historyBox = document.getElementById("history");
const buttons = document.querySelectorAll(".btn");

let expression = "";

function updateDisplay() {
  display.textContent = expression || "0";
}

function isOperator(value) {
  return ["+", "-", "*", "/", "%"].includes(value);
}

function getCurrentNumber() {
  const parts = expression.split(/[+\-*/%]/);
  return parts[parts.length - 1];
}

function addValue(value) {
  const lastChar = expression.slice(-1);

  if (value === "." && getCurrentNumber().includes(".")) {
    return;
  }

  if (isOperator(value) && expression === "" && value !== "-") {
    return;
  }

  if (isOperator(value) && isOperator(lastChar)) {
    expression = expression.slice(0, -1) + value;
  } else {
    expression += value;
  }

  updateDisplay();
}

function clearAll() {
  expression = "";
  historyBox.textContent = "";
  updateDisplay();
}

function deleteLast() {
  expression = expression.slice(0, -1);
  updateDisplay();
}

function calculate() {
  if (!expression) return;

  try {
    const safeExpression = expression.replace(/%/g, "/100");

    if (!/^[0-9+\-*/().\s]+$/.test(safeExpression)) {
      throw new Error("Invalid expression");
    }

    const result = Function(`"use strict"; return (${safeExpression})`)();

    if (!Number.isFinite(result)) {
      throw new Error("Invalid result");
    }

    historyBox.textContent = expression + " =";
    expression = String(Number(result.toFixed(10)));
    updateDisplay();
  } catch {
    display.textContent = "错误";
    expression = "";
  }
}

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const value = button.dataset.value;
    const action = button.dataset.action;

    if (value) addValue(value);
    if (action === "clear") clearAll();
    if (action === "delete") deleteLast();
    if (action === "calculate") calculate();
  });
});

document.addEventListener("keydown", (event) => {
  const key = event.key;

  if (/^[0-9+\-*/.%]$/.test(key)) {
    addValue(key);
  } else if (key === "Enter") {
    event.preventDefault();
    calculate();
  } else if (key === "Backspace") {
    deleteLast();
  } else if (key === "Escape") {
    clearAll();
  }
});
