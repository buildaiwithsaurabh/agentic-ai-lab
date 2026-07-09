import React, { useState } from "react";
import { Send } from "lucide-react";

interface ChatInputProps {
  onSend: (message: string) => void;
}

export default function ChatInput({ onSend }: ChatInputProps) {
  const [input, setInput] = useState("");

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  return (
    <form className="chat-input-form" onSubmit={onSubmit}>
      <div className="chat-input-container">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question or type something..."
          type="text"
          className="chat-input-field"
          autoFocus
        />
        <button
          type="submit"
          disabled={!input.trim()}
          className="chat-submit-button"
          aria-label="Send message"
        >
          <Send size={18} />
        </button>
      </div>
    </form>
  );
}
