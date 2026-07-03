interface Props{
    title:string;
    value:string;
}

export default function StatsCard({
title,
value
}:Props){

return(

<div className="card">

<h2>{title}</h2>

<h1>{value}</h1>

</div>

)

}