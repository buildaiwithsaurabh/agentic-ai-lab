import "./globals.css";
import type { Metadata } from "next";

import Navbar from "./components/Navbar";

export const metadata: Metadata = {
  title: "AI Chat Assistant",

  description:
    "Next.js 16 + AI SDK + Groq",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">

      <body>

        <Navbar />

        {children}

      </body>

    </html>
  );
}