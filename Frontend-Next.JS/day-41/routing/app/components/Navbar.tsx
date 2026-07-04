import Link from "next/link";

export default function Navbar() {
    return (
        <header className="navbar">
            <div className="logo">
                <h2>Developer Directory</h2>
                <p>Next.js Dynamic Routing</p>
            </div>

            <nav className="nav-links">
                <Link href="/">Home</Link>

                <Link href="/developers">
                    Developers
                </Link>
            </nav>
        </header>
    );
}