import { useState } from "react";
import "./index.css";

function App() {
  const [employee, setEmployee] = useState("");
  const [employees, setEmployees] = useState([]);

  const addEmployee = () => {
    if (!employee.trim()) return;

    setEmployees([...employees, employee]);
    setEmployee("");
  };

  return (
    <div className="container">
      <h1>Employee Directory Dashboard</h1>

      <div className="card">
        <input
          type="text"
          placeholder="Enter Employee Name"
          value={employee}
          onChange={(e) =>
            setEmployee(e.target.value)
          }
        />

        <button onClick={addEmployee}>
          Add Employee
        </button>

        <h3>
          Total Employees:
          {employees.length}
        </h3>

        {employees.length === 0 ? (
          <p>No Employees Found</p>
        ) : (
          <ul>
            {employees.map(
              (employee, index) => (
                <li key={index}>
                  {employee}
                </li>
              )
            )}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;