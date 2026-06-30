import { useTheme } from "../context/ThemeContext";

function ProfileCard({ developer }) {
    const { theme } = useTheme();

    return (
        <div
            className={`card ${theme === "dark" ? "card-dark" : ""
                }`}
        >
            <img
                src={developer.image}
                alt={developer.name}
                className="profile-image"
            />

            <h2>{developer.name}</h2>

            <h3>{developer.role}</h3>

            <p>
                <strong>📍 Location:</strong>{" "}
                {developer.location}
            </p>

            <p>
                <strong>📧 Email:</strong>{" "}
                {developer.email}
            </p>

            <p>
                <strong>💼 Experience:</strong>{" "}
                {developer.experience}
            </p>

            <p className="about">
                {developer.about}
            </p>

            <h4>Skills</h4>

            <div className="skills">

                {developer.skills.map((skill) => (
                    <span
                        key={skill}
                        className="skill"
                    >
                        {skill}
                    </span>
                ))}

            </div>

            <a
                href={developer.github}
                target="_blank"
                rel="noreferrer"
                className="github-btn"
            >
                View GitHub
            </a>
        </div>
    );
}

export default ProfileCard;