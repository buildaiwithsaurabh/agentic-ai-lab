import Navbar from "./components/Navbar";
import ProfileCard from "./components/ProfileCard";

import developers from "./data/developers";

import { ThemeProvider } from "./context/ThemeContext";

import "./index.css";

function App() {
  return (
    <ThemeProvider>
      <Navbar />

      <main className="container">
        <h1 className="title">
          Developer Profile Directory
        </h1>

        <p className="subtitle">
          React Context API • Theme Switcher • Reusable Components
        </p>

        <div className="card-container">
          {developers.map((developer) => (
            <ProfileCard
              key={developer.id}
              developer={developer}
            />
          ))}
        </div>
      </main>
    </ThemeProvider>
  );
}

export default App;