function showMessage() {
    const input = document.getElementById("userInput").value;
    const output = document.getElementById("output");

    output.textContent = "You typed: " + input;
}
