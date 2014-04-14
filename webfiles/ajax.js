function ajax(url, data, callback) {
    var req = false;
    req = new XMLHttpRequest();
    req.open('POST', url, true);
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            callback( JSON.parse(req.responseText) );
        }
    }
    req.send(data);
}

function feelings() {
    $('#results').css('opacity',0);
    $('#twitter').css('opacity',0);
    $('#bing').css('opacity',0);
    ajax('/feelings', document.search.query.value, function (obj) {
        twitter(obj['focus']);
        bing(obj['focus']);
        document.getElementById('firstEmotion').innerHTML = obj['emotion'];
        document.getElementById('firstObject').innerHTML = obj['focus'];
        $('.subject').text(obj['focus']);
        $('#resultImage').attr('src', obj['image'][0] );
        $('#results').animate({
            opacity: '1'
        },1500);
    });
}
function twitter(s) {    
    ajax('/twitter', s, function (obj) {
        document.getElementById('twitterEmotion').innerHTML = obj['emotion'];
        console.log(obj);
        $('#tweets').empty();
        obj['tweets'].forEach(function(elt) {
            $('#tweets').append('<span class="tweet">'+elt[0]+'</span><span class="emotn">'+elt[1]+'</span>');
        });
        $('#twitter').animate({
            opacity: '1'
        },1500);
    });
}
function bing(s) { 
    ajax('/bing', s, function (obj) {
        if ( obj['score'] >= 0 ) {
            document.getElementById('thumbs').src = 'webfiles/Facebook-thumbs-up.png';
            document.getElementById('bingSentiment').innerHTML = 'up';
        } else {
            document.getElementById('thumbs').src = 'webfiles/Facebook-thumbs-down.png';
            document.getElementById('bingSentiment').innerHTML = 'down';
        }
        $('#bing').animate({
            opacity: '1'
        },1500);
    });
}

window.onload = function() {


};
