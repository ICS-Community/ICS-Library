from django.http import Http404

def check_topic_owner(topic, request):
    if topic.author != request.user:
        raise Http404
