# 🌐 Chat With Webpage

> **Turn any webpage into an interactive AI conversation.**

Chat With Webpage is an AI-powered Chrome extension that lets users ask questions about the webpage they are currently viewing. Instead of manually searching through long articles, documentation, product pages, blogs, or educational content, users can simply open the extension and chat with the page.

The project combines a Chrome Extension, FastAPI, LangChain, and an open-source Hugging Face model to create a conversational webpage assistant.

---

## ✨ Features

- 🌐 Chat with the current webpage
- 🤖 Open-source LLM integration through Hugging Face
- ⚡ FastAPI backend
- 🦜 LangChain integration
- 🔍 Context-aware question answering
- 🧩 Chrome Extension interface
- 🔐 Environment-based API key management
- 📚 Designed for Retrieval-Augmented Generation (RAG)
- 💬 Interactive conversational UI

---

## 🧠 How It Works

```text
                    ┌─────────────────────┐
                    │    Current Webpage  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Chrome Extension   │
                    │                     │
                    │ Extract Page Text   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │      Backend        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      LangChain      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Open-Source LLM    │
                    │   (Hugging Face)    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       Answer        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Chrome Chat UI    │
                    └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Backend development |
| ⚡ FastAPI | REST API |
| 🦜 LangChain | LLM orchestration |
| 🤗 Hugging Face | Open-source LLM |
| 🌐 JavaScript | Chrome extension logic |
| 🎨 HTML/CSS | Extension UI |
| 🧩 Chrome Extension API | Browser integration |
| 🔎 FAISS | Vector search / RAG |
| 📚 BeautifulSoup | Web content processing |

---

## 📁 Project Structure

```text
webpage-ai/
│
├── extension/
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── style.css
│
├── backend/
│   ├── main.py
│   └── requirements.txt
│  
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/chat-with-webpage.git
cd chat-with-webpage
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 🔑 Configuration

Create a file:

```text
backend/.env
```

Add your Hugging Face token:

```env
HF_TOKEN=your_huggingface_token
```

Never commit this file.

A safe template is provided as:

```text
.env.example
```

---

## ▶️ Run the Backend

Navigate to the backend:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🧩 Install the Chrome Extension

1. Open Google Chrome.
2. Navigate to:

```text
chrome://extensions/
```

3. Enable **Developer mode**.
4. Click **Load unpacked**.
5. Select the `extension/` folder.
6. Pin the extension to the Chrome toolbar.

---

## 💬 Usage

1. Open any webpage.
2. Click the **Chat With Webpage** extension.
3. Click **Load Page**.
4. Ask a question about the webpage.

### Example questions

```text
What is this page about?
```

```text
Summarize this page in 5 bullet points.
```

```text
What are the main concepts discussed here?
```

```text
Explain this article in simple terms.
```

```text
What are the key features mentioned on this page?
```

---

## 🧪 Example Use Cases

### 📖 Articles

Ask:

> What is the main argument of this article?

### 📚 Documentation

Ask:

> How does this API work?

### 🛒 Product Pages

Ask:

> What are the main features of this product?

### 🎓 Educational Content

Ask:

> Explain this topic in simple terms.

### 🔬 Research Papers

Ask:

> What problem is this paper trying to solve?

---

## 🧠 Planned RAG Architecture

The current project is designed to evolve into a full Retrieval-Augmented Generation system.

Instead of sending the entire webpage to the LLM for every question:

```text
Webpage
   │
   ▼
Text Extraction
   │
   ▼
Text Splitting
   │
   ▼
Embeddings
   │
   ▼
FAISS Vector Store
   │
   ▼
Relevant Chunks
   │
   ▼
Open-Source LLM
   │
   ▼
Answer
```

This will make the system more suitable for large webpages and improve the relevance of generated answers.

---

## 🗺️ Roadmap

### ✅ Phase 1 — Core Prototype

- [x] Chrome extension setup
- [x] Webpage text extraction
- [x] FastAPI backend
- [x] LLM integration
- [x] Basic webpage question answering

### 🔄 Phase 2 — RAG

- [ ] Implement document chunking
- [ ] Generate embeddings
- [ ] Integrate FAISS
- [ ] Implement similarity search
- [ ] Retrieve relevant webpage chunks
- [ ] Improve prompt/context handling

### 🔮 Phase 3 — Advanced Features

- [ ] Conversation memory
- [ ] Page summarization
- [ ] Source citations
- [ ] Highlight relevant webpage sections
- [ ] PDF support
- [ ] Multiple webpage comparison
- [ ] Streaming responses
- [ ] Improved UI/UX
- [ ] Better error handling

---

## 🔐 Security

API credentials are stored using environment variables.

Sensitive files such as:

```text
.env
```

are excluded from Git using `.gitignore`.

**Never expose your Hugging Face token in:**

- Source code
- GitHub repositories
- Screenshots
- Frontend JavaScript
- Chrome extension files

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

### Fork the repository

```bash
git clone https://github.com/YOUR_USERNAME/chat-with-webpage.git
```

Create a branch:

```bash
git checkout -b feature/my-feature
```

Make your changes:

```bash
git add .
git commit -m "Add my feature"
```

Push your branch:

```bash
git push origin feature/my-feature
```

Then open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Yash Rajan**

Built with ❤️ using Python, FastAPI, LangChain, Hugging Face, JavaScript, HTML, and CSS.
