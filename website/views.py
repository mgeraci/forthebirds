from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404

from utils.http import http_response_ok
from website.models import User, UploadedImage


def home(request):
    """Render the homepage."""
    return render(request, 'home.html', {})


def about(request):
    """Render the About Laura page."""
    laura = get_object_or_404(User, username='laura')
    context = {
        'laura': laura,
    }
    return render(request, 'about.html', context)


@login_required
def uploaded_images(request):
    images = UploadedImage.objects.filter(user=request.user).order_by(
        '-time_uploaded')
    context = {'images': images}
    return render(request, 'uploaded_images.html', context)


def try_old_website(request, path):
    """
    Before returning a 404 page not found, check if path is at old website.
    """
    url = settings.OLD_SITE_DOMAIN + '/' + path

    if http_response_ok(url):
        return HttpResponsePermanentRedirect(url)
    else:
        raise Http404
