$(document).ready(function() {
	contact.initEventHandlers();
});
var contact = {
    initEventHandlers : function() {
        //clicking the submit form
        $("#subContact").bind('click',function(event){
            $("#loader").show();
            setTimeout('contact.ContactFormSubmit()',500);
        });
        //remove messages when user wants to correct (focus on the input)
        $(".inplaceError",$("#ContactForm")).bind('focus',function(){
            var $this = $(this);
            var $error_elem = $this.next();
            if($error_elem.length){
                $error_elem.fadeOut(function(){$(this).empty()});
            }
            $("#success_message").empty();
        });
        //user presses enter - submits form
        $("#ContactForm input,#ContactForm textarea").keypress(function (e) {
            if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
                $("#subContact").click();
                return false;
            }
            else{
                return true;
            }
        });
    },
    ContactFormSubmit : function() {
        $.ajax({type : 'POST',
            url : 'contact_exec.php',
            dataType : 'json',
            data : $("#ContactForm").serialize(),
            success : function(data,textStatus){
                //hide the ajax loader
                $("#loader").hide();
                if(data.result == '1'){
                    //show success message
                    $("#success_message").empty().html('Message sent').fadeIn();
                    //reset all form fields
                    //$("#ContactForm").reset();
                    $("#ContactForm").clearForm();
                  }
                  else if(data.result == '-1'){
                      for(var i=0; i < data.errors.length; ++i ){
                          if(data.errors[i].value!=''){
                            $("#"+data.errors[i].name).next().html('<span>'+data.errors[i].value+'</span>').fadeIn();
                            //alert(data.errors[i].value);
                          }
                      }
                  }
                  else{
                      alert("Unknown error returned!");
                  }
            },
            error : function(data,textStatus,errorThrown){
                alert("Submit Error!  " + errorThrown);
            }
        });
    }
};