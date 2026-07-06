import { NextResponse } from "next/server";
import { developers } from "@/app/data/developers";

// ===================================
// GET /api/developers
// ===================================

export async function GET() {
  return NextResponse.json({
    success: true,
    message: "Developers fetched successfully.",
    total: developers.length,
    data: developers,
  });
}