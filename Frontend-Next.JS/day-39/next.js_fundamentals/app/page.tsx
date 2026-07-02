import Link from "next/link";

export default function HomePage() {
  return (
    <main className="container">

      <section className="hero">

        <h1>🚀 Welcome to My Next.js Journey</h1>

        <p>
          This project marks the beginning of my journey with
          <strong> Next.js App Router</strong>.
        </p>

        <p>
          Today, I explored the core concepts that make Next.js one of the
          most popular React frameworks for building production-ready
          applications.
        </p>

      </section>

      <section className="topics">

        <h2>📚 Topics Covered</h2>

        <ul>
          <li>✅ What is Next.js?</li>
          <li>✅ Why Next.js?</li>
          <li>✅ App Router</li>
          <li>✅ File-Based Routing</li>
          <li>✅ Layouts</li>
          <li>✅ Link Component</li>
          <li>✅ Metadata API</li>
          <li>✅ Project Structure</li>
        </ul>

      </section>

      <section className="navigation">

        <h2>🔗 Explore Pages</h2>

        <div className="buttons">

          <Link href="/about" className="btn">
            About
          </Link>

          <Link href="/projects" className="btn">
            Projects
          </Link>

          <Link href="/contact" className="btn">
            Contact
          </Link>

        </div>

      </section>

      <section className="roadmap">

        <h2>🎯 Learning Roadmap</h2>

        <p>
          My goal is to become a <strong>Full-Stack GenAI Engineer</strong>
          by mastering modern web development and AI technologies.
        </p>

        <ul>
          <li>✅ Python Fundamentals</li>
          <li>✅ FastAPI</li>
          <li>✅ React</li>
          <li>✅ TypeScript Basics</li>
          <li>▶ Next.js (Current)</li>
          <li>⏳ Supabase</li>
          <li>⏳ Vercel AI SDK</li>
          <li>⏳ OpenAI / Gemini / Groq APIs</li>
          <li>⏳ RAG</li>
          <li>⏳ AI Agents</li>
          <li>⏳ Agentic AI</li>
        </ul>

      </section>

    </main>
  );
}