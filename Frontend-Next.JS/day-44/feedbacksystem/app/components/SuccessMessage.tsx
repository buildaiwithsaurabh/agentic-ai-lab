export default function SuccessMessage() {
  return (
    <div className="success-message">
      ✅ This form uses a <strong>Next.js Server Action</strong>.
      <br />
      After implementing the Server Action,
      feedback will be processed directly on
      the server without calling an API Route.
    </div>
  );
}