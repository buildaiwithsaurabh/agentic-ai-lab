import Chat from "./components/Chat";

export default function HomePage() {
  return (
    <main className="container">

      <section className="hero">

        <h1>

          🤖 AI Chat Assistant

        </h1>

        <p>

          My first AI application built with

          Next.js 16,

          AI SDK,

          and Groq.

        </p>

      </section>

      <Chat />

    </main>
  );
}