import { useState } from "react";
import "./index.css";

function App() {
  const [name, setName] = useState("");
  const [students, setStudents] = useState([]);
  const [totalStudents, setTotalStudents] = useState(0);

  const addStudent = () => {
    if (name.trim() === "") {
      alert("Please enter student name");
      return;
    }

    setStudents([...students, name]);
    setTotalStudents(totalStudents + 1);
    setName("");
  };

  return (
    <div className="container">
      <h1>Student Registration Dashboard</h1>

      <div className="card">
        <h2>Total Students: {totalStudents}</h2>

        <input
          type="text"
          placeholder="Enter student name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <button onClick={addStudent}>
          Add Student
        </button>

        <h3>Registered Students</h3>

        <ul>
          {students.map((student, index) => (
            <li key={index}>
              {student}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;