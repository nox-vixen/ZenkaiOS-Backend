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

const trailerSection =
document.getElementById("trailerSection");

const trailerCard =
document.getElementById("trailerCard");

const trailerImage =
document.getElementById("trailerImage");

const infoScore =
document.getElementById("infoScore");

const infoEpisodes =
document.getElementById("infoEpisodes");

const infoStudio =
document.getElementById("infoStudio");

const infoSource =
document.getElementById("infoSource");

const infoSeason =
document.getElementById("infoSeason");

const infoStatus =
document.getElementById("infoStatus");

const infoFormat =
document.getElementById("infoFormat");

const infoDuration =
document.getElementById("infoDuration");

const characterCarousel =
document.getElementById("characterCarousel");

// ===================================

backButton.onclick=()=>history.back();

// ===================================

loadAnime();

loadCharacters();

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

// ===================================
// TRAILER
// ===================================

if(anime.trailer && anime.trailer.id){

    trailerImage.src =
    `https://img.youtube.com/vi/${anime.trailer.id}/maxresdefault.jpg`;

    trailerCard.onclick = () => {

        window.open(

            `https://www.youtube.com/watch?v=${anime.trailer.id}`,

            "_blank"

        );

    };

}else{

    trailerSection.style.display = "none";

}

// ===================================
// ANIME INFORMATION
// ===================================

infoScore.innerText =
anime.rating
? anime.rating + "/100"
: "N/A";

infoEpisodes.innerText =
anime.episodes || "Unknown";

infoStudio.innerText =
anime.studios && anime.studios.length
? anime.studios.join(", ")
: "Unknown";

infoSource.innerText =
anime.source || "Unknown";

infoSeason.innerText =
anime.season && anime.year
? `${anime.season} ${anime.year}`
: (anime.year || "Unknown");

const status =
anime.status || "Unknown";

let statusClass = "";

switch(status.toUpperCase()){

case "RELEASING":

statusClass = "status-releasing";

break;

case "FINISHED":

statusClass = "status-finished";

break;

case "NOT_YET_RELEASED":

statusClass = "status-notyet";

break;

case "HIATUS":

statusClass = "status-hiatus";

break;

case "CANCELLED":

statusClass = "status-cancelled";

break;

}

infoStatus.innerHTML =

`<span class="statusBadge ${statusClass}">

${status}

</span>`;

infoFormat.innerText =
anime.format || "Unknown";

infoDuration.innerText =
anime.duration
? anime.duration + " min"
: "Unknown";

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

// ===================================
// LOAD CHARACTERS
// ===================================

async function loadCharacters(){

    try{

        const res = await fetch(

            `/api/details/${animeId}/characters`

        );

        if(!res.ok){

            throw new Error("Failed");

        }

        const characters = await res.json();

        characterCarousel.innerHTML = "";

        characters.forEach(character=>{

            characterCarousel.innerHTML += `

            <div class="characterCard">

                <img

                    class="characterImage"

                    src="${character.image}"

                    alt="${character.name}"

                    loading="lazy">

                <div class="characterName">

                    ${character.name}

                </div>

                <div class="voiceActor">

                    ${character.voiceActor || "Unknown Voice Actor"}

                </div>

            </div>

            `;

        });

    }catch(e){

        console.error(e);

        characterCarousel.innerHTML =

        "<p style='color:#888'>Unable to load characters.</p>";

    }

}
