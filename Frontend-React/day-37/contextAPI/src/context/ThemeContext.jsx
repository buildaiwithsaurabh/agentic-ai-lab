import { createContext, useContext, useState } from "react";

// Create Context
const ThemeContext = createContext();

// Custom Hook
export function useTheme() {
    return useContext(ThemeContext);
}

// Provider Component
export function ThemeProvider({ children }) {
    const [theme, setTheme] = useState("light");

    function toggleTheme() {
        setTheme((prevTheme) =>
            prevTheme === "light" ? "dark" : "light"
        );
    }

    const value = {
        theme,
        toggleTheme,
    };

    return (
        <ThemeContext.Provider value={value}>
            <div className={theme}>
                {children}
            </div>
        </ThemeContext.Provider>
    );
}