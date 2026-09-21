/**
 * "Copy page" split button beside the page title.
 *
 * The button copies the page as Markdown. The chevron opens a menu with
 * "View as Markdown" and "Edit on GitHub". The Markdown lives next to each
 * rendered page as `index.md` (see scripts/gen_markdown_pages.py); the edit
 * link comes from Zensical's `page.edit_url`. Configuration arrives through
 * `window.iscc`, set by the theme's main.html.
 */
(function () {
  "use strict";

  var ICONS = {
    copy:
      '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect width="14" height="14" x="8" y="8" rx="2" ry="2"/><path d="M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2"/></svg>',
    fileText:
      '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>',
    pencil:
      '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/><path d="m15 5 4 4"/></svg>',
    chevronDown:
      '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>',
    check:
      '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
  };

  /** Read the theme configuration written by main.html. */
  function getConfig() {
    return window.iscc || {};
  }

  /** URL of the Markdown source generated beside the rendered page. */
  function getMarkdownUrl() {
    var cfg = getConfig();
    var base = cfg.base ? cfg.base.replace(/\/?$/, "/") : "";
    return base + (cfg.pageUrl || "") + "index.md";
  }

  /** Build one menu entry. */
  function createItem(icon, title, desc, onClick) {
    var btn = document.createElement("button");
    btn.className = "copy-page__item";
    btn.type = "button";
    btn.innerHTML =
      '<span class="copy-page__item-icon">' +
      icon +
      "</span>" +
      '<span class="copy-page__item-text">' +
      '<span class="copy-page__item-title">' +
      title +
      "</span>" +
      '<span class="copy-page__item-desc">' +
      desc +
      "</span>" +
      "</span>";
    btn.addEventListener("click", function () {
      onClick(btn);
    });
    return btn;
  }

  /** Copy the Markdown source to the clipboard and confirm on the button. */
  function copyPage(el, actionBtn) {
    el.classList.remove("copy-page--open");
    var origHtml = actionBtn.innerHTML;
    fetch(getMarkdownUrl())
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        return r.text();
      })
      .then(function (text) {
        return navigator.clipboard.writeText(text);
      })
      .then(function () {
        actionBtn.innerHTML = ICONS.check + "<span>Copied</span>";
        setTimeout(function () {
          actionBtn.innerHTML = origHtml;
        }, 2000);
      })
      .catch(function (err) {
        console.error("Copy page failed:", err);
      });
  }

  /** Mount the widget next to the first page heading. */
  function init() {
    var cfg = getConfig();
    if (cfg.copyPage === false) return;
    var article = document.querySelector(".md-content__inner");
    if (!article || article.querySelector(".copy-page")) return;
    var h1 = article.querySelector("h1");
    if (!h1) return;

    var el = document.createElement("div");
    el.className = "copy-page";

    var split = document.createElement("div");
    split.className = "copy-page__split";

    var actionBtn = document.createElement("button");
    actionBtn.className = "copy-page__action";
    actionBtn.type = "button";
    actionBtn.title = "Copy page as Markdown";
    actionBtn.innerHTML = ICONS.copy + "<span>Copy page</span>";
    actionBtn.addEventListener("click", function () {
      copyPage(el, actionBtn);
    });

    var toggleBtn = document.createElement("button");
    toggleBtn.className = "copy-page__toggle";
    toggleBtn.type = "button";
    toggleBtn.title = "More actions";
    toggleBtn.setAttribute("aria-label", "More page actions");
    toggleBtn.innerHTML = ICONS.chevronDown;
    toggleBtn.addEventListener("click", function () {
      el.classList.toggle("copy-page--open");
    });

    split.appendChild(actionBtn);
    split.appendChild(toggleBtn);

    var menu = document.createElement("div");
    menu.className = "copy-page__menu";

    menu.appendChild(
      createItem(ICONS.copy, "Copy page", "Copy the page as Markdown", function () {
        copyPage(el, actionBtn);
      }),
    );

    menu.appendChild(
      createItem(ICONS.fileText, "View as Markdown", "Open the Markdown source", function () {
        el.classList.remove("copy-page--open");
        window.open(getMarkdownUrl(), "_blank");
      }),
    );

    if (cfg.editUrl) {
      menu.appendChild(
        createItem(ICONS.pencil, "Edit on GitHub", "Suggest a change to this page", function () {
          el.classList.remove("copy-page--open");
          window.open(cfg.editUrl, "_blank");
        }),
      );
    }

    el.appendChild(split);
    el.appendChild(menu);

    el.addEventListener("click", function (e) {
      e.stopPropagation();
    });

    var wrapper = document.createElement("div");
    wrapper.className = "copy-page-heading";
    h1.parentNode.insertBefore(wrapper, h1);
    wrapper.appendChild(h1);
    wrapper.appendChild(el);

    document.addEventListener("click", function () {
      el.classList.remove("copy-page--open");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") el.classList.remove("copy-page--open");
    });
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
