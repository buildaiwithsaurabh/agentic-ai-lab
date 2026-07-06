import QuoteCard from "./components/QuoteCard";
import DeveloperCard from "./components/DeveloperCard";

export default function HomePage() {
  return (
    <main className="container">

      <section className="hero">

        <h1>
          🚀 Developer API Dashboard
        </h1>

        <p>

          Welcome to Day 43 of my Next.js learning journey.

        </p>

        <p>

          Today I'm learning how to build backend APIs
          using Next.js Route Handlers.

        </p>

      </section>

      <section className="section">

        <h2>
          📚 Topics Covered
        </h2>

        <div className="grid">

          <div className="card">

            <h2>Concepts</h2>

            <ul>

              <li>✅ Route Handlers</li>

              <li>✅ API Routes</li>

              <li>✅ GET Request</li>

              <li>✅ POST Request</li>

              <li>✅ Request</li>

              <li>✅ Response</li>

              <li>✅ NextResponse</li>

            </ul>

          </div>

          <QuoteCard />

          <DeveloperCard />

        </div>

      </section>

    </main>
  );
}