function validate(){
    if($("#new").val()==''){
        alert("Please provide Post text");
        return false;
    }
    else{
        return true;
    }
}