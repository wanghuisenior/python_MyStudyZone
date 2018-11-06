



var url = window.location.href;
var hash = url.substring(url.indexOf("#") + 1);

if (hash === url) {
    hash = 'home';
}

$('section').load('includes/' + hash + '.html');

$('header').load('includes/header.html');
$('footer').load('includes/footer.html');