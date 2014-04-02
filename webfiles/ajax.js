function ajax(url, data, callback) {
    var req = false;
    req = new XMLHttpRequest();
    req.open('POST', url, true);
    req.onreadystatechange = function() {
        if (req.readyState == 4) {
            callback(req);
        }
    }
    req.send(JSON.stringify(data));
}

function feelings() {
    twitter();
    var data = {
        query: document.search.query.value,
        which: 'feelings' 
    }        
    $('#feelings').animate({
        opacity: 1
    }, 2000);    
    ajax('input.html', data, function (req) {
        $('#feelings').animate({
            opacity:0
        }, 1000, function() {
            document.getElementById('feelings').innerHTML = req.responseText;
            $('#feelings').animate({
                opacity:1
            }, 1000);
        });
    });
}

function twitter() {
    var data = {
        query: document.search.query.value,
        which: 'twitter' 
    }       
    $('#twitter').animate({
        opacity: 1
    }, 2000);
    ajax('input.html', data, function (req) {
        $('#twitter').animate({
            opacity:0
        }, 1000, function() {
            document.getElementById('twitter').innerHTML = req.responseText;
            $('#twitter').animate({
                opacity:1
            }, 1000);
        });
    });
}

function bing() {
    var data = {
        query: document.search.query.value,
        which: 'bing' 
    }       
    $('#bing').animate({
        opacity: 1
    }, 2000);
    ajax('input.html', data, function (req) {
        $('#bing').animate({
            opacity:0
        }, 1000, function() {
            document.getElementById('bing').innerHTML = req.responseText;
            $('#bing').animate({
                opacity:1
            }, 1000);
        });
    });
}