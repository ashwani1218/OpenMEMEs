function toRegistration(){
    window.location.href = "/registration"
}

function onSignIn(googleUser) {
    console.log("as")
    var profile = googleUser.getBasicProfile();
    console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
    console.log('Name: ' + profile.getName());
    console.log('Image URL: ' + profile.getImageUrl());
    console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
    
    $.ajax({
        type:'POST',
        data:{
            name:profile.getName(),
            email:profile.getEmail()
        },
        url:"/",
        success:function(data){
            console.log(data)
            //window.location.href = "/home"
            window.open("/home", "_self")
        },
        error: function(data){
            console.log(data)
        }
    });
}
  
