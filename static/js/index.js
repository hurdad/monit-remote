// Create a new YUI instance and populate it with the required modules.
YUI().use('datatable-sort', 'datatable-scroll', 'datatype', 'cssfonts', 
        'datasource-get', "datasource-jsonschema", "datatable-datasource",
    function (Y) {

    var url = "/status/summary?";   
    var ds = new Y.DataSource.Get( {source:url} );

    ds.plug( Y.Plugin.DataSourceJSONSchema, {
        schema: {
            metaFields: {total : "totalRecords" },
            resultListLocator: 'records',
            resultFields: [ 
                {
                    key: "id",
                    parser: "number"
                }, {
                    key: "led",
                    parser: "number"
                }, {
                    key: "hostname",
                    parser: "string"
                }, {
                    key: "cpu",
                    parser: "number"
                }, {
                    key: "mem",
                    parser: "number"
                }, {
                    key: "status",
                    parser: "string"
                }
            ]
        }
    });

    var ledFormatter = function (o) {
        o.innerHTML = '<img src="../../img/led' + o.data.led + '.png" class="led" alt="led">'
    };

/*
    var cpuFormatter = function (o) {
        var p = o.record.get("cpu");
        var n = o.record.get("statusid");
        var r = o.record.get("heartbeat");
        if (n != 1 && r == 1) {
            b(q).html('<div class="progress" title="' + (p > 0 ? p : 0) + '%"><div class="bar ' + (p <= 80 ? "bar-success" : p <= 95 ? "bar-warning" : "bar-danger") + '" style="width: ' + (p > 0 ? p : 0) + '%;"></div></div>')
        } else {
            b(q).html('<div class="progress" title="not available"><div class="bar bar-gray" style="width: 100%;"></div></div>')
        }
    };
  */ 

    var cols = [{
        key: "led",
        label: "*",
        sortable: true,
        formatter: ledFormatter
    }, {
        key: "hostname",
        label: "Host",
        sortable: true,
        formatter: "text"
    }, {
        key: "cpu",
        label: "%Cpu",
        sortable: true,
     //   formatter: h
    }, {
        key: "mem",
        label: "%Mem",
        sortable: true,
      //  formatter: l
    }, {
        key: "status",
        label: "Status",
        sortable: true,
        formatter: "text"
    }];

    var table = new Y.DataTable({
        columns: cols,
        sortable: true,
        height: '350px'
    });

    table.plug( Y.Plugin.DataTableDataSource, {
        datasource: ds,
        initialRequest: ''   // fires an initial request
    });

    table.render("#status");
});
