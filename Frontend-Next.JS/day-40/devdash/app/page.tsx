import Header from "./components/Header";
import StatsCard from "./components/StatsCard";
import Counter from "./components/Counter";
import Footer from "./components/Footer";

export default function Home(){

return(

<main>

<Header/>

<section className="grid">

<StatsCard
title="Projects"
value="12"
/>

<StatsCard
title="Commits"
value="145"
/>

<StatsCard
title="Learning Days"
value="40"
/>


</section>

<Counter/>

<Footer/>

</main>

)

}