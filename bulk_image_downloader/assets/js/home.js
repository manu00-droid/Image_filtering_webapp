document.getElementById("numImages").addEventListener("input", function () {
    const inputValue = parseInt(this.value);
    const certainValue = 60;

    const additionalText = document.getElementById("additionalText");

    if (inputValue > certainValue) {
        additionalText.style.display = "block";
    } else {
        additionalText.style.display = "none";
    }
});