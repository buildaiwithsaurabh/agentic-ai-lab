interface GitHubUser {
  id: number;
  login: string;
  avatar_url: string;
  html_url: string;
}

interface UserCardProps {
  user: GitHubUser;
}

export default function UserCard({
  user,
}: UserCardProps) {
  return (
    <div className="card">
      <img
        src={user.avatar_url}
        alt={user.login}
      />

      <h2>{user.login}</h2>

      <p>GitHub Developer</p>

      <a
        href={user.html_url}
        target="_blank"
        rel="noreferrer"
        className="btn"
      >
        View Profile
      </a>
    </div>
  );
}