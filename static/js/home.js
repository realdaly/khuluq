// ------- Slider -------
const swiper = new Swiper('.swiper', {
  init: false,
  rewind: true,
  spaceBetween: 0,
  grabCursor: true,
  autoplayDisableOnInteraction: true,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  keyboard: {
    enabled: true,
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
})

  
  
  
  
// ------- Productions Section -------
function showTab(tab){
  document.querySelector(".productions").querySelectorAll("section").forEach(section => {
    section.style.display = "none"
    section.style.opacity = "0"
  })
  document.querySelector(`#${tab}`).style.display = "flex"

  document.querySelector(".productions").querySelectorAll("section").forEach(section => {
    window.setTimeout(function(){
      section.style.opacity = "1"
    },0)

  })
}

document.addEventListener("DOMContentLoaded", function(){
  document.querySelector(".productions").querySelectorAll("input").forEach((input, index) => {
    if(index==0){
      input.checked = true
    } else {
      input.checked = false
    }
  })
})




// ------- Moral Stories -------
const storySwiper = new Swiper('.storySlider', {
  init: false,
  spaceBetween: 30,
  effect: 'fade',
  loop: true,
  pagination: {
    el: '.storySliderPagination',
    clickable: true,
  }
});




// ------- Image Gallery Section -------
function imageGallery(item){
  const overlay = document.querySelector(".homeImageGallery .galleryOverlay")
  const overlayImage = overlay.querySelector("img")
  const overlayClose = overlay.querySelector(".close")
  const overlayDownload = overlay.querySelector(".download")
  

  const src = item.querySelector("img").src
  overlayImage.src = src
  overlayDownload.href = src
  overlayImage.style.cursor = "zoom-out"
  overlay.classList.add("open")
  overlay.style.animationPlayState = "running"
  
  
  function close(){
      overlay.classList.remove("open")
  }
  
  document.onkeydown=function(e){
      if(e.which == 27){
          close();
          return false
      }
  }

  
  overlayClose.addEventListener("click", close)
  overlay.addEventListener("click", close)
  overlayDownload.onclick = function(){
      event.stopPropagation()
  }
}




// ------- Videos Section -------
function videoSection(item){
  const videosSection = document.querySelector(".homeVideos")
  const playlistItems = videosSection.querySelectorAll(".playlistItem")
  const iframe = videosSection.querySelector("iframe")

  if(iframe.src != item.dataset.link){
    iframe.src = item.dataset.link
  }

  playlistItems.forEach(one => {
    one.style.color = "var(--accent)"
    one.style.boxShadow = "none"
  })
  item.style.color = "var(--reverseComponent)"
  item.style.boxShadow = "var(--itemShadow)"
}




// ------- Footer -------
const branchBtns = document.querySelectorAll(".branchBtn")

function showBranch(branch){
  document.querySelectorAll(".branch").forEach(branch => {
    branch.removeAttribute("id")
  })
  document.querySelector(`.${branch}`).setAttribute("id", "show")
}

branchBtns.forEach(btn => {
  btn.onclick = function(){
    branchBtns.forEach(btn => {
      btn.removeAttribute("id")
    })
    this.setAttribute("id", "activeButton")
    showBranch(this.dataset.branch)
    if(document.querySelector(".location iframe").src != this.dataset.location){
      document.querySelector(".location iframe").src = this.dataset.location
    }
  }
})




// ------- array shuffling function -------
function shuffle(array){
  const newArray = [...array]
  const length = newArray.length

  for (let i = 0; i < length; i++) {
    const randomPosition = Math.floor((newArray.length - i) * Math.random())
    const randomItem = newArray.splice(randomPosition, 1)

    newArray.push(...randomItem)
  }

  return newArray
}