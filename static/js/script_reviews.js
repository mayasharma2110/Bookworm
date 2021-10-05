$(".delete_review").click(function() {
    console.log("Conditional check")
    $(this).next().removeClass("hide1").addClass("show1")
})