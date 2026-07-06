export interface Developer {
  id: number;
  name: string;
  role: string;
  experience: string;
  location: string;
  skills: string[];
}

export const developers: Developer[] = [
  {
    id: 1,
    name: "Saurabh Kumar",
    role: "Full Stack GenAI Engineer",
    experience: "2 Years",
    location: "Bhopal, India",
    skills: [
      "React",
      "Next.js",
      "TypeScript",
      "Python",
      "FastAPI",
      "PostgreSQL",
    ],
  },

  {
    id: 2,
    name: "John Carter",
    role: "Frontend Developer",
    experience: "4 Years",
    location: "New York, USA",
    skills: [
      "React",
      "Next.js",
      "Tailwind CSS",
      "Redux",
      "JavaScript",
    ],
  },

  {
    id: 3,
    name: "Emma Watson",
    role: "Backend Engineer",
    experience: "5 Years",
    location: "London, UK",
    skills: [
      "Node.js",
      "Express",
      "FastAPI",
      "PostgreSQL",
      "Docker",
    ],
  },

  {
    id: 4,
    name: "Sophia Brown",
    role: "AI Engineer",
    experience: "3 Years",
    location: "Toronto, Canada",
    skills: [
      "Python",
      "OpenAI",
      "Gemini",
      "LangChain",
      "RAG",
    ],
  },

  {
    id: 5,
    name: "David Wilson",
    role: "Cloud Engineer",
    experience: "6 Years",
    location: "Sydney, Australia",
    skills: [
      "AWS",
      "Docker",
      "Kubernetes",
      "Terraform",
      "Linux",
    ],
  },
];