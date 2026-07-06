export interface Quote {
  id: number;
  quote: string;
  author: string;
}

export const quotes: Quote[] = [
  {
    id: 1,
    quote: "Stay hungry, stay foolish.",
    author: "Steve Jobs",
  },

  {
    id: 2,
    quote: "Programs must be written for people to read.",
    author: "Harold Abelson",
  },

  {
    id: 3,
    quote: "Code is like humor. When you have to explain it, it's bad.",
    author: "Cory House",
  },

  {
    id: 4,
    quote: "First, solve the problem. Then, write the code.",
    author: "John Johnson",
  },

  {
    id: 5,
    quote: "The best error message is the one that never shows up.",
    author: "Thomas Fuchs",
  },

  {
    id: 6,
    quote: "Learning never exhausts the mind.",
    author: "Leonardo da Vinci",
  },
];