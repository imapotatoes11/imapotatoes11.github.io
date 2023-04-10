if (navigator.userAgent.includes("Firefox") || navigator.userAgent.includes("Internet Explorer")) {
    if (!window.location.href.includes("unsupported=true"))
        window.location.href="unsupported_browser.html"
}