$(function () {
    $(document).ready(function () {


        //details button click handler
        $('td > button[action="details"]').click(function () {
            host_id = $(this).attr('host-id');
            window.location = "details/" + host_id;
        });

        //edit button click handler
        $('td > button[action="edit"]').click(function () {
            host_id = $(this).attr('host-id');
            
        });

        //add button click handler
        $('#add-monit-host').click(function () {
            $('#add-host-modal').modal('show');

        });















        //delete confirmation confirm
        $("#continue-delete-button").click(function() {
            //send DELETE
            $.ajax({
                type: 'DELETE',
                url: 'db/' + table + '/' + id,
                dataType: "json",
                success: function(response) {
                    if (response.success)
                        window.location.reload();
                    else{
                        //show alert
                        $("#confirmation-delete-alert").empty();
                        $("#confirmation-delete-alert").append(response.message);
                        $("#confirmation-delete-alert").show();
                    }
                }
            });
        });







    });
});

