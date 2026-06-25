import { useState } from "react";
import "./index.css";

function App() {
  const [studentName, setStudentName] = useState("");
  const [search, setSearch] = useState("");

  const [students, setStudents] = useState([]);

  const addStudent = () => {
    if (!studentName.trim()) {
      alert("Student name is required");
      return;
    }

    const newStudent = {
      id: crypto.randomUUID(),
      name: studentName
    };

    setStudents([...students, newStudent]);

    setStudentName("");
  };

  const filteredStudents = students.filter((student) =>
    student.name
      .toLowerCase()
      .includes(search.toLowerCase())
  );

  return (
    <div className="container">

      <h1>Student Management System</h1>

      <div className="card">

        <input
          type="text"
          placeholder="Student Name"
          value={studentName}
          onChange={(e) =>
            setStudentName(e.target.value)
          }
        />

        <button onClick={addStudent}>
          Register
        </button>

        <hr />

        <input
          type="text"
          placeholder="Search Student"
          value={search}
          onChange={(e) =>
            setSearch(e.target.value)
          }
        />

        <h3>
          Students : {students.length}
        </h3>

        {
          filteredStudents.length === 0
          ? (
            <p>No Student Found</p>
          )
          : (
            <ul>

              {
                filteredStudents.map((student) => (

                  <li key={student.id}>
                    {student.name}
                  </li>

                ))
              }

            </ul>
          )
        }

      </div>

    </div>
  );
}

export default App;