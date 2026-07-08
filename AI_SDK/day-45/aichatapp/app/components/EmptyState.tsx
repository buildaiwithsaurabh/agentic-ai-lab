import { Sparkles, Code, Pencil, HelpCircle } from "lucide-react";

interface EmptyStateProps {
  onSuggestionClick?: (prompt: string) => void;
}

export default function EmptyState({ onSuggestionClick }: EmptyStateProps) {
  const suggestions = [
    {
      text: "Explain quantum computing in simple terms",
      icon: <HelpCircle className="suggestion-icon" size={18} />,
    },
    {
      text: "Write a TypeScript function to fetch API data with error handling",
      icon: <Code className="suggestion-icon" size={18} />,
    },
    {
      text: "Draft an email requesting a deadline extension politely",
      icon: <Pencil className="suggestion-icon" size={18} />,
    },
    {
      text: "Suggest 5 creative naming ideas for a green energy startup",
      icon: <Sparkles className="suggestion-icon" size={18} />,
    },
  ];

  return (
    <div className="empty">
      <div className="empty-content">
        <div className="empty-header">
          <div className="empty-icon-wrapper">
            <Sparkles size={36} className="empty-spark-icon" />
          </div>
          <h3>How can I help you today?</h3>
          <p>Ask a question, brainstorm ideas, write code, or just chat.</p>
        </div>

        <div className="suggestions-grid">
          {suggestions.map((suggestion, index) => (
            <button
              key={index}
              className="suggestion-card"
              onClick={() => onSuggestionClick?.(suggestion.text)}
            >
              <div className="suggestion-card-header">
                {suggestion.icon}
                <span className="suggestion-text">{suggestion.text}</span>
              </div>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
