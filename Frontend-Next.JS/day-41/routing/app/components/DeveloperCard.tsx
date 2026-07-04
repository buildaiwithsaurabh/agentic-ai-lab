import Link from "next/link";

interface Developer {
    id: number;
    name: string;
    role: string;
    location: string;
    experience: string;
    image: string;
    skills: string[];
}

interface Props {
    developer: Developer;
}

export default function DeveloperCard({
    developer,
}: Props) {
    return (
        <div className="card">
            <img
                src={developer.image}
                alt={developer.name}
            />

            <h2>{developer.name}</h2>

            <h3>{developer.role}</h3>

            <p>
                <strong>Location:</strong>{" "}
                {developer.location}
            </p>

            <p>
                <strong>Experience:</strong>{" "}
                {developer.experience}
            </p>

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

            <Link
                href={`/developers/${developer.id}`}
                className="btn"
            >
                View Profile
            </Link>
        </div>
    );
}