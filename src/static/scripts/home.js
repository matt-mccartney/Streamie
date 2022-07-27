var scrollSlider = (elem, dir) => {
    let itemWidth = 250 + 10 // 10 for spacing
    let step = 5
    let parent = elem.parentElement;
    let slider = parent.querySelector('#slider');

    if (slider.scrollLeft - itemWidth*step <= 0) {
        parent.querySelector('.prev').style.display = "none";
        parent.querySelector('.next').style.display = "block";
    }
    else {
        parent.querySelector('.prev').style.display = "block";
        parent.querySelector('.next').style.display = "none";
    }
    if (slider.scrollLeft + itemWidth*step <= slider.clientWidth) {
        parent.querySelector('.next').style.display = "none";
        parent.querySelector('.prev').style.display = "block";
    }
    else {
        parent.querySelector('.next').style.display = "block";
        parent.querySelector('.prev').style.display = "none";
    }

    if (dir === "right") {
        slider.scrollLeft += itemWidth*step;
    }
    else if (dir === "left") {
        slider.scrollLeft -= itemWidth*step;
    } else {
        throw ValueError;
    }

    console.log(slider.scrollLeft, slider.scrollRight)
}