import { feedbackList } from "../data/feedback";

export default function FeedbackList() {
  return (
    <section
      className="card"
      id="submitted"
    >
      <h2>📋 Submitted Feedback</h2>

      <p>
        Feedback stored in our temporary
        data layer.
      </p>

      <br />

      {feedbackList.length === 0 ? (
        <p>No feedback available.</p>
      ) : (
        feedbackList.map((feedback) => (
          <div
            key={feedback.id}
            className="feedback-item"
          >
            <h3>{feedback.name}</h3>

            <p>
              <strong>Email:</strong>{" "}
              {feedback.email}
            </p>

            <p>
              <strong>Message:</strong>{" "}
              {feedback.message}
            </p>
          </div>
        ))
      )}
    </section>
  );
}