django.jQuery(function() {
    var $ = django.jQuery;
    $("#id_country").change(function() {
        var $states = $("#id_state").empty();
        $.get(L10N.ajaxUrls.country_areas, { "country_id": $(this).val() }, 
              function(data) {
                  areas = JSON.parse(data);
                  for(var i = 0 ; i < areas.length ; i++) {
                      var area = areas[i];
                      $states.append("<option value='"+area.id+"'>"+area.name+"</option>");
                  }
              });
    });
});