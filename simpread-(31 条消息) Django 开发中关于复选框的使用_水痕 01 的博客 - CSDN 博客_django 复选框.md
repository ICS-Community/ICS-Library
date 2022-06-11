> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/kuangshp128/article/details/75948310)

### 一、查询数据库[遍历](https://so.csdn.net/so/search?q=%E9%81%8D%E5%8E%86&spm=1001.2101.3001.7020)所有的复选框

*   1、`python`查询数据库所有的`tag`

```
# 新增文章
def add(request):
    if request.method == 'GET':
        tags = TagModel.objects.all()
        return render(request, 'books_add.html', {'tags': tags})
    elif request.method == 'POST':
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        blogModel = BlogModel(title=title, content=content, author=AuthorModel.objects.get(id=1))
        blogModel.save()
        # 获取复选框的值,是一个选中的数组
        tags = request.POST.getlist('tags')
        # 循环遍历所有选中的复选框,利用多对多的关系追加到数据库
        for tag in tags:
            blogModel.tag.add(tag)

        return HttpResponseRedirect('book_add')
    else:
        return HttpResponse(u'是不被处理的请求方式')
```

*   2、前端页面

```
<div class="form-group">
    <label class="col-sm-2 control-label">标签</label>
    <div class="col-sm-9">
        {% for tag in tags %}
            <label class="checkbox-inline">
                <input value="{{ tag.id }}" type="checkbox" />{{ tag.name }}
            </label>
        {% endfor %}
    </div>
</div>
```

*   3、进入编辑页面，先获取全部的复选框及选中的`id`

```
# 编辑博客
def edit(request, blog_id):
    tags = TagModel.objects.all()
    # 利用正向查找关于本博客选择的tag
    blogModel = BlogModel.objects.filter(id=blog_id).first()
    # 获取全部的tag
    check_tag = blogModel.tag.all()
    # 获取选中的id
    check_id = [int(x.id) for x in check_tag]
    print check_id
    return render(request, 'books_edit.html', {'tags': tags, 'check_id': check_id})
```

*   4、判断如果选中的就勾选

```
<div class="form-group">
    <label class="col-sm-2 control-label">标签</label>
    <div class="col-sm-9">
        {% for tag in tags %}
            {% if tag.id in check_id %}
                <label class="checkbox-inline">
                    <input value="{{ tag.id }}" type="checkbox" />{{ tag.name }}
                </label>
            {% else %}
                <label class="checkbox-inline">
                    <input value="{{ tag.id }}" type="checkbox" />{{ tag.name }}
                </label>
            {% endif %}
        {% endfor %}
    </div>
</div>
```

### 二、`ajax`提交的时候注意要把复选框转换字符串提交

*   1、前端代码

```
$('#btn').on('click', function (e) {
            // 设置空数组
            var hobby = [];
            $('#hobby-group').find('input[type=checkbox]').each(function () {
                if ($(this).prop("checked")) {
                    var hobbyId = $(this).val();
                    hobby.push(hobbyId);
                }
            })
            console.log(hobby);
            $.ajax({
                'url': '/ajaxpost/',
                'method': 'post',
                'data': {
                    'username': $('.username').val(),
                    'hobby': hobby
                },
                'traditional': true,
                'beforeSend': function (xhr, settings) {
                    var csrftoken = ajaxpost.getCookie('csrftoken');
                    //2.在header当中设置csrf_token的值
                    xhr.setRequestHeader('X-CSRFToken', csrftoken);
                },
                'success': function (data) {
                    console.log(data);
                }
            })
        })
```

*   2、后端代码

```
@require_http_methods(['POST'])
def ajaxpost(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username', None)
        # 获取复选框的值
        hobby = request.POST.getlist('hobby')
        print '*' * 100
        print hobby
        print '*' * 100
        return HttpResponse(u'成功')
    else:
        return HttpResponse(u'验证错误')
```