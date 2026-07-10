import type { ProviderId } from "./providers";

export interface ModelConfig {
  id: string;
  name: string;
  description: string;
  provider: ProviderId;
  contextWindow: string;
  speed: "Fast" | "Medium" | "Slow";
  tags?: string[];
}

export const models: ModelConfig[] = [
  // ─── Groq Models ──────────────────────────────────────────────────────────
  {
    id: "llama-3.3-70b-versatile",
    name: "Llama 3.3 70B Versatile",
    description: "Meta's flagship model — balanced speed and capability.",
    provider: "groq",
    contextWindow: "128k",
    speed: "Fast",
    tags: ["Versatile", "Popular"],
  },
  {
    id: "llama-3.1-8b-instant",
    name: "Llama 3.1 8B Instant",
    description: "Ultra-fast small model for simple tasks.",
    provider: "groq",
    contextWindow: "128k",
    speed: "Fast",
    tags: ["Fastest"],
  },
  {
    id: "mixtral-8x7b-32768",
    name: "Mixtral 8x7B",
    description: "Mistral's MoE model with large context support.",
    provider: "groq",
    contextWindow: "32k",
    speed: "Fast",
    tags: ["MoE"],
  },
  {
    id: "gemma2-9b-it",
    name: "Gemma 2 9B",
    description: "Google's lightweight open model via Groq.",
    provider: "groq",
    contextWindow: "8k",
    speed: "Fast",
    tags: ["Google"],
  },

  // ─── Google Gemini Models ──────────────────────────────────────────────────
  {
    id: "gemini-2.5-flash",
    name: "Gemini 2.5 Flash",
    description: "Google's fastest thinking model with adaptive reasoning.",
    provider: "google",
    contextWindow: "1M",
    speed: "Fast",
    tags: ["Thinking", "New"],
  },
  {
    id: "gemini-2.5-pro",
    name: "Gemini 2.5 Pro",
    description: "Most capable Gemini model with 1M context and deep reasoning.",
    provider: "google",
    contextWindow: "1M",
    speed: "Medium",
    tags: ["Most Capable", "Thinking"],
  },
  {
    id: "gemini-2.0-flash",
    name: "Gemini 2.0 Flash",
    description: "Multimodal model with native tool-use and image support.",
    provider: "google",
    contextWindow: "1M",
    speed: "Fast",
    tags: ["Multimodal"],
  },
  {
    id: "gemini-1.5-pro",
    name: "Gemini 1.5 Pro",
    description: "Production-grade Gemini with massive context window.",
    provider: "google",
    contextWindow: "2M",
    speed: "Medium",
    tags: ["2M Context"],
  },
  {
    id: "gemini-1.5-flash",
    name: "Gemini 1.5 Flash",
    description: "Fast and efficient Gemini for everyday tasks.",
    provider: "google",
    contextWindow: "1M",
    speed: "Fast",
    tags: ["Efficient"],
  },

  // ─── OpenAI Models ─────────────────────────────────────────────────────────
  {
    id: "gpt-4o",
    name: "GPT-4o",
    description: "OpenAI's fastest flagship multimodal model.",
    provider: "openai",
    contextWindow: "128k",
    speed: "Fast",
    tags: ["Flagship", "Multimodal"],
  },
  {
    id: "gpt-4o-mini",
    name: "GPT-4o Mini",
    description: "Affordable and capable — best for everyday tasks.",
    provider: "openai",
    contextWindow: "128k",
    speed: "Fast",
    tags: ["Affordable"],
  },
  {
    id: "gpt-4-turbo",
    name: "GPT-4 Turbo",
    description: "High intelligence with vision and large context.",
    provider: "openai",
    contextWindow: "128k",
    speed: "Medium",
    tags: ["Vision"],
  },
  {
    id: "o1-mini",
    name: "o1 Mini",
    description: "OpenAI's fast reasoning model for STEM problems.",
    provider: "openai",
    contextWindow: "128k",
    speed: "Medium",
    tags: ["Reasoning"],
  },
  {
    id: "o3-mini",
    name: "o3 Mini",
    description: "Latest compact reasoning model from OpenAI.",
    provider: "openai",
    contextWindow: "200k",
    speed: "Medium",
    tags: ["Reasoning", "New"],
  },
];

export const DEFAULT_MODEL_ID = "llama-3.3-70b-versatile";
export const DEFAULT_PROVIDER_ID: ProviderId = "groq";

export function getModelsByProvider(provider: ProviderId): ModelConfig[] {
  return models.filter((m) => m.provider === provider);
}

export function findModel(modelId: string): ModelConfig | undefined {
  return models.find((m) => m.id === modelId);
}
