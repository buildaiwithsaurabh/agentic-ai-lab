"use server";

import { feedbackList } from "../data/feedback";

export async function submitFeedback(
  formData: FormData
) {
  // Read form values
  const name = formData.get("name")?.toString().trim();
  const email = formData.get("email")?.toString().trim();
  const message = formData.get("message")?.toString().trim();

  // Validation
  if (!name || !email || !message) {
    console.log("❌ All fields are required.");
    return;
  }

  // Create new feedback object
  const newFeedback = {
    id: feedbackList.length + 1,
    name,
    email,
    message,
  };

  // Store in memory
  feedbackList.push(newFeedback);

  console.log("✅ Feedback Submitted");
  console.table(newFeedback);

  // Return response
  return {
    success: true,
    message: "Feedback submitted successfully.",
  };
}