// Page Javascripts here
$(function () {

   const params = {
      // "level": "2",
      "fields": ["id", "name", "code"]
   };

   const url = "/dashboard/indicators";

   // Send a get request to server
   $.ajax({
      url: url,
      data: JSON.stringify({
         "kind": "",
         "payload": params
      }),
      dataType: "json",
      type: "POST",

      contentType: "application/json",

      error: function(xhr, textStatus, message) {
         console.log(xhr.status + " " + message)
      },
      success: function(json) {
         // console.log(json)
         $.each(json.indicators, function(key, val) {
            $("#data-indicators").append('<option value="' + val.id + '">' + val.name + '</option>');
         });
      }
   });

   $("select#levels").change(function() {
      let level = $("select#levels option:selected").val();

      $(".lv-wrapper .data-selected").html("");
      $.ajax({
         url: "/dashboard/organisationUnits",
         data: JSON.stringify({
            "payload": {
               "level": level
            }
         }),
         dataType: "json",
         type: "POST",

         contentType: "application/json",

         error: function(xhr, textStatus, message) {
            console.log(xhr.status + " " + message)
         },
         success: function(json) {
            // console.log(json);
            $.each(json.organisationUnits, function(key, val) {
               let checkbox = '<input class="check-data" type="checkbox" name="'+ val.id +'"/>';

               $(".lv-wrapper .data-selected").append('<li class="list-group-item">'+ val.name + checkbox +'</li>');
            });

            /**
             * On even list element is clicked
            * Add class active to it
            * Remove class active from other one
            */
            $(".data-selected li").on("click", function() {
               $(".data-selected li.active").removeClass("active");
               $(this).addClass("active");

               // Toggle check true and false when clicked
               let checkbox = $(this).find('input[type="checkbox"]');
               checkbox.attr("checked", !checkbox.attr("checked"))
               // checkbox.attr('checked', !$checkbox.attr('checked'))
            });
         }
      });
   });

   /**
    * On event that the options change
    * Add element to selected indicators
    */
   $("#data-indicators").change(function() {
      let data_id = $("#data-indicators option:selected").val();
      let data_text = $("#data-indicators option:selected").text();

      $(".av-wrapper .data-selected").append('<li data-id="'+ data_id +'" class="data-av list-group-item">'+ data_text +'</li>');

      /**
       * On even list element is clicked
       * Add class active to it
       * Remove class active from other one
       */
      $(".data-selected li").on("click", function() {
         $(".data-selected li.active").removeClass("active");
         $(this).addClass("active");
      });
      
   });

});