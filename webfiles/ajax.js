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
        obj['tweets'].forEach(function(elt) {
            $('#tweetA').append('<p>'+elt+'</p>');
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
    console.log('loaded'); 
};
