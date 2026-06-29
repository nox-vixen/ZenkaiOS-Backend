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

recent.slice(0,5).forEach(item=>{

recentList.innerHTML+=`

<div class="recent-item">

<div class="recent-left"
onclick="quickSearch('${item}')">

<i class="fa-solid fa-clock-rotate-left"></i>

<span>${item}</span>

</div>

<button
class="recent-arrow"
onclick="quickSearch('${item}')">

<i class="fa-solid fa-arrow-up-right-from-square"></i>

</button>

</div>

`;

});

}

// ==========================

function renderTrending(){

trendingList.innerHTML="";

trending.forEach(item=>{

trendingList.innerHTML+=`

<div
class="trending-chip"

onclick="quickSearch('${item}')">

${item}

</div>

`;

const chip=trendingList.lastElementChild;

let timer;

chip.addEventListener("touchstart",()=>{

timer=setTimeout(()=>{

deleteTrending(new Event("hold"),item);

},700);

});

chip.addEventListener("touchend",()=>{

clearTimeout(timer);

});

chip.addEventListener("touchmove",()=>{

clearTimeout(timer);

});

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
const popup =
document.getElementById("confirmPopup");

const popupTitle =
document.getElementById("confirmTitle");

const popupText =
document.getElementById("confirmText");

const popupYes =
document.getElementById("confirmYes");

document.getElementById("confirmCancel").onclick=()=>{

popup.style.display="none";

};

document.getElementById("clearHistory").onclick=()=>{

popup.style.display="flex";

popupTitle.innerText="Clear History";

popupText.innerText=
"Delete all recent searches?";

popupYes.onclick=()=>{

recent=[];

localStorage.removeItem("zenkai_recent");

renderRecent();

popup.style.display="none";

};

};
// ==========================
// DELETE SINGLE TRENDING
// ==========================

function deleteTrending(event,text){

event.preventDefault();

popup.style.display="flex";

popupTitle.innerText="Delete Trending";

popupText.innerText=`Remove "${text}" from Trending?`;

popupYes.onclick=()=>{

const index=trending.indexOf(text);

if(index>-1){

trending.splice(index,1);

renderTrending();

}

popup.style.display="none";

};

}
// ==========================
// VOICE SEARCH
// ==========================

const voiceBtn =
document.getElementById("voiceBtn");

const voiceSheet =
document.getElementById("voiceSheet");

const cancelVoice =
document.getElementById("cancelVoice");

const voiceStatus =
document.getElementById("voiceStatus");

const voiceResult =
document.getElementById("voiceResult");

let recognition=null;

const SpeechRecognition=
window.SpeechRecognition||
window.webkitSpeechRecognition;

if(SpeechRecognition){

recognition=
new SpeechRecognition();

recognition.lang="en-US";

recognition.interimResults=true;

recognition.maxAlternatives=1;

recognition.continuous=false;

voiceBtn.onclick=()=>{

voiceSheet.style.display="flex";

voiceStatus.innerText="Listening...";

voiceResult.innerText="";

recognition.start();

};

recognition.onresult=(event)=>{

let transcript="";

for(

let i=event.resultIndex;

i<event.results.length;

i++

){

transcript+=

event.results[i][0].transcript;

}

voiceResult.innerText=transcript;

if(event.results[event.results.length-1].isFinal){

searchInput.value=transcript;

clearSearch.style.display="block";

searchAnime(transcript);

saveRecent(transcript);

}

};

recognition.onend=()=>{

setTimeout(()=>{

voiceSheet.style.display="none";

},600);

};

recognition.onerror=()=>{

voiceStatus.innerText="Voice unavailable";

setTimeout(()=>{

voiceSheet.style.display="none";

},1000);

};

}else{

voiceBtn.onclick=()=>{

alert("Voice search is not supported on this browser.");

};

}

cancelVoice.onclick=()=>{

voiceSheet.style.display="none";

if(recognition){

recognition.stop();

}

};
