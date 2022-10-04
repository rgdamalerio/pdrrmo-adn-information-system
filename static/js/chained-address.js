function getBarangay(mun_id) {
  let $ = django.jQuery;
  $.get('/address/barangay/' + mun_id +'/', function (resp){
      let barangay_list = '<option value="" selected="">---------</option>'
      $.each(resp.data, function(i, item){
        barangay_list += '<option value="'+ item.psgccode +'">'+ item.brgyname +'</option>'
      });
      $('#id_barangay').html(barangay_list);
  });
}

function getBarangay_custom_form(mun_id) {
  $.get('/address/barangay/' + mun_id +'/', function (resp){
      let barangay_list = '<option value="" selected="">---------</option>'
      $.each(resp.data, function(i, item){
        barangay_list += '<option value="'+ item.psgccode +'">'+ item.brgyname +'</option>'
      });
      $('#id_barangay').html(barangay_list);
  });
}