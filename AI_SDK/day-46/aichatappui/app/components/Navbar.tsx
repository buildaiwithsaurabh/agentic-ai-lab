import { BotMessageSquare } from "lucide-react";

export default function Navbar() {
    return (
        <header className="navbar">
            <div className="logo">
                <h2>
                    <BotMessageSquare
                        size={28}
                        style={{ marginRight: "10px", verticalAlign: "middle" }}
                    />

                    AI Chat Assistant
                </h2>

                <p>
                    Next.js 16 • AI SDK 5 • Groq
                </p>
            </div>
        </header>
    );
}