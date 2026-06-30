import { useTheme } from "../context/ThemeContext";

function Navbar() {
    const { theme, toggleTheme } = useTheme();

    return (
        <nav className="navbar">
            <div>
                <h2>Developer Directory</h2>
                <p>React Context API Demo</p>
            </div>

            <button
                className="theme-btn"
                onClick={toggleTheme}
            >
                {theme === "light"
                    ? "🌙 Dark Mode"
                    : "☀️ Light Mode"}
            </button>
        </nav>
    );
}

export default Navbar;