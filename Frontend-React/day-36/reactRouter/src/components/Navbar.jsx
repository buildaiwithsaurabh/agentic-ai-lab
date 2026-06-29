import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <h2>🤖 Cyber Agent</h2>

      <div className="links">
        <NavLink to="/">Home</NavLink>

        <NavLink to="/about">About</NavLink>

        <NavLink to="/destinations">Destinations</NavLink>
      </div>
    </nav>
  );
}

export default Navbar;