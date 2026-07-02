import Link from "next/link";

export default function Navbar() {
  return (
    <header className="navbar">

      <div className="logo">
        <h2>Next.js Learning</h2>
        <p>Day 39 • App Router</p>
      </div>

      <nav className="nav-links">
        <Link href="/">Home</Link>
        <Link href="/about">About</Link>
        <Link href="/projects">Projects</Link>
        <Link href="/contact">Contact</Link>
      </nav>

    </header>
  );
}