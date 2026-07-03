"use client";

import { useState } from "react";

export default function Counter(){

const [count,setCount]=useState(0);

return(

<div className="counter">

<h2>Counter</h2>

<h1>{count}</h1>

<button
onClick={()=>setCount(count+1)}
>

Increase

</button>

</div>

)

}