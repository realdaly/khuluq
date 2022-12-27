let videosSection
let playlistItems
let iframe

// ------- Youtube Player -------
function createYoutubePlayer(url){
  const article = document.querySelector(".article")
  article.innerHTML += 
  `<div class="videos articleVideos">
    <div class="playlistWrapper">
        <div class="playlistItems">
            <div class="items">
            </div>
        </div>
        <div class="player">
            <iframe src="${url}" frameborder="0" allowfullscreen></iframe>
        </div>
    </div>
  </div>`
  videosSection = document.querySelector(".articleVideos")
  iframe = videosSection.querySelector("iframe")

}


function youtubePlayer(item){
  playlistItems = videosSection.querySelectorAll(".playlistItem")
  if(iframe.src != item.dataset.src){
    iframe.src = item.dataset.src
  }
  playlistItems.forEach(one => {
    one.style.color = "var(--accent)"
    one.style.boxShadow = "none"
  })
  item.style.color = "var(--reverseComponent)"
  item.style.boxShadow = "var(--itemShadow)"
}




// ------- Image Gallery -------

function imageGallery(item){
  const overlay = document.querySelector(".overlay")
  const overlayImage = overlay.querySelector("img")
  const overlayClose = overlay.querySelector(".close")
  const download = document.getElementById("download")
    
  const src = item.querySelector("img").src
  download.href = src
  overlayImage.src = src
  
  overlayImage.style.cursor = "zoom-out"
  overlay.classList.add("open")
  overlay.style.animationPlayState = "running"
  
  
  function close(){
    overlay.classList.remove("open")
  }
  
  document.onkeydown=function(e){
    if(e.which == 27){
        close()
        return false
    }
  }
  
  overlayClose.addEventListener("click", close)
  overlay.addEventListener("click", close)
}