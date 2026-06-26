import { useEffect, useState } from "react";
import "./index.css";

function App() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetchUsers();
  }, []);

  async function fetchUsers() {
    try {
      const response = await fetch(
        "https://jsonplaceholder.typicode.com/users"
      );

      if (!response.ok) {
        throw new Error("Failed to fetch users");
      }

      const data = await response.json();
      setUsers(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  if (loading) {
    return <h2 className="status">Loading Users...</h2>;
  }

  if (error) {
    return <h2 className="status">{error}</h2>;
  }

  return (
    <div className="container">
      <h1>User Directory Dashboard</h1>

      <div className="grid">
        {users.map((user) => (
          <div className="card" key={user.id}>
            <h2>{user.name}</h2>

            <p>
              <strong>Username:</strong> {user.username}
            </p>

            <p>
              <strong>Email:</strong> {user.email}
            </p>

            <p>
              <strong>Phone:</strong> {user.phone}
            </p>

            <p>
              <strong>Website:</strong> {user.website}
            </p>

            <p>
              <strong>Company:</strong> {user.company.name}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;