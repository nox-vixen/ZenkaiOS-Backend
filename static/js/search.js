// ==========================
// ELEMENTS
// ==========================

const searchInput = document.getElementById("searchInput");

const clearSearch = document.getElementById("clearSearch");

const backBtn = document.getElementById("backBtn");

const recentList = document.getElementById("recentList");

const trendingList = document.getElementById("trendingList");

const genreChips = document.getElementById("genreChips");

const resultGrid = document.getElementById("resultGrid");

// ==========================
// STATIC DATA
// ==========================

const trending = [

"One Piece",

"Demon Slayer",

"Solo Leveling",

"Jujutsu Kaisen",

"Chainsaw Man",

"Blue Lock",

"Dandadan",

"Kaiju No.8"

];

const genres=[

"Action",

"Adventure",

"Comedy",

"Drama",

"Fantasy",

"Horror",

"Isekai",

"Mecha",

"Mystery",

"Romance",

"Sci-Fi",

"Sports"

];

// ==========================
// RECENT SEARCHES
// ==========================

let recent =

JSON.parse(

localStorage.getItem("zenkai_recent")

)||[];

// ==========================

renderRecent();

renderTrending();

renderGenres();

// ==========================

backBtn.onclick=()=>history.back();

// ==========================

searchInput.addEventListener("input",()=>{

const text=searchInput.value.trim();

clearSearch.style.display=

text.length?"block":"none";

if(text.length===0){

resultGrid.innerHTML="";

return;

}

searchAnime(text);

});

clearSearch.onclick=()=>{

searchInput.value="";

clearSearch.style.display="none";

resultGrid.innerHTML="";

searchInput.focus();

};

// ==========================

function renderRecent(){

recentList.innerHTML="";

if(recent.length===0){

recentList.innerHTML=

"<p style='color:#777'>No recent searches</p>";

return;

}

recent.forEach(item=>{

recentList.innerHTML+=`

<div class="genre-chip"

onclick="quickSearch('${item}')">

🕒 ${item}

</div>

`;

});

}

// ==========================

function renderTrending(){

trendingList.innerHTML="";

trending.forEach(item=>{

trendingList.innerHTML+=`

<div class="genre-chip"

onclick="quickSearch('${item}')">

🔥 ${item}

</div>

`;

});

}

// ==========================

function renderGenres(){

genreChips.innerHTML="";

genres.forEach(item=>{

genreChips.innerHTML+=`

<div class="genre-chip"

onclick="quickSearch('${item}')">

${item}

</div>

`;

});

}

// ==========================

function quickSearch(text){

searchInput.value=text;

clearSearch.style.display="block";

searchAnime(text);

saveRecent(text);

}

// ==========================

function saveRecent(text){

recent=

recent.filter(x=>x!==text);

recent.unshift(text);

recent=recent.slice(0,8);

localStorage.setItem(

"zenkai_recent",

JSON.stringify(recent)

);

renderRecent();

}

// ==========================

async function searchAnime(query){

resultGrid.innerHTML=

"<p style='color:#777'>Searching...</p>";

try{

const res=

await fetch(

`https://api.jikan.moe/v4/anime?q=${encodeURIComponent(query)}&limit=12`

);

const json=

await res.json();

resultGrid.innerHTML="";

if(!json.data.length){

resultGrid.innerHTML=

"<p>No anime found.</p>";

return;

}

saveRecent(query);

json.data.forEach(anime=>{

resultGrid.innerHTML+=`

<div class="search-card">

<img

src="${anime.images.jpg.image_url}"

alt="${anime.title}">

<div class="search-card-title">

${anime.title}

</div>

</div>

`;

});

}catch(e){

resultGrid.innerHTML=

"<p>Connection error.</p>";

}

}
