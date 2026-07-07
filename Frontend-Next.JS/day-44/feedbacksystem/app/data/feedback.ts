export interface Feedback {
  id: number;
  name: string;
  email: string;
  message: string;
}

export const feedbackList: Feedback[] = [
  {
    id: 1,
    name: "John Doe",
    email: "john@example.com",
    message:
      "Excellent explanation of Server Actions!",
  },
  {
    id: 2,
    name: "Sarah Smith",
    email: "sarah@example.com",
    message:
      "The project structure is easy to understand.",
  },
];