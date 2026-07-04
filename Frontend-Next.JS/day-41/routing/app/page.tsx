import Link from "next/link";

export default function HomePage() {
  return (
    <main className="container">

      <section className="hero">

        <h1>
          🚀 Next.js Dynamic Routing
        </h1>

        <p>

          Welcome to Day 41 of my Next.js learning journey.

        </p>

        <p>

          Today I'm learning how Next.js creates dynamic pages
          using the App Router.

        </p>

        <Link
          href="/developers"
          className="button"
        >

          Explore Developers →

        </Link>

      </section>

      <section>

        <h2>

          Topics Covered

        </h2>

        <br />

        <ul>

          <li>✅ Dynamic Routing</li>

          <li>✅ Dynamic Segments</li>

          <li>✅ params</li>

          <li>✅ generateStaticParams()</li>

          <li>✅ Link</li>

          <li>✅ Navigation</li>

        </ul>

      </section>

    </main>
  );
}