"use client";

import { useChat } from "@ai-sdk/react";
import Message from "./Message";
import ChatInput from "./ChatInput";
import EmptyState from "./EmptyState";
import TypingIndicator from "./TypingIndicator";
import useAutoScroll from "../hooks/useAutoScroll";
import { AlertCircle, RotateCcw } from "lucide-react";
import { UIMessage } from "ai";

export default function Chat() {
  const {
    messages,
    sendMessage,
    regenerate,
    status,
    error,
  } = useChat();

  const isLoading = status === "submitted" || status === "streaming";
  
  const lastMessage = messages[messages.length - 1];
  const isUserMessage = lastMessage?.role === "user";
  
  const { scrollContainerRef, messagesEndRef } = useAutoScroll(
    [messages, isLoading],
    isUserMessage
  );

  // Click suggestions triggers immediate submission
  const handleSuggestionClick = (promptText: string) => {
    sendMessage({ text: promptText });
  };

  const getMessageText = (message: UIMessage) => {
    return message.parts
      .filter((part) => part.type === "text")
      .map((part) => (part as any).text)
      .join("");
  };

  return (
    <div className="chat-container">
      {/* Message List area */}
      <div className="chat-messages" ref={scrollContainerRef}>
        {messages.length === 0 ? (
          <EmptyState onSuggestionClick={handleSuggestionClick} />
        ) : (
          <div className="messages-list">
            {messages.map((message, index) => (
              <Message
                key={message.id || index}
                role={message.role}
                content={getMessageText(message)}
              />
            ))}
            
            {/* Typing indicator */}
            {isLoading && lastMessage?.role === "user" && (
              <TypingIndicator />
            )}
            
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>

      {/* Error Banner */}
      {error && (
        <div className="error-banner">
          <AlertCircle size={18} />
          <p>Failed to get response: {error.message || "Please check your network connection or API keys."}</p>
          <button onClick={() => regenerate()} className="retry-button" type="button">
            <RotateCcw size={14} style={{ marginRight: "4px" }} />
            Retry
          </button>
        </div>
      )}

      {/* Input controls */}
      <ChatInput onSend={(text) => sendMessage({ text })} />
    </div>
  );
}

