from django.db import models

class CustomPermission(models.Model):
    name = models.CharField('이름', max_length=16)
    parent = models.ForeignKey('CustomPermission', related_name='child_permissions', on_delete=models.CASCADE, verbose_name='부모 권한', blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        if self.parent and self.parent.parent:
            raise Exception('{} 는 이미 부모 권한을 갖고 있습니다. '.format(self.parent))

        super(CustomPermission, self).save()




class UserHasPermission(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='user_perms')
    permission = models.ForeignKey(CustomPermission, related_name='user_perms', on_delete=models.CASCADE)

    def __str__(self):
        return '사용자 {} -> 권한 {}'.format(self.user, self.permission)


def has_permissions(user, permission_name):
    # 권한 검사
    if user.user_perms.filter(permission__name=permission_name).count():
        return True

    # 자식 검사
    perm_list = list(map(lambda x: x.permission, user.user_perms.all()))
    for p in perm_list:
        if p.child_permissions and  p.child_permissions.filter(name=permission_name).count():
            return True

    return False


