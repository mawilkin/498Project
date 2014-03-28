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

function button() {
    var data = document.the_form.query.value;           
    ajax('input.html', data, function (req) {
        var elem = document.getElementById('result')
        elem.innerHTML = req.responseText
    });
}