// Harvests Gateway website: navigation, product filters, reveal animations and the WhatsApp order form
(function () {
  "use strict";
  document.documentElement.classList.add("js");

  // Header shadow on scroll
  var header = document.getElementById("siteHeader");
  function onScroll() { header.classList.toggle("scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("mainNav");
  function setMenu(open) {
    document.body.classList.toggle("nav-open", open);
    document.documentElement.classList.toggle("nav-lock", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  }
  toggle.addEventListener("click", function () { setMenu(!document.body.classList.contains("nav-open")); });
  nav.addEventListener("click", function (e) { if (e.target.closest("a")) setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
  document.addEventListener("click", function (e) {
    if (document.body.classList.contains("nav-open") && !e.target.closest(".site-header")) setMenu(false);
  });
  window.addEventListener("resize", function () { if (window.innerWidth > 960) setMenu(false); });

  // Reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // Home page hero slideshow
  var slider = document.getElementById("heroSlider");
  if (slider) {
    var slides = slider.querySelectorAll(".hero-slide");
    var dots = slider.querySelectorAll(".hero-dots button");
    var current = 0, timer = null, DELAY = 4500;
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function show(i) {
      current = (i + slides.length) % slides.length;
      slides.forEach(function (s, n) { s.classList.toggle("is-active", n === current); });
      dots.forEach(function (d, n) {
        d.classList.toggle("is-active", n === current);
        d.setAttribute("aria-selected", String(n === current));
      });
    }
    function start() { stop(); if (!reduceMotion) timer = setInterval(function () { show(current + 1); }, DELAY); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }

    dots.forEach(function (d, n) { d.addEventListener("click", function () { show(n); start(); }); });
    slider.addEventListener("mouseenter", stop);
    slider.addEventListener("mouseleave", start);
    document.addEventListener("visibilitychange", function () { document.hidden ? stop() : start(); });

    // Swipe left or right on phones
    var startX = null;
    slider.addEventListener("touchstart", function (e) { startX = e.touches[0].clientX; }, { passive: true });
    slider.addEventListener("touchend", function (e) {
      if (startX === null) return;
      var dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 40) { show(current + (dx < 0 ? 1 : -1)); start(); }
      startX = null;
    });

    start();
  }

  // Product filters (Products page). Also supports links like /products#popcorn
  var chips = document.querySelectorAll(".chip[data-filter]");
  if (chips.length) {
    var cards = document.querySelectorAll("#productGrid .product-card");
    function applyFilter(cat) {
      chips.forEach(function (c) {
        var on = c.dataset.filter === cat;
        c.classList.toggle("is-active", on);
        c.setAttribute("aria-pressed", String(on));
      });
      cards.forEach(function (card) {
        var show = cat === "all" || card.dataset.category === cat;
        card.classList.toggle("is-hidden", !show);
        if (show) card.classList.add("in");
      });
    }
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        applyFilter(c.dataset.filter);
        history.replaceState(null, "", c.dataset.filter === "all" ? location.pathname : "#" + c.dataset.filter);
      });
    });
    var hash = location.hash.replace("#", "");
    if (hash && document.querySelector('.chip[data-filter="' + hash + '"]')) applyFilter(hash);
  }

  // Quick order form (Contact page) -> opens WhatsApp with the order
  var form = document.getElementById("orderForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var name = form.name.value.trim();
      var product = form.product.value;
      var qty = Math.max(1, parseInt(form.qty.value, 10) || 1);
      var loc = form.location.value.trim();
      var note = form.note.value.trim();
      var err = document.getElementById("formError");

      form.name.classList.toggle("invalid", !name);
      form.product.classList.toggle("invalid", !product);
      if (!name || !product) { err.hidden = false; return; }
      err.hidden = true;

      var lines = [
        "Hello Harvests Gateway, I would like to place an order.",
        "",
        "*Name:* " + name,
        "*Snack:* " + product,
        "*Packs:* " + qty
      ];
      if (loc) lines.push("*Delivery location:* " + loc);
      if (note) lines.push("*Note:* " + note);
      lines.push("", "Thank you.");

      var url = "https://wa.me/" + form.dataset.wa + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
    });
  }
})();
