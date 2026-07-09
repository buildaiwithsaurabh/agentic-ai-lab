"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { User, Bot } from "lucide-react";
import CodeBlock from "./CodeBlock";

interface MessageProps {
  role: string;
  content: string;
}

export default function Message({ role, content }: MessageProps) {
  const isUser = role === "user";

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
                    <CodeBlock
                      language={match[1]}
                      value={codeText}
                    />
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

