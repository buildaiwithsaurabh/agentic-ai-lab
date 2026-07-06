export default function QuoteCard() {
  return (
    <div
      className="card"
      id="quotes"
    >
      <h2>💬 Quotes API</h2>

      <p>
        Learn how to build REST APIs using
        Next.js Route Handlers.
      </p>

      <br />

      <h3>Available Endpoints</h3>

      <br />

      <p>

        <strong>GET</strong>

      </p>

      <code>

        /api/quotes

      </code>

      <br />
      <br />

      <p>

        <strong>POST</strong>

      </p>

      <code>

        /api/quotes

      </code>

      <br />
      <br />

      <p>

        Returns JSON responses using
        <strong> NextResponse.json()</strong>

      </p>
    </div>
  );
}