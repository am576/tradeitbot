document.getElementById("button-test").addEventListener("click", ()=>{eel.test_selenium()}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}