function delete_check(){

    // show hidden div
    $("#delete_book_check").removeClass("hide").addClass("show"); 

}

document.getElementById("delete_book").addEventListener('click',delete_check);