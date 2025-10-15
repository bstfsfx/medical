$(document).ready(function() {
    // when the modal is shown
    $("#deleteConfirmModal").on("show.bs.modal", function(event) {
        const button = $(event.relatedTarget); // Button that triggered the modal
        const contactId = button.data("id"); // Extract info from data-* attributes
        const deleteUrl = button.data("url");
        $("modal-contact-id").text(contactId);
        //set the delete url
        $("#confirmDeleteBtn").attr("href", deleteUrl);
    });
    // when the de;ete button is clicked
    $("#confirmDeleteBtn").click(function(event) {
        // close the modal
        $("#deleteConfirmModal").modal("hide");
        setTimeout(() => {
            window.location.href = $("#confirmDeleteBtn").attr("href");
        }, 300);
    });
});