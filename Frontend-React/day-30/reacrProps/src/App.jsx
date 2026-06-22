import ProfileCard from "./components/ProfileCard";

function App() {
  return (
    <div className="container">
      <h1>Day 30 - React Fundamentals</h1>
      <h2>Props in React</h2>

      <ProfileCard
        name="Saurabh Kumar Pandey"
        description="Passionate about building AI-powered applications and solving real-world problems."
        location="India"
        email="saurabh@example.com"
        github="https://github.com/buildaiwithsaurabh"
      />
    </div>
  );
}

export default App;