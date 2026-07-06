import Link from "next/link";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="logo">
        <h2>Developer API Dashboard</h2>
        <p>Next.js Route Handlers</p>
      </div>

      <nav className="nav-links">
        <Link href="/">Home</Link>

        <Link href="#quotes">
          Quotes API
        </Link>

        <Link href="#developers">
          Developers API
        </Link>
      </nav>
    </header>
  );
}