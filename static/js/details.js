$(function () {
    $(document).ready(function () {

        var host_id;
        var proc_name;
        var enable_refresh = true;

        //refresh 60 s
        setTimeout(function () { 
            if(enable_refresh)            
                location.reload();
        }, 60 * 1000);

        //start button click handler
        $('td > button[action="start-proc"]').click(function () {
            host_id = $(this).attr('host-id');
            proc_name = $(this).attr('proc-name');

            $.ajax({
                type: "POST",
                url: '/action/start/' + host_id + '/' + proc_name,
                success: function(response) {
                    window.location.reload();
                }
            }); 
        });

        //stop button click handler
        $('td > button[action="stop-proc"]').click(function () {
            host_id = $(this).attr('host-id');
            proc_name = $(this).attr('proc-name');

            $.ajax({
                type: "POST",
                url: '/action/stop/' + host_id + '/' + proc_name,
                success: function(response) {
                    window.location.reload();
                }
            });
        });
  
        //restart button click handler
        $('td > button[action="restart-proc"]').click(function () {
            host_id = $(this).attr('host-id');
            proc_name = $(this).attr('proc-name');

            $.ajax({
                type: "POST",
                url: '/action/restart/' + host_id + '/' + proc_name,
                success: function(response) {
                    window.location.reload();
                }
            });
        
        });

        //edit button click handler
        $('td > button[action="edit"]').click(function () {
            host_id = $(this).attr('host-id');
            proc_name = $(this).attr('proc-name');

            //hide alert
            $("#edit-config-alert").hide();

            $.ajax({
                type: "GET",
                url: '/config/' + host_id + '/' + proc_name,
                dataType: "json",
                success: function (response) {
              
                    //assign variables
                    $("#edit-config-value-textarea").val(response)

                    //disable refresh
                    enable_refresh = false;
                 
                    //show
                    $('#edit-config-modal').modal('show');
                }
            });
        });

        //config edit save
        $("#edit-config-modal-save").click(function() {
            var config = {};
            config.data = $("#edit-config-value-textarea").val();

            //get service name from config
            var patt = /check \w+ (\w+)/i;
            var match_result = config.data.match(patt);
            
            if (match_result == null){
                 //show alert
                $("#edit-config-alert").empty();
                $("#edit-config-alert").append('configuration syntax invalid');
                $("#edit-config-alert").show();
                return;
            }
   
            $.ajax({
                type: "POST",
                url: '/config/' + host_id + '/' + match_result[1],
                data: config,
                dataType: 'json',
                success: function(response) {
                    if (response.success)
                        setTimeout(function(){window.location.reload();},1000); //sleep to let monit reload
                    else{
                        //show alert
                        $("#edit-config-alert").empty();
                        $("#edit-config-alert").append(response.message);
                        $("#edit-config-alert").show();
                    }
                }
            });
        });

        //add button click handler
        $('#add-monit-config').click(function () {
            host_id = $(this).attr('host-id');
           
             //hide alert
            $("#add-config-alert").hide();

            //assign default variables
            $("#add-config-value-textarea").val("check process sshd with pidfile /var/run/sshd.pid\r\n\tif changed pid then alert\r\n");

            //disable refresh
            enable_refresh = false;
          
            //show
            $('#add-config-modal').modal('show');

        });

        //add config
        $("#add-config-modal-save").click(function() {

            var config = {};
            config.data = $("#add-config-value-textarea").val();   

            //get service name from config
            var patt = /check \w+ (\w+)/i;
            var match_result = config.data.match(patt);
            
            if (match_result == null){
                 //show alert
                $("#add-config-alert").empty();
                $("#add-config-alert").append('configuration syntax invalid');
                $("#add-config-alert").show();
                return;
            }
 
            $.ajax({
                type: "POST",
                url: '/config/' + host_id + '/' + match_result[1],
                data: config,
                dataType: 'json',
                success: function(response) {
                    if (response.success)
                        setTimeout(function(){window.location.reload();},1000); //sleep to let monit reload
                    else{
                         //show alert
                        $("#add-config-alert").empty();
                        $("#add-config-alert").append(response.message);
                        $("#add-config-alert").show();
                    }
                }
            });
        });

        //config delete click handler
        $('button[action="delete-config"]').click(function() {
            $('#confirmation-delete-alert').hide();
            $('#confirmation-delete-modal').modal('show');
        });

        //delete confirmation confirm
        $("#continue-delete-button").click(function() {
            //send DELETE
            $.ajax({
                type: 'DELETE',
                url: '/config/' + host_id + '/' + proc_name,
                dataType: "json",
                success: function(response) {
                    if (response.success)
                        setTimeout(function(){window.location.reload();},1000); //sleep to let monit reload
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

