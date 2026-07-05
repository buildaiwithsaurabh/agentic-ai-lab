import UserCard from "./components/UserCard";

interface GitHubUser {

  id:number;

  login:string;

  avatar_url:string;

  html_url:string;

}

async function getUsers(){

  const response = await fetch(

    "https://api.github.com/users",

    {
      cache:"no-store"
    }

  );

  if(!response.ok){

    throw new Error("Failed to fetch users");

  }

  return response.json();

}

export default async function HomePage(){

  const users:GitHubUser[] = await getUsers();

  return(

    <main className="container">

      <section className="hero">

        <h1>

          🚀 GitHub Developer Dashboard

        </h1>

        <p>

          Learning Server Side Data Fetching
          in Next.js App Router

        </p>

      </section>

      <section className="grid">

        {

          users.slice(0,12).map((user)=>(

            <UserCard

              key={user.id}

              user={user}

            />

          ))

        }

      </section>

    </main>

  )

}