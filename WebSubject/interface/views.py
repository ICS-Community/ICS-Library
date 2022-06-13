from django.shortcuts import render
from interface.models import Tag

def search(request):
    if request.method == 'GET':
        tags = Tag.objects.all() # 获取tags列表
        return render(request, 'interface/search.html', {'tags': tags})
    elif request.method == 'POST':
        content = request.POST.get('content', None)
        # 获取复选框的值,是一个选中的数组
        tags = request.POST.getlist('tags')
        