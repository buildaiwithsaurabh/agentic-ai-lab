import { NextResponse } from "next/server";
import { quotes } from "@/app/data/quotes";

// ===================================
// GET /api/quotes
// ===================================

export async function GET() {
  return NextResponse.json({
    success: true,
    message: "Quotes fetched successfully.",
    total: quotes.length,
    data: quotes,
  });
}

// ===================================
// POST /api/quotes
// ===================================

export async function POST(request: Request) {
  try {
    const body = await request.json();

    if (!body.quote || !body.author) {
      return NextResponse.json(
        {
          success: false,
          message: "Quote and author are required.",
        },
        {
          status: 400,
        }
      );
    }

    const newQuote = {
      id: quotes.length + 1,
      quote: body.quote,
      author: body.author,
    };

    quotes.push(newQuote);

    return NextResponse.json(
      {
        success: true,
        message: "Quote created successfully.",
        data: newQuote,
      },
      {
        status: 201,
      }
    );
  } catch {
    return NextResponse.json(
      {
        success: false,
        message: "Invalid request body.",
      },
      {
        status: 400,
      }
    );
  }
}