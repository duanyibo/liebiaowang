from django.contrib import admin

# Register your models here.
from .models import City_info,Url_info,Users_info,Urls_info
from django.contrib import admin

# Register your models here.
import xadmin


xadmin.site.register(City_info)
xadmin.site.register(Url_info)
xadmin.site.register(Users_info)
xadmin.site.register(Urls_info)


from xadmin import views

# 基本的修改
class BaseSetting(object):
    enable_themes = True   # 打开主题功能
    use_bootswatch = True  #

# 针对全局的
class GlobalSettings(object):
    site_title = "列表系统管理"  # 系统名称
    site_footer = "++++++"      # 底部版权栏
    # menu_style = "accordion"     # 将菜单栏收起来


# 注册，注意一个是BaseAdminView，一个是CommAdminView
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
