
def test_login_codeE(login_page):
        # 场景1：正常登录（无错误）
    login_page.login("root", "123456@Aa", "1234",None,None,'验证码错误')
def test_login_passwordE(login_page):
   # 或者显式指定None
    login_page.login("root", "valid_pass", "1234", None, '密码(8-50位包含大小写字母,数字,无空格)', '验证码错误')
def test_login_usernameE(login_page):
   # 场景2：只有用户名错误
    login_page.login("", "123456@Aa", "1234", "请输入4-50位的账户(用户名)", None,'验证码错误')
def test_login_allE(login_page):
   # 场景4：所有字段都错误
    login_page.login("", "1", " ", "请输入4-50位的账户(用户名)", "密码长度至少为8位", "验证码错误")
