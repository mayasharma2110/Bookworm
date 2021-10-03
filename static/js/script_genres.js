function delete_check(){

    // show hidden div
    $("#delete_genre_check").removeClass("hide").addClass("show"); 

}

document.getElementById("delete_genre").addEventListener('click',delete_check);