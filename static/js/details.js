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

synopsisText.innerHTML =
anime.description || "No synopsis available.";

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

window.addEventListener("scroll", () => {

    if (!ticking) {

        window.requestAnimationFrame(() => {

            const y = window.scrollY;

            bannerImage.style.transform =
                `translateY(${y * 0.18}px) scale(1.08)`;

            posterSection.style.transform =
                `translateY(${-Math.min(y * 0.18, 35)}px)`;

            ticking = false;

        });

        ticking = true;

    }

});
