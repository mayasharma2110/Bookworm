function delete_check(){

    // show hidden div
    $("#delete_review_check").removeClass("hide").addClass("show"); 

}

document.getElementById("delete_review").addEventListener('click',delete_check);