function ajax(url, data, callback) {
    var req = false;
    req = new XMLHttpRequest();
    req.open('POST', url, true);
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            callback(req);
        }
    }
    req.send(data);
}

function feelings() {
    twitter();
    bing();
    ajax('/feelings', document.search.query.value, function (req) {
        document.getElementById('firstEmotion').innerHTML = req.responseText;
    });
}
function twitter() {    
    ajax('/twitter', document.search.query.value, function (req) {
        document.getElementById('twitterEmotion').innerHTML = req.responseText;
    });
}
function bing() {    
    ajax('/bing', document.search.query.value, function (req) {
        document.getElementById('bingEmotion').innerHTML = req.responseText;
    });
}