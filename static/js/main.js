$(document).ready(function () {

    $('#postForm').submit(function (e) {
        e.preventDefault();
        var url = '/make-a-post';
        var formData = new FormData(this);
        $.ajax({
            type: "post",
            url: url,
            data: formData,
            contentType: false,
            processData: false,
            success: function (response) {
                if (response.status){
                    console.log('post done successfully')
                    $('#postForm')[0].reset()
                    window.location.href='/';
                }else{
                    console.log('post not done error occured')
                }
            }
        });
    });
})