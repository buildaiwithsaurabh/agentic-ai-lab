import { notFound } from "next/navigation";
import Link from "next/link";

import { developers } from "../../data/developers";

interface Props {
    params: {
        id: string;
    };
}

export async function generateStaticParams() {
    return developers.map((developer) => ({
        id: developer.id.toString(),
    }));
}

export default function DeveloperDetails({
    params,
}: Props) {

    const developer = developers.find(
        (item) => item.id === Number(params.id)
    );

    if (!developer) {
        notFound();
    }

    return (
        <main className="container">

            <div className="details">

                <img
                    src={developer.image}
                    alt={developer.name}
                />

                <h1>{developer.name}</h1>

                <h3>{developer.role}</h3>

                <br />

                <p>

                    <strong>Location:</strong>{" "}
                    {developer.location}

                </p>

                <br />

                <p>

                    <strong>Experience:</strong>{" "}
                    {developer.experience}

                </p>

                <br />

                <p>{developer.about}</p>

                <br />

                <h2>Skills</h2>

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

                <br />

                <Link
                    href="/developers"
                    className="button"
                >
                    ← Back to Developers
                </Link>

            </div>

        </main>
    );
}