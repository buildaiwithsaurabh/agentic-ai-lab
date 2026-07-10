import { streamText, UIMessage, convertToModelMessages } from "ai";
import { getProviderModel } from "../../lib/providers";
import { DEFAULT_MODEL_ID, DEFAULT_PROVIDER_ID, findModel } from "../../lib/models";
import type { ProviderId } from "../../lib/providers";

export const maxDuration = 30;

export async function POST(req: Request) {
  try {
    const {
      messages,
      modelId,
      providerId,
    }: { messages: UIMessage[]; modelId?: string; providerId?: string } =
      await req.json();

    const resolvedModelId = modelId ?? DEFAULT_MODEL_ID;
    const resolvedProviderId = (providerId as ProviderId) ?? DEFAULT_PROVIDER_ID;

    // Validate the model exists in our registry
    const modelConfig = findModel(resolvedModelId);
    if (!modelConfig) {
      return Response.json(
        { error: `Unknown model: ${resolvedModelId}` },
        { status: 400 }
      );
    }

    const model = getProviderModel(resolvedProviderId, resolvedModelId);

    const result = streamText({
      model,
      messages: convertToModelMessages(messages),
      system: `You are a helpful AI assistant. You are currently running as ${modelConfig.name} (${resolvedProviderId}).`,
    });

    return result.toUIMessageStreamResponse();
  } catch (error) {
    console.error("Chat API Error:", error);
    return Response.json(
      { error: "Something went wrong." },
      { status: 500 }
    );
  }
}
