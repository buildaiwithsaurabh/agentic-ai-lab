"use client";

import { Bot } from "lucide-react";

export default function TypingIndicator() {
  return (
    <div className="message-wrapper assistant-wrapper">
      <div className="message-avatar">
        <div className="avatar assistant-avatar">
          <Bot size={18} />
        </div>
      </div>
      <div className="message assistant typing">
        <div className="typing-indicator">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </div>
  );
}
