/**
 * Mount the iscc.ai chat widget with anonymous authentication.
 *
 * Fetches a short-lived token from iscc.ai, then mounts the Chainlit copilot
 * widget with the theme's stylesheet injected into its shadow DOM. Enabled by
 * `chat = true` in `[project.extra.iscc]`; main.html loads this file only then.
 */
(function () {
  "use strict";

  var SERVER = "https://iscc.ai";

  /** Theme name matching the active colour scheme. */
  function currentTheme() {
    var scheme = document.body.getAttribute("data-md-color-scheme");
    return scheme === "slate" ? "dark" : "light";
  }

  /** Absolute URL of the widget stylesheet, resolved from the theme base. */
  function stylesheetUrl() {
    var base = (window.iscc && window.iscc.base) || "";
    var href = base.replace(/\/?$/, "/") + "assets/iscc/copilot.css";
    return new URL(href, window.location.href).href;
  }

  async function mount() {
    if (typeof window.mountChainlitWidget !== "function") return;
    try {
      var response = await fetch(SERVER + "/api/copilot-token");
      var data = await response.json();
      window.mountChainlitWidget({
        chainlitServer: SERVER,
        theme: currentTheme(),
        accessToken: data.accessToken,
        customCssUrl: stylesheetUrl(),
      });
    } catch (e) {
      console.warn("iscc.ai chat: failed to mount", e);
    }
  }

  if (document.readyState === "complete") {
    mount();
  } else {
    window.addEventListener("load", mount);
  }
})();
