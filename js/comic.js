var comic_images = []
var current_page_index = 0;
var total_pages = 0;
const comicImag = document.getElementById("comic-img");
const pageSelect = document.getElementById("page-select");
function init_images(image_array)
{
    for (var i = 0; i < image_array.length; i++) 
    {
        comic_images.push(image_array[i]);
    }
    total_pages = comic_images.length;
}
function init()
{
    pageSelect.addEventListener("change", function () {
        current_page_index = pageSelect.value;
        update_comic_page();
    });
    function init_page_select() {
        pageSelect.innerHTML = "";
        for (let i = 0; i < total_pages; i++) {
            const option = document.createElement("option");
            option.value = i;
            option.text = i + 1;
            pageSelect.appendChild(option);
        }
    }
    if (total_pages > 0) {
        init_page_select();
        update_comic_page();
    }
}
function page_up() {
    if (current_page_index > 0) {
        current_page_index--;
        update_comic_page();
    }
}
function page_down() {
    if (current_page_index < total_pages - 1) {
        current_page_index++;
        update_comic_page();
    }
}
function update_comic_page() {
    comicImag.src = comic_images[current_page_index];
    pageSelect.value = current_page_index;
}