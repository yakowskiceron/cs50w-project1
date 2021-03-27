$(document).ready(function(){   
    
    $("#myform").submit(function(){
        var search = $("#books").val();

        if(search == '')
        {
            alert("Ingrese un nombre a buscar");
        }
        else{
            var url = '';
            var img='';
            var title='';
            var author='';

            $.get("https://www.googleapis.com/books/v1/volumes?=" + search,function(response){

                for(i=0;i<response.items.length; i++)
                {
                    title=$('<h5 class="center-align white-text">' + response.items[i].volumeInfo.title + '</h5>');
                }
            });
        }

    });
    
    return false;

});