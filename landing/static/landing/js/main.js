(function () {
  "use strict";

  // --- Sticky header: solid background after scrolling past the hero top ---
  const header = document.querySelector(".site-header");
  const onScroll = () => {
    if (window.scrollY > 40) header.classList.add("is-solid");
    else header.classList.remove("is-solid");
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // --- Mobile navigation toggle ---
  const toggle = document.querySelector(".nav-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => {
      const open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    links.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      })
    );
  }

  // --- Scroll reveal ---
  const revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach((el) => io.observe(el));
    // Safety net: if anything is still hidden after 2.5s (e.g. observer never
    // fires), reveal it so content is never stuck invisible.
    setTimeout(() => revealEls.forEach((el) => el.classList.add("is-visible")), 2500);
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  // --- Footer year ---
  const yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
