function signOut() {
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
