from django.db import models


class CommonModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)  ## 수정일자
    updated_ate = models.DateTimeField(auto_now=True)  ## 생성일자

    class Meta:
        abstract = True  ##이 class django가 봐도 데이터 베이스에 저장하지 않는다.
