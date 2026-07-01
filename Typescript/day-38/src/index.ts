// Primitive Types

let name: string = "Saurabh";

let age: number = 24;

let isDeveloper: boolean = true;

console.log(name);
console.log(age);
console.log(isDeveloper);

// Arrays

let skills: string[] = [
  "React",
  "TypeScript",
  "FastAPI",
  "Python"
];

console.log(skills);

// Object

let student: {
  id: number;
  name: string;
  course: string;
} = {
  id: 1,
  name: "Saurabh",
  course: "M.Tech"
};

console.log(student);

// Function

function greet(name: string): string {
  return `Welcome ${name}`;
}

console.log(greet("Saurabh"));

// Union Types

let id: number | string;

id = 1001;

id = "EMP1001";

console.log(id);

// Literal Types

let role: "Admin" | "Student" | "Teacher";

role = "Student";

console.log(role);

// any

let value: any = "Hello";

value = 100;

value = true;

console.log(value);

// unknown

let data: unknown = "TypeScript";

if (typeof data === "string") {
  console.log(data.toUpperCase());
}

// Type Inference

let city = "Bhopal";

let salary = 10.5;

let active = true;

console.log(city);
console.log(salary);
console.log(active);