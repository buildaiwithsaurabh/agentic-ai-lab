"use client";

import { useState, useRef, useEffect } from "react";
import { models } from "../lib/models";
import { providers, type ProviderId } from "../lib/providers";
import type { ModelConfig } from "../lib/models";
import { ChevronDown, Zap, Circle, Brain } from "lucide-react";

interface ModelSelectorProps {
  selectedModel: ModelConfig;
  onModelChange: (model: ModelConfig) => void;
}

const speedIcon: Record<string, React.ReactNode> = {
  Fast: <Zap size={11} />,
  Medium: <Circle size={11} />,
  Slow: <Brain size={11} />,
};

const speedColor: Record<string, string> = {
  Fast: "#16a34a",
  Medium: "#d97706",
  Slow: "#7c3aed",
};

const PROVIDER_ORDER: ProviderId[] = ["groq", "google", "openai"];

export default function ModelSelector({ selectedModel, onModelChange }: ModelSelectorProps) {
  const [open, setOpen] = useState(false);
  const [activeProvider, setActiveProvider] = useState<ProviderId>(selectedModel.provider);
  const dropdownRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(e.target as Node)) {
        setOpen(false);
      }
    };
    document.addEventListener("mousedown", handler);
    return () => document.removeEventListener("mousedown", handler);
  }, []);

  const providerModels = models.filter((m) => m.provider === activeProvider);
  const currentProvider = providers[selectedModel.provider];

  return (
    <div className="model-selector" ref={dropdownRef}>
      {/* Trigger Button */}
      <button
        type="button"
        className="model-trigger"
        onClick={() => setOpen((o) => !o)}
        aria-expanded={open}
        aria-label="Select AI model"
        style={{ "--provider-color": currentProvider.color } as React.CSSProperties}
      >
        <span className="model-trigger-icon">{currentProvider.icon}</span>
        <span className="model-trigger-name">{selectedModel.name}</span>
        <ChevronDown
          size={14}
          className={`model-trigger-chevron ${open ? "open" : ""}`}
        />
      </button>

      {/* Dropdown Panel */}
      {open && (
        <div className="model-dropdown" role="dialog" aria-label="Model picker">
          {/* Provider Tabs */}
          <div className="provider-tabs">
            {PROVIDER_ORDER.map((pid) => {
              const p = providers[pid];
              return (
                <button
                  key={pid}
                  type="button"
                  className={`provider-tab ${activeProvider === pid ? "active" : ""}`}
                  style={{ "--tab-color": p.color } as React.CSSProperties}
                  onClick={() => setActiveProvider(pid)}
                >
                  <span>{p.icon}</span>
                  <span>{p.name}</span>
                </button>
              );
            })}
          </div>

          {/* Model List */}
          <div className="model-list" role="listbox">
            {providerModels.map((m) => {
              const isSelected = m.id === selectedModel.id;
              return (
                <button
                  key={m.id}
                  type="button"
                  role="option"
                  aria-selected={isSelected}
                  className={`model-option ${isSelected ? "selected" : ""}`}
                  onClick={() => {
                    onModelChange(m);
                    setOpen(false);
                  }}
                >
                  <div className="model-option-header">
                    <span className="model-option-name">{m.name}</span>
                    <span
                      className="model-speed-badge"
                      style={{ color: speedColor[m.speed] }}
                    >
                      {speedIcon[m.speed]}
                      {m.speed}
                    </span>
                  </div>
                  <p className="model-option-desc">{m.description}</p>
                  <div className="model-option-meta">
                    <span className="model-ctx">{m.contextWindow} ctx</span>
                    {m.tags?.map((tag) => (
                      <span key={tag} className="model-tag">{tag}</span>
                    ))}
                  </div>
                </button>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
