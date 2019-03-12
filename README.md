
#在settings添加样式路径，否则查询不到static下包的路径
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static"),
]

#注意使用media时需要注意

与用户上传相关的配置，否则用户无法从外部访问
MEDIA_ROOT = os.path.join(BASE_DIR,"media")#配置media存放路径
MEDIA_URL = "/media/"#配置外部访问media权限

在url中配置
re_path(r'media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT})