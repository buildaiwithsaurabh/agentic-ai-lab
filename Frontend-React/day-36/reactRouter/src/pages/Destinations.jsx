const worlds = [
  "Neo Tokyo",
  "Quantum Forest",
  "Cyber Castle",
  "AI Academy",
  "Robot Kingdom",
  "Galaxy Hub"
];

function Destinations() {
  return (
    <div className="page">
      <h1>🌍 Cyber Worlds</h1>

      <div className="grid">
        {worlds.map((world) => (
          <div className="card" key={world}>
            <h2>{world}</h2>

            <p>
              Explore this futuristic destination with your intelligent AI
              partner.
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Destinations;