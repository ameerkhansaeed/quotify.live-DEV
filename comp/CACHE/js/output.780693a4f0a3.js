const pageButtons=document.querySelectorAll('.page');pageButtons.forEach(button=>{button.addEventListener('click',()=>{pageButtons.forEach(btn=>btn.classList.remove('active'));button.classList.add('active');});});function changePage(offset){const activeButton=document.querySelector('.page.active');if(activeButton){const currentIndex=Array.from(pageButtons).indexOf(activeButton);const newIndex=currentIndex+offset;if(newIndex>=0&&newIndex<pageButtons.length){activeButton.classList.remove('active');pageButtons[newIndex].classList.add('active');}}};const menu_btn=document.querySelector('.hamburger');const mobile_menu=document.querySelector('.mobile_nav');menu_btn.addEventListener('click',function(event){event.stopPropagation();menu_btn.classList.toggle('is-active');mobile_menu.classList.toggle('is-active');});document.addEventListener('click',function(event){const isClickInsideMenu=mobile_menu.contains(event.target);const isClickOnButton=menu_btn.contains(event.target);if(!isClickInsideMenu&&!isClickOnButton){menu_btn.classList.remove('is-active');mobile_menu.classList.remove('is-active');}});const MIN_SPEED=1.5
const MAX_SPEED=2.5
function randomNumber(min,max){return Math.random()*(max-min)+min}
class Blob{constructor(el){this.el=el
const boundingRect=this.el.getBoundingClientRect()
this.size=boundingRect.width
this.initialX=randomNumber(0,window.innerWidth-this.size)
this.initialY=randomNumber(0,window.innerHeight-this.size)
this.el.style.top=`${this.initialY}px`
this.el.style.left=`${this.initialX}px`
this.vx=randomNumber(MIN_SPEED,MAX_SPEED)*(Math.random()>0.5?1:-1)
this.vy=randomNumber(MIN_SPEED,MAX_SPEED)*(Math.random()>0.5?1:-1)
this.x=this.initialX
this.y=this.initialY}
update(){this.x+=this.vx
this.y+=this.vy
if(this.x>=window.innerWidth-this.size){this.x=window.innerWidth-this.size
this.vx*=-1}
if(this.y>=window.innerHeight-this.size){this.y=window.innerHeight-this.size
this.vy*=-1}
if(this.x<=0){this.x=0
this.vx*=-1}
if(this.y<=0){this.y=0
this.vy*=-1}}
move(){this.el.style.transform=`translate(${this.x - this.initialX}px, ${
      this.y - this.initialY
    }px)`}}
function initBlobs(){const blobEls=document.querySelectorAll('.bouncing-blob')
const blobs=Array.from(blobEls).map((blobEl)=>new Blob(blobEl))
function update(){requestAnimationFrame(update)
blobs.forEach((blob)=>{blob.update()
blob.move()})}
requestAnimationFrame(update)}
initBlobs();