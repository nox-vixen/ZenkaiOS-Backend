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

const res = await fetch(`/api/details/${animeId}`);

if (!res.ok) {
    throw new Error("HTTP " + res.status);
}

const anime = await res.json();

bannerImage.src = anime.bannerImage || anime.coverImage;

// Keep the banner if available; otherwise use the cover image.

posterImage.src = anime.coverImage;

animeTitle.innerText=

anime.title;

animeJapanese.innerText = "";

animeMeta.innerHTML = `
⭐ ${anime.rating || "N/A"}
•
${anime.status || ""}
•
${anime.episodes || "?"} Episodes
•
${anime.year || ""}
`;

const synopsis =
anime.description || "No synopsis available.";

synopsisText.innerHTML = synopsis;
synopsisText.classList.add("collapsed");

const readMore =
document.getElementById("readMore");

if(synopsis.replace(/<[^>]*>/g,"").length < 380){

    readMore.style.display = "none";

}else{

    readMore.style.display = "inline-block";

}

genreSection.innerHTML="";

anime.genres.forEach(g => {

genreSection.innerHTML += `

<div class="genre">

${g}

</div>

`;

});

}catch(e){

animeTitle.innerText = "Failed to load anime.";

console.error("Anime fetch failed:", e);

alert("Anime fetch failed:\n" + e);

}

}
// ===================================
// CINEMATIC HERO
// ===================================

const heroBanner =
document.getElementById("heroBanner");

const posterSection =
document.getElementById("posterSection");

// ===================================
// Ultra Smooth Cinematic Hero
// ===================================

let ticking = false;

// ===================================
// READ MORE / READ LESS
// ===================================

const readMoreButton =
document.getElementById("readMore");

let synopsisExpanded = false;

readMoreButton.addEventListener("click",()=>{

    if(!synopsisExpanded){

        synopsisText.style.maxHeight = "3000px";

        readMoreButton.innerText = "Read Less";

        synopsisText.classList.remove("collapsed");

        synopsisExpanded = true;

    }else{

        synopsisText.style.maxHeight = "145px";

        readMoreButton.innerText = "Read More";

        synopsisText.classList.add("collapsed");

        synopsisExpanded = false;

    }

});
