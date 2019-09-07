function checkValidAndOTP(){
    phone = $('#phone').val()
    pin = $('#pin').val()
    var url = '/atm/checkValidAndOTP/'
    $.ajax({
        type: "POST",
        url : url,
        data:{
            phone: phone,
            pin: pin,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success : function(status) {
            console.log(status)
            if (status){
                $('.form-control')[0].disabled = true
                $('.form-control')[1].disabled = true
                $("#btnSubmit").attr("disabled",true)
                $('.container').append('<input id="otp" type="text" class="form-control" name="otp" placeholder="Enter your 6 digit OTP">')
                $('.container').append('<button id="btnOTP" onClick="verifyOTP()" type="button" class="btn btn-primary" >Submit OTP</button>')
            }
            else{
                alert("Phone number does not exits or invalid pin")
            }
        },
    })
    
}

function verifyOTP(){
    otp = $('#otp').val()
    phone = $('#phone').val()
    var url = '/atm/verifyOTP/'
    $.ajax({
        type: "POST",
        url : url,
        data:{
            phone: phone,
            otp: otp,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        before : function(){
            $('#otp').attr("disabled",true)
            $('#btnOTP').attr("disabled",true)
        },
        success : function(status) {
            window.location.replace("http://localhost:9000/atm/card/");
        },
    })
}
