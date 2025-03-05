// Function to navigate between pages
function navigateTo(page) {
    window.location.href = page;
}

// Function to send a chat message
function sendMessage() {
    let messageBox = document.getElementById("chat-box");
    let input = document.getElementById("message").value;
    if (input.trim() !== "") {
        messageBox.innerHTML += `<p>👤 You: ${input}</p>`;
        document.getElementById("message").value = "";
    }
}
