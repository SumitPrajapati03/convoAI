# convoAI

A full-stack AI chatbot with real-time streaming responses, smart context-aware follow-up suggestions, and multi-provider LLM support — built with FastAPI and React.

## ✨ Features

- **Real-time streaming responses** — Words appear progressively via Server-Sent Events (SSE) with a blinking cursor, giving a fast, responsive chat feel. Automatically falls back to a standard API call if streaming fails.
- **Context-aware follow-up suggestions** — After every AI response, 3–4 relevant follow-up questions are generated based on the actual conversation topic (not generic filler). Includes relevance validation, duplicate filtering, and retry logic.
- **Multi-provider LLM support** — Works with Groq, Gemini, and Ollama, with automatic fallback between providers if one is unavailable.
- **Reliable suggestion sync** — Request tracking and conversation validation ensure suggestions never leak between different chats, even with rapid switching or slow networks.
- **Clean, minimal UI** — A premium, distraction-free interface inspired by Claude and Linear, with soft rounded corners, generous spacing, and a brown accent used only for key actions.
- **Conversation management** — Sidebar with searchable chat history, new chat creation, and persistent conversations.

## 🛠 Tech Stack

**Backend**
- Python, FastAPI
- SSE (Server-Sent Events) for streaming
- Multi-provider LLM integration (Groq / Gemini / Ollama)

**Frontend**
- React
- Tailwind CSS

## 📁 Project Structure

```
convoAI/
├── backend/
│   ├── main.py
│   ├── routers/
│   │   ├── chat.py
│   │   └── stream.py
│   ├── services/
│   │   ├── llm_manager.py
│   │   ├── suggestion_service.py
│   │   └── conversation_service.py
│   ├── schemas/
│   │   ├── stream.py
│   │   └── suggestion.py
│   └── test_suggestions.py
└── frontend/
    └── src/
        ├── components/
        │   ├── ChatInterface.jsx
        │   ├── MessageList.jsx
        │   ├── MessageInput.jsx
        │   ├── SuggestionBar.jsx
        │   ├── Sidebar.jsx
        │   └── ConversationList.jsx
        └── services/
            ├── api.js
            └── suggestionApi.js
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Node.js 18+
- API keys for at least one LLM provider (Groq, Gemini, or a local Ollama instance)

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

The backend will start on `http://localhost:8000`.

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will start on `http://localhost:5173` (or your configured Vite port).

### Environment Variables

Create a `.env` file in the `backend` directory with your LLM provider credentials:

```env
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_gemini_key
OLLAMA_BASE_URL=http://localhost:11434
```

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/chat/message` | Send a message and get a full response |
| `POST` | `/api/chat/stream` | Send a message and stream the response via SSE |
| `GET` | `/api/chat/suggestions/{conversation_id}` | Get context-aware follow-up suggestions |

## 🧠 How It Works

### Streaming
The backend generates the full LLM response, then streams it to the frontend word-by-word over SSE with a small delay between chunks. This keeps the architecture provider-independent and stable while still delivering a real-time feel. If the stream fails, the app transparently falls back to a normal request/response call.

### Suggestions
Follow-up suggestions are generated from the last several messages in the conversation. The service extracts topic keywords, filters out generic phrases, removes duplicates, and validates that suggestions are actually relevant to the conversation — retrying once if not, and falling back to sensible defaults only when generation fails.

## 🧪 Testing

```bash
cd backend
python test_suggestions.py
```

## 📄 License

This project currently has no license specified.
