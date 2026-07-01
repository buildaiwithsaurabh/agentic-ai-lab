"use strict";
// Primitive Types
Object.defineProperty(exports, "__esModule", { value: true });
let name = "Saurabh";
let age = 24;
let isDeveloper = true;
console.log(name);
console.log(age);
console.log(isDeveloper);
// Arrays
let skills = [
    "React",
    "TypeScript",
    "FastAPI",
    "Python"
];
console.log(skills);
// Object
let student = {
    id: 1,
    name: "Saurabh",
    course: "M.Tech"
};
console.log(student);
// Function
function greet(name) {
    return `Welcome ${name}`;
}
console.log(greet("Saurabh"));
// Union Types
let id;
id = 1001;
id = "EMP1001";
console.log(id);
// Literal Types
let role;
role = "Student";
console.log(role);
// any
let value = "Hello";
value = 100;
value = true;
console.log(value);
// unknown
let data = "TypeScript";
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
//# sourceMappingURL=index.js.map