"use client";

import { UIMessage } from "ai";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { User, Bot, Copy, Check } from "lucide-react";
import { useState } from "react";

interface MessageProps {
  role: string;
  content: string;
}

export default function Message({ role, content }: MessageProps) {
  const isUser = role === "user";
  const [copied, setCopied] = useState(false);

  const handleCopy = (text: string) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className={`message-wrapper ${isUser ? "user-wrapper" : "assistant-wrapper"}`}>
      <div className="message-avatar">
        {isUser ? (
          <div className="avatar user-avatar">
            <User size={18} />
          </div>
        ) : (
          <div className="avatar assistant-avatar">
            <Bot size={18} />
          </div>
        )}
      </div>
      <div className={`message ${isUser ? "user" : "assistant"}`}>
        {isUser ? (
          <div className="message-content">{content}</div>
        ) : (
          <div className="message-content">
            <ReactMarkdown
              remarkPlugins={[remarkGfm]}
              components={{
                code({ node, className, children, ...props }) {
                  const match = /language-(\w+)/.exec(className || "");
                  const codeText = String(children).replace(/\n$/, "");
                  const isInline = !match;

                  if (isInline) {
                    return <code className="inline-code" {...props}>{children}</code>;
                  }

                  return (
                    <div className="code-block-wrapper">
                      <div className="code-block-header">
                        <span className="code-lang">{match[1] || "code"}</span>
                        <button
                          className="copy-btn"
                          onClick={() => handleCopy(codeText)}
                          type="button"
                          aria-label="Copy code"
                        >
                          {copied ? <Check size={14} /> : <Copy size={14} />}
                          <span>{copied ? "Copied!" : "Copy"}</span>
                        </button>
                      </div>
                      <pre className="code-pre">
                        <code className={className} {...props}>
                          {children}
                        </code>
                      </pre>
                    </div>
                  );
                },
              }}
            >
              {content}
            </ReactMarkdown>
          </div>
        )}
      </div>
    </div>
  );
}
