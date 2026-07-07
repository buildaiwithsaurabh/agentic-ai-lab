import Link from "next/link";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="logo">
        <h2>Feedback Management</h2>
        <p>Next.js Server Actions</p>
      </div>

      <nav className="nav-links">
        <Link href="/">Home</Link>

        <Link href="#feedback">
          Feedback Form
        </Link>

        <Link href="#submitted">
          Submitted Feedback
        </Link>
      </nav>
    </header>
  );
}