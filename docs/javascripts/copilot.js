/**
 * Mount the ISCC-AI copilot chat widget with anonymous authentication.
 *
 * Fetches a JWT token from the copilot-token endpoint, then mounts the
 * Chainlit copilot widget with the token for cross-origin authentication.
 */
window.addEventListener("load", async function () {
  if (typeof window.mountChainlitWidget !== "function") return;

  var server = "https://iscc.ai";
  var tokenUrl = server + "/api/copilot-token";

  try {
    var response = await fetch(tokenUrl);
    var data = await response.json();
    window.mountChainlitWidget({
      chainlitServer: server,
      theme: "light",
      accessToken: data.accessToken,
      customCssUrl: window.location.origin + "/stylesheets/copilot.css?v=1",
    });
  } catch (e) {
    console.warn("ISCC-AI copilot: failed to fetch token", e);
  }
});
