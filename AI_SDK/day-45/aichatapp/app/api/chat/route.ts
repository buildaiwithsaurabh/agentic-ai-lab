import { streamText, UIMessage, convertToModelMessages } from "ai";
import { model } from "@/app/lib/ai";

export const maxDuration = 30;

export async function POST(req: Request) {
  try {
    const { messages }: { messages: UIMessage[] } = await req.json();

    const result = streamText({
      model,
      messages: convertToModelMessages(messages),
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
