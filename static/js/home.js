window.onerror = function(message, source, line, column, error){

document.body.innerHTML = `
<div style="
padding:20px;
background:#000;
color:#fff;
font-family:monospace;
white-space:pre-wrap;
word-break:break-word;
">

<h2>JavaScript Error</h2>

<b>Message:</b>
${message}

<br><br>

<b>Line:</b>
${line}

<br><br>

<b>Column:</b>
${column}

<br><br>

<b>Source:</b>
${source}

</div>
`;

return true;

};


function showSkeleton(){

heroSlider.innerHTML=`
<div class="skeleton-banner"></div>
`;

let html="";

for(let s=0;s<6;s++){

html+=`

<div class="home-section">

<div class="skeleton-row">

${new Array(6).fill(`
<div class="skeleton-card">

<div class="skeleton-poster"></div>

<div class="skeleton-title"></div>

<div class="skeleton-rating"></div>

</div>
`).join("")}

</div>

</div>

`;

}

homeSections.innerHTML=html;

}

// ==========================
// HEADER
// ==========================

const menuBtn = document.getElementById("menuBtn");
const searchBtn = document.getElementById("searchBtn");
const notificationBtn = document.getElementById("notificationBtn");
const profileAvatar = document.getElementById("profileAvatar");

menuBtn.onclick = () => console.log("Menu");

searchBtn.onclick = () => location.href = "/search";

notificationBtn.onclick = () => console.log("Notifications");

profileAvatar.onclick = () => location.href = "/profile";

const header = document.getElementById("header");

let lastScroll = 0;

window.addEventListener("scroll", () => {

const current = window.pageYOffset;

if(current > lastScroll && current > 80){

header.style.transform="translate(-50%,-100%)";

}else{

header.style.transform="translate(-50%,0)";

}

lastScroll=current;

});


// ==========================
// HERO
// ==========================

const heroSlider=document.getElementById("heroSlider");

const heroIndicators=document.getElementById("heroIndicators");

const homeSections=document.getElementById("homeSections");

showSkeleton();

async function loadHome(){

const response=await fetch("/api/home");

const data=await response.json();

buildHero(data.featured.items);
buildTopPick(data.featured.items[0]);
buildSections(data.sections);
startHeroSlider();

}

function buildHero(items){

heroSlider.innerHTML="";

heroIndicators.innerHTML="";

items.forEach((anime,index)=>{

heroSlider.innerHTML+=`

<div class="hero-slide">

<img src="${anime.bannerImage || anime.coverImage}">

<div class="hero-overlay">

<div class="hero-tag">

TOP ANIME

</div>

<div class="hero-title">

${anime.title}

</div>

<div class="hero-description">

${(anime.description || "No description available.").substring(0,120)}...

</div>

<div class="hero-actions">

<button
class="hero-watch"
onclick="openAnime(${anime.id})">

<i class="fa-solid fa-play"></i>

Watch Now

</button>

<button
class="hero-list">

<i class="fa-solid fa-plus"></i>

My List

</button>

</div>

</div>

</div>

`;

heroIndicators.innerHTML+=`

<span class="${index===0?"active":""}"></span>

`;

});


}

function buildTopPick(anime){

document.getElementById("topPickCard").innerHTML=`

<div class="top-pick-v4">

<div class="top-pick-poster">

<img
src="${anime.coverImage}"
alt="${anime.title}">

</div>

<div class="top-pick-details">

<div class="top-pick-rating">

⭐ ${anime.rating ?? "N/A"}

<span>•</span>

${anime.year ?? ""}

</div>

<h2>

${anime.title}

</h2>

<div class="top-pick-genres">

${(anime.genres || []).slice(0,3).map(g=>`<span>${g}</span>`).join("")}

</div>

<p>

${anime.description || ""}

</p>

<div class="top-pick-icons">

<button
onclick="openAnime(${anime.id})">

<i class="fa-solid fa-play"></i>

</button>

<button>

<i class="fa-solid fa-plus"></i>

</button>

</div>

</div>

</div>

`;

}

function buildSections(sections){

homeSections.innerHTML="";

sections.forEach(section=>{

let cards="";

section.items.forEach((anime,index)=>{

cards+=`

<div class="anime-card" onclick="openAnime(${anime.id})">

<div class="anime-poster">

<img
src="${anime.coverImage}"
loading="lazy"
alt="${anime.title}">

<div class="anime-rank">
#${index+1}
</div>

<div class="episode-badge">
${anime.status || "ANIME"}
</div>

<div class="anime-gradient"></div>

<div class="anime-hover">

<button class="play-mini">

<i class="fa-solid fa-play"></i>

</button>

</div>

<div class="progress-bar">

<div class="progress-fill" style="width:${Math.floor(Math.random()*70)+20}%"></div>

</div>

</div>

<div class="anime-info">

<div class="anime-title">

${anime.title}

</div>

<div class="anime-meta">

⭐ ${anime.rating ?? "N/A"}

<span class="dot"></span>

${anime.year ?? ""}

</div>

</div>

</div>

`;

});

homeSections.innerHTML+=`

<section class="home-section">

<div class="section-header">

<div class="section-title">

<i class="fa-solid fa-fire"></i>

<span>${section.title}</span>

</div>

<div class="section-view">

VIEW ALL

</div>

</div>

<div class="anime-row">

${cards}

</div>

</section>

`;

});

}

loadHome();

// ==========================
// HERO AUTO SLIDER
// ==========================

let currentHero = 0;

let heroTimer = null;

let resumeTimer = null;

let isTouchingHero = false;

function showHero(index){

const slides =
document.querySelectorAll(".hero-slide");

const dots =
document.querySelectorAll("#heroIndicators span");

if(!slides.length) return;

currentHero = index;

heroSlider.scrollTo({

left:index*heroSlider.clientWidth,

behavior:"smooth"

});

slides.forEach(slide=>slide.classList.remove("active"));

dots.forEach(dot=>dot.classList.remove("active"));

if(dots[index]){

dots[index].classList.add("active");

}

if(slides[index]){

slides[index].classList.add("active");

}

}

function startHeroSlider(){

if(heroTimer){

clearInterval(heroTimer);

}

showHero(0);

heroTimer = setInterval(()=>{

const slides =
document.querySelectorAll(".hero-slide");

if(!slides.length) return;

currentHero++;

if(currentHero>=slides.length){

currentHero=0;

}

showHero(currentHero);

},5000);

}

function stopHeroSlider(){

if(heroTimer){

clearInterval(heroTimer);

heroTimer = null;

}

}

function resumeHeroSlider(){

clearTimeout(resumeTimer);

resumeTimer = setTimeout(()=>{

startHeroSlider();

},3000);

}

heroSlider.addEventListener("scroll",()=>{

const slides =
document.querySelectorAll(".hero-slide");

if(!slides.length) return;

const index =
Math.round(heroSlider.scrollLeft/heroSlider.clientWidth);

const dots =
document.querySelectorAll("#heroIndicators span");

dots.forEach(dot=>dot.classList.remove("active"));

if(dots[index]){

dots[index].classList.add("active");

currentHero=index;

}

});

heroSlider.addEventListener("touchstart",()=>{

isTouchingHero = true;

stopHeroSlider();

});

heroSlider.addEventListener("touchend",()=>{

isTouchingHero = false;

resumeHeroSlider();

});

heroSlider.addEventListener("mousedown",()=>{

stopHeroSlider();

});

heroSlider.addEventListener("mouseup",()=>{

resumeHeroSlider();

});

heroSlider.addEventListener("mouseenter",()=>{

stopHeroSlider();

});

heroSlider.addEventListener("mouseleave",()=>{

resumeHeroSlider();

});

function openAnime(id){

window.location.href="/watch?id="+id;

}




// ==========================
// Bottom Navigation
// ==========================

document.getElementById("bottomNav").innerHTML = `

<div class="nav-item active">

<i class="fa-solid fa-house"></i>

<span>Home</span>

</div>

<div class="nav-item">

<i class="fa-solid fa-tv"></i>

<span>Anime</span>

</div>

<div class="center-nav">

<i class="fa-solid fa-play"></i>

</div>

<div class="nav-item">

<i class="fa-solid fa-bookmark"></i>

<span>List</span>

</div>

<div class="nav-item">

<i class="fa-solid fa-user"></i>

<span>Profile</span>

</div>

`;
