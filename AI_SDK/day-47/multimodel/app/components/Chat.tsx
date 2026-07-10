"use client";

import { useChat } from "@ai-sdk/react";
import { useState } from "react";
import Message from "./Message";
import ChatInput from "./ChatInput";
import EmptyState from "./EmptyState";
import TypingIndicator from "./TypingIndicator";
import ModelSelector from "./ModelSelector";
import useAutoScroll from "../hooks/useAutoScroll";
import { AlertCircle, RotateCcw } from "lucide-react";
import { UIMessage } from "ai";
import { models, DEFAULT_MODEL_ID, findModel } from "../lib/models";
import type { ModelConfig } from "../lib/models";
import { providers } from "../lib/providers";

const defaultModel = findModel(DEFAULT_MODEL_ID) ?? models[0];

export default function Chat() {
  const [selectedModel, setSelectedModel] = useState<ModelConfig>(defaultModel);

  const {
    messages,
    sendMessage,
    regenerate,
    status,
    error,
  } = useChat({
    body: {
      modelId: selectedModel.id,
      providerId: selectedModel.provider,
    },
  });

  const isLoading = status === "submitted" || status === "streaming";

  const lastMessage = messages[messages.length - 1];
  const isUserMessage = lastMessage?.role === "user";

  const { scrollContainerRef, messagesEndRef } = useAutoScroll(
    [messages, isLoading],
    isUserMessage
  );

  const handleSuggestionClick = (promptText: string) => {
    sendMessage({ text: promptText });
  };

  const getMessageText = (message: UIMessage) => {
    return message.parts
      .filter((part) => part.type === "text")
      .map((part) => (part as any).text)
      .join("");
  };

  const currentProvider = providers[selectedModel.provider];

  return (
    <div className="chat-container">
      {/* Model Selector Bar */}
      <div className="model-selector-bar">
        <div className="model-selector-label">
          <span
            className="provider-dot"
            style={{ background: currentProvider.color }}
          />
          <span>Model</span>
        </div>
        <ModelSelector
          selectedModel={selectedModel}
          onModelChange={(model) => setSelectedModel(model)}
        />
      </div>

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
