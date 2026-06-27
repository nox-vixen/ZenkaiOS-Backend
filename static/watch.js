const API="https://zenkai-backend-7jrx.onrender.com";

const id=new URLSearchParams(location.search).get("id");

fetch(API+"/api/anime/"+id)

.then(r=>r.json())

.then(anime=>{

document.getElementById("loading").style.display="none";

document.getElementById("anime").style.display="block";

document.getElementById("banner").style.backgroundImage=`url(${anime.bannerImage})`;

document.getElementById("cover").src=anime.coverImage;

document.getElementById("title").textContent=anime.title;

document.getElementById("meta").innerHTML=`

⭐ ${anime.rating}

•

${anime.year}

•

${anime.format}

•

${anime.status}

`;

document.getElementById("description").innerHTML=anime.description;

const genres=document.getElementById("genres");

anime.genres.forEach(g=>{

const span=document.createElement("span");

span.className="genre";

span.textContent=g;

genres.appendChild(span);

});

});
