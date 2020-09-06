$(function() {

  var arr = window.location.href.split("/");
  var api_url = arr[0] + "//" + arr[2]+'/bookapi/api/v1/posts/'
    load_posts()

    // Load all posts on page load
    function load_posts() {
        $.ajax({
            url : api_url, // the endpoint
            type : "GET", // http method
            // handle a successful response
            success : function(json) {
                for (var i = 0; i < json.length; i++) {
                    dateString = convert_to_readable_date(json[i].created)
                    $("#talk").prepend("<li id='post-"+json[i].id+"'><strong>"+json[i].name+
                        "</strong> - <em> "+json[i].author+"</em> - <span> "+dateString+
                        "</span> - <a id='delete-post-"+json[i].id+"'>delete me</a></li>");
                }
            },
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };



    // convert ugly date to human readable date
    function convert_to_readable_date(date_time_string) {
        var newDate = moment(date_time_string).format('MM/DD/YYYY, h:mm:ss a')
        return newDate
    }

    // Submit post on submit
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!")  // sanity check
        create_post();
    });

    // Delete post on click
    $("#talk").on('click', 'a[id^=delete-post-]', function(){
        var post_primary_key = $(this).attr('id').split('-')[2];
        console.log(post_primary_key) // sanity check
        delete_post(post_primary_key);
    });

    // AJAX for posting
    function create_post() {
        console.log("create post is working!") // sanity check
        $.ajax({
            url : api_url, // the endpoint
            type : "POST", // http method
            data : { the_post : $('#post-text').val(), }, // data sent with the post request
            // handle a successful response
            success : function(json) {
                var pname = $("#post-text").val();
                console.log(pname);
                $('#post-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                dateString = convert_to_readable_date(json.created)
                $("#talk").prepend("<li id='post-"+json.id+"'><strong>"+json.name+"</strong> - <em> "+
                    json.author+"</em> - <span> "+dateString+
                    "</span> - <a id='delete-post-"+json.id+"'>delete me</a></li>");
                console.log("success"); // another sanity check
            },

            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    };

    // AJAX for deleting
    function delete_post(post_primary_key){
        if (confirm('are you sure you want to remove this post?')==true){
            $.ajax({
                url : api_url+post_primary_key, // the endpoint
                type : "DELETE", // http method
                data : { postpk : post_primary_key }, // data sent with the delete request
                success : function(json) {
                    // hide the post
                  $('#post-'+post_primary_key).hide(); // hide the post on success
                  console.log("post deletion successful");
                },

                error : function(xhr,errmsg,err) {
                    // Show an error
                    $('#results').html("<div class='alert-box alert radius' data-alert>"+
                    "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        } else {
            return false;
        }
    };


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });



});
