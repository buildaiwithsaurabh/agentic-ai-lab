import FeedbackForm from "./components/FeedbackForm";
import FeedbackList from "./components/FeedbackList";

export default function HomePage() {
  return (
    <main className="container">

      <section className="hero">

        <h1>
          🚀 Feedback Management System
        </h1>

        <p>

          Learn how to use Server Actions
          for handling forms in Next.js.

        </p>

      </section>

      <section className="grid">

        <div className="card">

          <h2>

            📚 Topics Covered

          </h2>

          <ul>

            <li>✅ Server Actions</li>

            <li>✅ "use server"</li>

            <li>✅ Form Submission</li>

            <li>✅ FormData</li>

            <li>✅ Validation</li>

            <li>✅ Server-side Logic</li>

          </ul>

          <br />

          <p>

            This project demonstrates how
            forms can directly invoke
            server-side functions without
            creating API Routes.

          </p>

        </div>

        <FeedbackForm />

      </section>

      <br />
      <br />

      <FeedbackList />

    </main>
  );
}