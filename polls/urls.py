from django.urls import path
from . import views

urlpatterns = [
    # ex:/polls/
    path('',views.index, name='index'),
    # ex:/polls/5
    # the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/',views.detail, name='detail'),
    # ex:/polls/specifics/5
    # added the word 'specifics'
    # 如果你想改变投票详情视图的 URL，比如想改成 polls/specifics/12/ ，
    # 你不用在模板里修改任何东西（包括其它模板），
    # 只要在 polls/urls.py 里稍微修改一下就行：
    # 去除index.html模板中的硬编码后，注释掉上一个url的话，index的跳转行不通
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex:/polls/5/results
    path('<int:question_id>/results/',views.results, name='results'),
    # ex:/polls/5/vote
    path('<int:question_id>/vote/',views.vote, name='vote'),
]