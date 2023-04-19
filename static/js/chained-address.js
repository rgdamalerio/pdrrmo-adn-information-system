function getBarangay(mun_id) {
    $.get('/address/barangay/' + mun_id +'/', function (resp){
        let barangay_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
          barangay_list += '<option value="'+ item.psgccode +'">'+ item.brgyname +'</option>'
        });
        $('#id_barangay').html(barangay_list);
    });
  }
  
  
function getPurok(barangay_id) {
    $.get('/address/purok/' + barangay_id +'/', function (resp){
        let purok_list = '<option value="" selected="">---------</option>'
        $.each(resp.data, function(i, item){
          purok_list += '<option value="'+ item.purok_id +'">'+ item.purok_name +'</option>'
        });
        $('#id_purok_id').html(purok_list);
    });
  }
  
