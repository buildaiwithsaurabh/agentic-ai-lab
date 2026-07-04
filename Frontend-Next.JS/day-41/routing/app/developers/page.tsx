import DeveloperCard from "../components/DeveloperCard";
import { developers } from "../data/developers";

export default function DevelopersPage() {
    return (
        <main className="container">

            <section className="hero">

                <h1>Developer Directory</h1>

                <p>
                    Click on any developer to explore their
                    complete profile using Dynamic Routing.
                </p>

            </section>

            <section className="grid">

                {developers.map((developer) => (

                    <DeveloperCard
                        key={developer.id}
                        developer={developer}
                    />

                ))}

            </section>

        </main>
    );
}