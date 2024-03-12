const responses = {
    "h": "https://h.kevin-wang.ca"
}
function submit(selection) {
    if (!(selection in responses)) {
        return
    }
    window.open(responses[selection], "_blank")
}