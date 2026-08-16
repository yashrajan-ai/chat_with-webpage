let pageText = "";


// ============================================
// Get current webpage text
// ============================================

document
    .getElementById("extractBtn")
    .addEventListener("click", async () => {

        const [tab] = await chrome.tabs.query({
            active: true,
            currentWindow: true
        });

        try {

            const results = await chrome.scripting.executeScript({
                target: {
                    tabId: tab.id
                },

                func: () => document.body.innerText
            });

            pageText = results[0].result;

            document.getElementById("status").innerText =
                "Page loaded successfully.";

            addMessage(
                "ai",
                "I have loaded this webpage. Ask me anything about it."
            );

        } catch (error) {

            console.error(error);

            document.getElementById("status").innerText =
                "Could not read this webpage.";
        }
    });


// ============================================
// Ask question
// ============================================

document
    .getElementById("askBtn")
    .addEventListener("click", async () => {

        const questionInput =
            document.getElementById("question");

        const question =
            questionInput.value.trim();

        if (!question) {
            return;
        }

        if (!pageText) {

            addMessage(
                "ai",
                "Please click 'Load Page' first."
            );

            return;
        }

        // Show user's question

        addMessage(
            "user",
            question
        );

        questionInput.value = "";

        addMessage(
            "ai",
            "Thinking..."
        );

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/ask",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({
                        page_text: pageText,
                        question: question
                    })
                }
            );

            const data = await response.json();

            // Remove "Thinking..."

            const chatBox =
                document.getElementById("chatBox");

            chatBox.lastElementChild.remove();

            addMessage(
                "ai",
                data.answer
            );

        } catch (error) {

            console.error(error);

            const chatBox =
                document.getElementById("chatBox");

            chatBox.lastElementChild.remove();

            addMessage(
                "ai",
                "Something went wrong while contacting the server."
            );
        }
    });


// ============================================
// Add message to chat
// ============================================

function addMessage(type, message) {

    const chatBox =
        document.getElementById("chatBox");

    const div =
        document.createElement("div");

    div.classList.add(
        "message",
        type
    );

    div.innerText = message;

    chatBox.appendChild(div);

    chatBox.scrollTop =
        chatBox.scrollHeight;
}