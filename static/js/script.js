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

// JavaScript to handle comment deletion
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-comment-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const commentId = button.dataset.commentId;
            fetch(`/core/delete_comment/${commentId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({})
            })
            .then(response => {
                if (response.ok) {
                    // Reload the page or remove the deleted comment from the DOM
                    location.reload(); // Reload the page
                    // Alternatively, remove the deleted comment from the DOM
                    // const commentElement = button.closest('.media');
                    // commentElement.remove();
                } else {
                    console.error('Error deleting comment:', response.status);
                }
            })
            .catch(error => {
                console.error('Error deleting comment:', error);
            });
        });
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});