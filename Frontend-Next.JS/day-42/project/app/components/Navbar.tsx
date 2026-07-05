import Link from "next/link";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="logo">
        <h2>GitHub Dashboard</h2>
        <p>Next.js Data Fetching</p>
      </div>

      <nav className="nav-links">
        <Link href="/">Home</Link>

        <Link
          href="https://github.com"
          target="_blank"
        >
          GitHub
        </Link>
      </nav>
    </header>
  );
}