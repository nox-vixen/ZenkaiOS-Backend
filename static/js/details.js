// ===================================
// GET ANIME ID
// ===================================

const animeId =
window.location.pathname.split("/").pop();

// ===================================
// ELEMENTS
// ===================================

const bannerImage =
document.getElementById("bannerImage");

const posterImage =
document.getElementById("posterImage");

const animeTitle =
document.getElementById("animeTitle");

const animeJapanese =
document.getElementById("animeJapanese");

const animeMeta =
document.getElementById("animeMeta");

const synopsisText =
document.getElementById("synopsisText");

const genreSection =
document.getElementById("genreSection");

const backButton =
document.getElementById("backButton");

// ===================================

backButton.onclick=()=>history.back();

// ===================================

loadAnime();

// ===================================

async function loadAnime(){

try{

const res=

await fetch(

`https://api.jikan.moe/v4/anime/${animeId}/full`

);

const json=

await res.json();

const anime=json.data;

bannerImage.src=

anime.images.jpg.large_image_url;

if(anime.trailer.image_url){

bannerImage.src=

anime.trailer.image_url;

}

posterImage.src=

anime.images.jpg.large_image_url;

animeTitle.innerText=

anime.title;

animeJapanese.innerText=

anime.title_japanese || "";

animeMeta.innerHTML=

`
⭐ ${anime.score || "N/A"}

•

${anime.status}

•

${anime.episodes || "?"} Episodes

•

${anime.year || ""}
`;

synopsisText.innerText=

anime.synopsis ||

"No synopsis available.";

genreSection.innerHTML="";

anime.genres.forEach(g=>{

genreSection.innerHTML+=

`

<div class="genre">

${g.name}

</div>

`;

});

}catch(e){

animeTitle.innerText=

"Failed to load anime.";

console.log(e);

}

}
// ===================================
// CINEMATIC HERO
// ===================================

const heroBanner =
document.getElementById("heroBanner");

const posterSection =
document.getElementById("posterSection");

window.addEventListener(

"scroll",

()=>{

const y=

window.scrollY;

if(y<180){

heroBanner.style.height=

340-y+"px";

posterSection.style.transform=

`translateY(${-y*0.25}px)`;

}else{

heroBanner.style.height=

"160px";

posterSection.style.transform=

"translateY(-45px)";

}

}

);
