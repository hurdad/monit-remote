$(function () {
    $(document).ready(function () {

        var host_id;

        //refresh 60 s
        setTimeout(function () { 
            location.reload();
        }, 60 * 1000);

        //details button click handler
        $('td > button[action="detail-host"]').click(function () {
            host_id = $(this).attr('host-id');
            window.location = "details/" + host_id;
        });

        //edit button click handler
        $('td > button[action="edit-host"]').click(function () {
            host_id = $(this).attr('host-id');
     
            //hide alert
            $("#edit-host-alert").hide();

            $.ajax({
                type: "GET",
                url: '/host/' + $(this).attr('host-id'),
                dataType: "json",
                success: function (response) {
              
                    //assign variables
                    $("#edit-monit-httpd-url-text").val(response.monit_httpd_url);
                    $("#edit-monit-httpd-username-text").val(response.monit_httpd_username);
                    $("#edit-monit-httpd-password-text").val(response.monit_httpd_password);
                    $("#edit-monit-config-directory-text").val(response.monit_config_directory);
                    $("#edit-monit-binary-path-text").val(response.monit_binary_path);
                    $("#edit-ssh-ip-text").val(response.ssh_ip);
                    $("#edit-ssh-username-text").val(response.ssh_username);
                    $("#edit-ssh-private-key-text").val(response.ssh_private_key);

                    //show
                    $('#edit-host-modal').modal('show');
       
                }
            });
        });

        //host edit save
        $("#edit-host-modal-save").click(function() {

            var host = {};
            host.monit_httpd_url        = $("#edit-monit-httpd-url-text").val();    
            host.monit_httpd_username   = $("#edit-monit-httpd-username-text").val();
            host.monit_httpd_password   = $("#edit-monit-httpd-password-text").val();
            host.monit_config_directory = $("#edit-monit-config-directory-text").val();
            host.monit_binary_path      = $("#edit-monit-binary-path-text").val();
            host.ssh_ip                 = $("#edit-ssh-ip-text").val();
            host.ssh_username           = $("#edit-ssh-username-text").val();
            host.ssh_private_key        = $("#edit-ssh-private-key-text").val();

            $.ajax({
                type: "PUT",
                url: '/host/' + host_id,
                data: host,
                dataType: 'json',
                success: function(response) {
                    if (response.success)
                        window.location.reload();
                    else{
                        //show alert
                        $("#edit-host-alert").empty();
                        $("#edit-host-alert").append(response.message);
                        $("#edit-host-alert").show();
                    }
                }
            });
        });

        //add button click handler
        $('#add-monit-host').click(function () {
           
             //hide alert
            $("#add-host-alert").hide();

            //assign default variables
            $("#add-monit-httpd-url-text").val('http://localhost:2812');
            $("#add-monit-httpd-username-text").val('admin');
            $("#add-monit-httpd-password-text").val('monit');
            $("#add-monit-config-directory-text").val('/etc/monit.d/');
            $("#add-monit-binary-path-text").val('/usr/bin/monit');
            $("#add-ssh-ip-text").val('localhost');
            $("#add-ssh-username-text").val('root');
            $("#add-ssh-private-key-text").val('~/.ssh/id_rsa');

            //show
            $('#add-host-modal').modal('show');

        });

        //add host
        $("#add-host-modal-save").click(function() {

            var host = {};
            host.monit_httpd_url        = $("#add-monit-httpd-url-text").val();    
            host.monit_httpd_username   = $("#add-monit-httpd-username-text").val();
            host.monit_httpd_password   = $("#add-monit-httpd-password-text").val();
            host.monit_config_directory = $("#add-monit-config-directory-text").val();
            host.monit_binary_path      = $("#add-monit-binary-path-text").val();
            host.ssh_ip                 = $("#add-ssh-ip-text").val();
            host.ssh_username           = $("#add-ssh-username-text").val();
            host.ssh_private_key        = $("#add-ssh-private-key-text").val();

            $.ajax({
                type: "POST",
                url: '/host/add',
                data: host,
                dataType: 'json',
                success: function(response) {
                    if (response.success)
                        window.location.reload();
                    else{
                         //show alert
                        $("#add-host-alert").empty();
                        $("#add-host-alert").append(response.message);
                        $("#add-host-alert").show();
                    }
                }
            });
        });

        //host delete click handler
        $('button[action="delete-host"]').click(function() {
            $('#confirmation-delete-alert').hide();
            $('#confirmation-delete-modal').modal('show');
        });

        //delete confirmation confirm
        $("#continue-delete-button").click(function() {
            //send DELETE
            $.ajax({
                type: 'DELETE',
                url: '/host/' + host_id,
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

