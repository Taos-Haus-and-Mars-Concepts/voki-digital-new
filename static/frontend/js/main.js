/**
* Template Name: Gp
* Updated: Jul 27 2023 with Bootstrap v5.3.1
* Template URL: https://bootstrapmade.com/gp-free-multipurpose-html-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

console.log("main.js is loaded and running!");

// 1. Select all hero icon-boxes that have data-service
const heroBoxes = document.querySelectorAll('.icon-box[data-service]');

// Let's log out how many we found
console.log("Found heroBoxes:", heroBoxes);
console.log("Number of heroBoxes found:", heroBoxes.length);

// 2. A helper to scroll to #services smoothly
function scrollToServices() {
  const header = document.querySelector('#header');
  console.log("Header found?", header);
  const offset = header ? header.offsetHeight : 0;
  console.log("Header offset is:", offset);

  const servicesSection = document.querySelector('#services');
  console.log("Services section found?", servicesSection);

  // If we didn't find #services, return early
  if (!servicesSection) {
    console.warn("No #services section found. Exiting scrollToServices.");
    return;
  }

  const elementPos = servicesSection.offsetTop;
  console.log("Scrolling to Y-position:", elementPos - offset);

  window.scrollTo({
    top: elementPos - offset,
    behavior: 'smooth'
  });
}

// 3. Add click listeners for hero boxes
heroBoxes.forEach(box => {
  box.addEventListener('click', () => {
    console.log("Hero box clicked:", box);

    // Grab the matching service name from data-service
    const serviceName = box.getAttribute('data-service');
    console.log("Service name is:", serviceName);

    // Scroll to #services
    console.log("Scrolling to #services now...");
    scrollToServices();

    // After a short delay, flip the correct card
    setTimeout(() => {
      const targetCard = document.querySelector(`.flip-card[data-service-target="${serviceName}"]`);
      if (targetCard) {
        console.log("Found target card:", targetCard);
        // Add the .flipped class so it rotates
        targetCard.classList.add('flipped');
        console.log("Added .flipped class to target card.");
      } else {
        console.warn(`No .flip-card found with data-service-target="${serviceName}"`);
      }
    }, 600); // Adjust timeout if needed
  });
});

// 4. Let users flip cards directly while on Services
const flipCards = document.querySelectorAll('.flip-card');
console.log("Found flip cards:", flipCards);

flipCards.forEach(card => {
  card.addEventListener('click', () => {
    console.log("Services card clicked:", card);
    // Toggle .flipped so it flips/unflips on each click
    card.classList.toggle('flipped');
    console.log("Toggled .flipped class on this card");
  });
});


(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Clients Slider
   */
  new Swiper('.clients-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 2,
        spaceBetween: 40
      },
      480: {
        slidesPerView: 3,
        spaceBetween: 60
      },
      640: {
        slidesPerView: 4,
        spaceBetween: 80
      },
      992: {
        slidesPerView: 6,
        spaceBetween: 120
      }
    }
  });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Initiate portfolio lightbox 
   */
  const portfolioLightbox = GLightbox({
    selector: '.portfolio-lightbox'
  });

  /**
   * Portfolio details slider
   */
  new Swiper('.portfolio-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Testimonials slider
   */
  new Swiper('.testimonials-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false
    });
  });

  /**
   * Initiate Pure Counter 
   */
  new PureCounter();

})()

let prevScrollPos = window.scrollY;
const navbar = document.querySelector(".navbar");

window.onscroll = function () {
    let currentScrollPos = window.scrollY;

    if (prevScrollPos > currentScrollPos) {
        // Scrolling up, show the navbar
        navbar.style.top = "0";
    } else {
        // Scrolling down, hide the navbar
        navbar.style.top = `-${navbar.clientHeight}px`;
    }

    prevScrollPos = currentScrollPos;
};


// hero js background

document.addEventListener('DOMContentLoaded', function () {
    const media = document.querySelectorAll('.background-media');
    let currentIndex = 0;

    function changeMedia() {
        const currentMedia = media[currentIndex];
        const nextIndex = (currentIndex + 1) % media.length;
        const nextMedia = media[nextIndex];

        currentMedia.style.opacity = 0;
        nextMedia.style.opacity = 1;

        currentMedia.style.zIndex = 0;
        nextMedia.style.zIndex = 1;

        currentIndex = nextIndex;

        setTimeout(() => {
            changeMedia();
        }, 5000); // Change media every 5 seconds
    }

    changeMedia();
});



const cardSlider = document.querySelector('.cards-container');
let currentIndex = 0;
const cardWidth = 280; // Adjusted card width including margin

// Left Arrow Click Event
document.querySelector('.arrow-left').addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        cardSlider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
    }
});

// Right Arrow Click Event
document.querySelector('.arrow-right').addEventListener('click', () => {
    const maxIndex = cardSlider.children.length - Math.floor(document.querySelector('.card-slider').offsetWidth / cardWidth);
    if (currentIndex < maxIndex) {
        currentIndex++;
        cardSlider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
    }
});



