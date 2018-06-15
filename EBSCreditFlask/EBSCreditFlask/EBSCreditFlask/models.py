#coding:utf-8
import peewee
import datetime

db = peewee.MySQLDatabase(database = 'ebscreditdb',# string
    passwd = '123456', # string
    user = 'root', # string
    host = 'localhost', # string
    port = 3306, # int, 可不写
)

class BaseModel(peewee.Model):
    class Meta:
        database = db

class SoftDeleteModel(peewee.Model):
    IsDel = peewee.BooleanField(default=False)

class CreationAuditedModel(peewee.Model):    
    CreateUserId = peewee.IntegerField(null=True)
    CreateTime = peewee.DateTimeField(default=datetime.datetime.now())

class UpdateAuditedModel(peewee.Model):
    UpdateUserId = peewee.IntegerField(null=True)
    UpdateTime = peewee.DateTimeField(null=True)

class AuditedModel(CreationAuditedModel,UpdateAuditedModel):
    pass

class AuditedAllModel(AuditedModel,SoftDeleteModel):
    pass

""" 用户信息表 """
class UserInfo(BaseModel,AuditedAllModel):
    """description of class"""
    Name = peewee.CharField(max_length=50)
    WorkNo = peewee.CharField(max_length=50)
    Accout = peewee.CharField(max_length=50)
    Password = peewee.CharField(max_length=50)
    Email = peewee.CharField(max_length=50)
    RoleId = peewee.IntegerField()
    Mobile = peewee.CharField(max_length=50)
    IsActive = peewee.BooleanField(default=False)
    RoleName = peewee.CharField(max_length=50)
    # CreateTime = peewee.DateTimeField(default=datetime.now())
    # CreateUserId = peewee.IntegerField(null=True)
    # UpdateUserId = peewee.IntegerField(null=True)
    # UpdateTime = peewee.DateTimeField(null=True)
    # IsDel = peewee.BooleanField(default=False)
    IsOnline = peewee.BooleanField(default=False)
    LastUpdatePwdTime = peewee.DateTimeField(null=True)
    UserPostId = peewee.CharField(max_length=50,null=True)
    UserPostLevel = peewee.CharField(max_length=50,null=True)
    DeptId = peewee.IntegerField(null=True)
    DeptName = peewee.CharField(max_length=50,null=True)


""" 用户登录日志 """
class UserLoginLog(BaseModel):
    UserID = peewee.IntegerField()
    LoginIP = peewee.CharField(max_length=50,null=True)
    IsDel = peewee.BooleanField(default=False)
    LoginTime = peewee.DateTimeField(null=True)

""" 角色信息 """
class Role(BaseModel,AuditedAllModel):
    RoleName = peewee.CharField(max_length=100)
    Authorities = peewee.TextField()
    #CreateTime = peewee.DateTimeField(default=datetime.now())
    #LastUpdatePwdTime = peewee.DateTimeField(null=True)
    #CreateUserId = peewee.IntegerField(null=True)
    #UpdateUserId = peewee.IntegerField(null=True)
    #IsDel = peewee.BooleanField(default=False)
    MaxAssignCount = peewee.IntegerField()
    MaxObtainCount = peewee.IntegerField()
    MaxCount = peewee.IntegerField()
    Remark = peewee.CharField(max_length = 100)

""" 部门信息 """
class Dept(BaseModel,AuditedAllModel):
    DeptCode = peewee.CharField(max_length=50)
    DeptName = peewee.CharField(max_length=100)
    DeptDesc = peewee.TextField()   
    OrderNo = peewee.IntegerField()

""" 用户与部门关系表 """
class DeptUsers(BaseModel,SoftDeleteModel):    
    DeptID = peewee.IntegerField()
    UserID = peewee.IntegerField()

""" 权限信息 """
class AuthorityInfo(BaseModel,AuditedAllModel):
    NodeID = peewee.IntegerField()
    ParentNodeID = peewee.ForeignKeyField('self',related_name='children', null=True)
    NodeType = peewee.IntegerField()
    AuthorityCode = peewee.CharField(max_length=50)
    NodeName = peewee.CharField(max_length=50)
    PageUrl = peewee.CharField(max_length=100)
    ActionName = peewee.CharField(max_length=100)
    OrderNo = peewee.IntegerField()
    NodeTag = peewee.IntegerField(null=True)

""" 角色与权限关系表 """
class RoleAuthority(BaseModel,SoftDeleteModel):
    AuthorityCode = peewee.CharField(max_length=50)
    RoleID = peewee.IntegerField()
   
""" 数据字典表 """
class SysDic(BaseModel,SoftDeleteModel):
    DicName = peewee.CharField(max_length=50)
    DicType = peewee.IntegerField()
    OrderNum = peewee.IntegerField()
    Remark = peewee.CharField(max_length = 100)

""" 数据字典子项目表 """
class SysDicItem(BaseModel,SoftDeleteModel):
    DicID =  peewee.ForeignKeyField(SysDic, related_name='SysDic',on_delete='CASCADE') #peewee.IntegerField()
    SuperItemID = peewee.IntegerField()
    ItemName = peewee.CharField(max_length = 100)
    ItemValue = peewee.CharField(max_length=50)    
    OrderNum = peewee.IntegerField()
    Remark = peewee.CharField(max_length = 100)
  
""" 企业主体信息表 """
class PreMainForm(BaseModel,AuditedAllModel):
    CreditNum = peewee.CharField(max_length=30)
    EntName = peewee.CharField(max_length=200) 
    WebsiteName = peewee.CharField(max_length=200) 
    WebsiteAddress = peewee.CharField(max_length=250)
    WebLogoAddress = peewee.CharField(max_length=250)
    IndustryID = peewee.IntegerField(null=True)
    ScoreAhead = peewee.DoubleField(null=True)
    ScoreCurrent = peewee.DoubleField(null=True)
    AuditState = peewee.IntegerField(null=True)
    AuditUserID = peewee.IntegerField(null=True)
    State = peewee.IntegerField(null=True)
    AuditTime = peewee.DateTimeField(null=True)
    EntRegNo = peewee.CharField(max_length=50)
    EntOrgCode = peewee.CharField(max_length=20)
    EntSccCode = peewee.CharField(max_length=20)
    RegCap = peewee.CharField(max_length=50)
    EstDate = peewee.DateTimeField(null=True)
    Brand = peewee.CharField(max_length=50)
    ProvinceID = peewee.CharField(max_length=10)
    CityID = peewee.CharField(max_length=10)
    AreaID = peewee.CharField(max_length=10)

""" 模型信息表 """
class PreModel(BaseModel,AuditedAllModel):
    ModelName = peewee.CharField(max_length=50)
    ModelState = peewee.IntegerField(null=True)
    ModelApplyState = peewee.IntegerField(null=True)
    ReCreditState = peewee.IntegerField()

""" 模型与指标关系表 """
class PreModelTarget(BaseModel,AuditedAllModel):
    TargetName = peewee.CharField(max_length=50)
    TargetCode = peewee.CharField(max_length=50)
    TargetID = peewee.IntegerField(null=True)
    ParentTargetID = peewee.IntegerField(null=True)
    TargetWeight = peewee.DoubleField(null=True)
    TargetLevel = peewee.IntegerField(null=True)
    Remark = peewee.CharField(max_length=500)
    ModelID = peewee.IntegerField(null=True)


if __name__ == "__main__":
    UserInfo.create_table()
    UserLoginLog.create_table()
    Role.create_table()
    Dept.create_table()
    DeptUsers.create_table()
    AuthorityInfo.create_table()
    RoleAuthority.create_table()
    SysDic.create_table()
    SysDicItem.create_table()
    PreMainForm.create_table()
    PreModel.create_table()
    PreModelTarget.create_table()