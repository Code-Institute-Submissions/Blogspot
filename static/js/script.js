$(document).ready(function () {
    $('#searchBtn').click(function () {
        $('#searchInput').toggleClass('d-none d-md-block').focus();
    });
});

function likeOrRedirect(slug) {
    if (user_authenticated) {
        likePost(slug);
    } else {
        window.location.href = "#";
    }
}

function dislikeOrRedirect(slug) {
    if (user_authenticated) {
        dislikePost(slug);
    } else {
        window.location.href = "#";
    }
}

function reportOrRedirect(slug) {
    if (user_authenticated) {
        reportPost(slug);
    } else {
        window.location.href = "#";
    }
}