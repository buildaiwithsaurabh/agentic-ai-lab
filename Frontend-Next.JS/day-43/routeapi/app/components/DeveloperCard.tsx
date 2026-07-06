export default function DeveloperCard() {
  return (
    <div
      className="card"
      id="developers"
    >
      <h2>👨‍💻 Developers API</h2>

      <p>
        Retrieve developer information
        through Route Handlers.
      </p>

      <br />

      <h3>Available Endpoint</h3>

      <br />

      <p>

        <strong>GET</strong>

      </p>

      <code>

        /api/developers

      </code>

      <br />
      <br />

      <h3>Example Response</h3>

      <br />

      <pre>
{`[
  {
    "id":1,
    "name":"Saurabh",
    "role":"Full Stack GenAI Engineer"
  }
]`}
      </pre>
    </div>
  );
}