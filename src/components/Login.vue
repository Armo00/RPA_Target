<template>
    <div>
        <div class="login_container">
            <div class="background">
                <img src="../assets/login_BG.jpg" width="100%" alt="" />
            </div>
            <div class="login_box"></div>
            <div class="login_box2">
                <!--头像-->
                <div class="avatar_box">
                    <img src="../assets/shu.jpg" alt="" />
                </div>
                <!--表单-->
                <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="0px" class="login_form">
                    <!--UserName-->
                    <el-form-item label="" prop="username">
                        <el-input v-model="loginForm.username" prefix-icon="el-icon-user"></el-input>
                    </el-form-item>
                    <!--PassWord-->
                    <el-form-item label="" prop="password">
                        <el-input v-model="loginForm.password" prefix-icon="el-icon-lock"
                                  type="password"></el-input>
                    </el-form-item>
                    <!--Button-->
                    <el-form-item class="btns">
                        <el-button type="primary" @click="login">登录</el-button>
                        <el-button type="info" @click="resetLoginForm">注册</el-button>
                    </el-form-item>
                </el-form>
            </div>

        </div>
        <div class="thanks">
            This is an RPA Demo system, developed by NEXT Aerospace
        </div>
        <div class="thanks">
            Copyright 2020-2021 NEXT Aerospace. All rights reserved.
        </div>
    </div>

        
</template>


<script>export default {
        data() {
        return {
            serverUrl: '121.5.27.218:9999',
            //serverUrl:'127.0.0.1:9999',
            loginForm: {
                Mode:'0',
                username: '',
                password: '',
            },
   
            //This is the input rule for the form
            loginFormRules: {
                username: [{ required: true, message: '请输入用户名', trigger: 'blur' },],
                password: [{ required: true, message: '请输入密码', trigger: 'blur' },]
            },

        }
        },
        mounted: function () {
            document.title = '登录';
            window.sessionStorage.setItem('serverUrl', this.serverUrl);
        },
        
        methods: {


            //Reset Login Form
            resetLoginForm() {
                window.sessionStorage.setItem('token', 'temp');
                this.$router.push('/register')

            },
            login() {
                this.$refs.loginFormRef.validate(valid => {
                    if (!valid) return;
                    
                    window.sessionStorage.setItem('Username', this.loginForm.username);
                    var sendData = { Mode: '0', username: this.loginForm.username, password: this.loginForm.password };
                    const result = this.$http.post('http://' + this.serverUrl+'/login', sendData).then(res => {
                        //console.log(res);
                        if (res.data.return_code == 8000) return this.$message.error('用户名错误');
                        if (res.data.return_code == 8001) return this.$message.error('密码错误');
                        if (res.data.return_code == 8100) return this.$message.error(res.data.return_info);
                        if (res.data.return_code == 9000) return this.$message.error(res.data.result);
                        if (res.data.return_code == 20001) {
                            window.sessionStorage.setItem('token', res.data.token);
                            //this.$message.success(res.data.return_info);
                            //console.log(res.data.token);
                            this.$router.push('/admin');
                            return;
                        };
                        if (res.data.return_code == 200) {
                            this.$message.success('登陆成功！');
                            window.sessionStorage.setItem('token', res.data.token);
                            window.sessionStorage.setItem('Username', res.data.username);
                            window.sessionStorage.setItem('allHub', res.data.allHub);
                            this.$router.push('/home');
                        } else {
                            this.$message.error('发生错误！！');
                        }
                        
                    });

                });

            }
        }
}</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
    .login_container{
        background-color: #2b4b6b;
        height: 100%;
    }
    .thanks {
        transform: translate(0%,5100%);
    }
    .login_box {
        width: 450px;
        height: 300px;
        background-color:#fff;
        border-radius: 30px;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%,-50%);
        opacity: 0.8;
    }
    .login_box2 {
        width: 450px;
        height: 300px;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%,-50%);
        transform: translate(-50%,-50%);

    }
    .avatar_box {
        height: 130px;
        width: 130px;
        border: 3px solid #eee;
        border-radius: 50%;
        padding: 10px;
        box-shadow: 0 0 10px #ddd;
        position: absolute;
        left: 50%;
        transform: translate(-50%,-50%);
        background-color: #fff;
        img{
               width:100%;
               height:100%;
               border-radius:50%;
               background-color: #eee;

           }  
    }
    .btns{
        display:flex;
        justify-content:flex-end;
    }
    .login_form{
        position:absolute;
        bottom:0;
        width:100%;
        padding:0 20px;
        box-sizing:border-box;
    }
    .background {
        width: 100%;
        height: 100%; /**宽高100%是为了图片铺满屏幕 */
        z-index: -1;
        position: absolute;
    }
</style>
