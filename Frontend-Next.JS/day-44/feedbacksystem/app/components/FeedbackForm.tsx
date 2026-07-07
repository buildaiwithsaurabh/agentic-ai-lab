import { submitFeedback } from "../actions/feedback";
import SuccessMessage from "./SuccessMessage";

export default function FeedbackForm() {
  return (
    <div className="card" id="feedback">
      <h2>📝 Submit Feedback</h2>

      <p>
        Fill out the form below.
        The form submission is handled using a Next.js Server Action.
      </p>

      <br />

      <form action={submitFeedback}>
        <input
          type="text"
          name="name"
          placeholder="Enter your name"
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Enter your email"
          required
        />

        <textarea
          name="message"
          placeholder="Write your feedback..."
          required
        />

        <button type="submit">
          Submit Feedback
        </button>
      </form>

      <br />

      <SuccessMessage />
    </div>
  );
}