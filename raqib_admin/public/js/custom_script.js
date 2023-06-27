window.addEventListener("hashchange", function() {
  if (window.location.href.includes("/list")) {
    var newURL = window.location.href.replace("/list", "/image");
    window.location.href = newURL;
  }
});
