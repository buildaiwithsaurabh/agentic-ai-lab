import img1 from "../assets/img1.jpg";

function ProfileCard(props) {
  return (
    <div className="card">
      <img
        src={img1}
        alt="profile"
        className="profile-image"
      />

      <h2>{props.name}</h2>

      <p>{props.description}</p>

      <div className="info">
        <p>
          <strong>Location:</strong> {props.location}
        </p>

        <p>
          <strong>Email:</strong> {props.email}
        </p>
      </div>

      <a
        href={props.github}
        target="_blank"
        rel="noreferrer"
        className="github-btn"
      >
        View GitHub Profile
      </a>
    </div>
  );
}

export default ProfileCard;