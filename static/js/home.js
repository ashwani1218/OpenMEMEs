function signOut(path) {
    $.ajax({
        type:"GET",
        url:"/logout",
        success:(data)=>{
            if(path){
                window.location.href = path
            }
            console.log(data+"User Logged out")
            window.location.reload()
        },
        error:(e)=>{
            console.log(e)
        }
    })
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
        // TODO: Change the url to home after session is implemented.   
        window.open("/","_self");
    });

}
function gapiInit(){
    gapi.load('auth2', function() {
        gapi.auth2.init()  /* Ready. Make a call to gapi.auth2.init or some other API */
    });    
}

