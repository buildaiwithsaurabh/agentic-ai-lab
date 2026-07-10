import { groq } from "@ai-sdk/groq";
import { google } from "@ai-sdk/google";
import { openai } from "@ai-sdk/openai";

export type ProviderId = "groq" | "google" | "openai";

// Use ReturnType inference — no need to import @ai-sdk/provider directly
type GroqModel   = ReturnType<typeof groq>;
type GoogleModel = ReturnType<typeof google>;
type OpenAIModel = ReturnType<typeof openai>;
export type AnyLanguageModel = GroqModel | GoogleModel | OpenAIModel;

export interface ProviderConfig {
  id: ProviderId;
  name: string;
  icon: string;
  color: string;
  getModel: (modelId: string) => AnyLanguageModel;
}

export const providers: Record<ProviderId, ProviderConfig> = {
  groq: {
    id: "groq",
    name: "Groq",
    icon: "⚡",
    color: "#f55036",
    getModel: (modelId: string) => groq(modelId),
  },
  google: {
    id: "google",
    name: "Google Gemini",
    icon: "✦",
    color: "#4285f4",
    getModel: (modelId: string) => google(modelId),
  },
  openai: {
    id: "openai",
    name: "OpenAI",
    icon: "◎",
    color: "#10a37f",
    getModel: (modelId: string) => openai(modelId),
  },
};

export function getProviderModel(
  providerId: ProviderId,
  modelId: string
): AnyLanguageModel {
  const provider = providers[providerId];
  if (!provider) {
    throw new Error(`Unknown provider: ${providerId}`);
  }
  return provider.getModel(modelId);
}
