import { Link } from "react-router-dom";

function NotFound() {
  return (
    <div className="page">
      <h1>404 🚫</h1>

      <h2>Portal Not Found</h2>

      <p>
        The AI Agent could not locate this dimension.
      </p>

      <Link to="/">Return Home</Link>
    </div>
  );
}

export default NotFound;