var toggleSearchColor = () => {
    let searchDiv = document.getElementById("searchDiv");
    console.log(searchDiv.style.borderColor)
    if (searchDiv.style.borderColor == "rgb(48, 82, 255)") {
        searchDiv.style.borderColor = "gray";
    }
    else {
        searchDiv.style.borderColor = "#3052FF";
    }
}