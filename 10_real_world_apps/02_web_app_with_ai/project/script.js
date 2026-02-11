function processCommand() {
    const input = document.getElementById("userInput").value.toLowerCase();
    const output = document.getElementById("output");

    if (input === "hello") {
        output.textContent = "Hello there!";

    } else if (input === "time") {
        const now = new Date();
        output.textContent = "Current time: " + now.toLocaleTimeString();

    } else if (input.startsWith("add")) {
        const parts = input.split(" ");
        if (parts.length === 3) {
            const num1 = parseFloat(parts[1]);
            const num2 = parseFloat(parts[2]);
            output.textContent = "Result: " + (num1 + num2);
        } else {
            output.textContent = "Usage: add 5 7";
        }

    } else {
        output.textContent = "I don't understand that command.";
    }
}
