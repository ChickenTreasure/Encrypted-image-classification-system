<template>
  <div class="login_container">
    <div class="snow-container">
        <div class="snow foreground"></div>
        <div class="snow foreground layered"></div>
        <div class="snow middleground"></div>
        <div class="snow middleground layered"></div>
        <div class="snow background"></div>
        <div class="snow background layered"></div>
    </div>
    <div class="login_box">
        <!-- 头像区域 -->
        <div class="avatar_box">
            <img src="../assets/logo.png" alt="">
        </div>
        <!-- 登录表单区域 -->
        <el-form ref="loginFormRef" :model="loginForm" :rules="loginFormRules" label-width="80px" class="login_form">
            <!-- 账号 -->
            <el-form-item label="账号" prop="username">
                <el-input v-model="loginForm.username"></el-input>
            </el-form-item>
            <!-- 密码 -->
            <el-form-item label="密码" prop="password">
                <el-input v-model="loginForm.password" type="password"></el-input>
            </el-form-item>
            <!-- 按钮区域 -->
            <div @click="login" class="submit-w3l">
                <input type="submit" value="登录">
            </div>
            
        </el-form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
    data(){
        return{
        //这是登录表单的数据绑定对象
        loginForm:{
            username: 'admin',
            password: '123456'
        },
        //这是表单的验证规则对象
        loginFormRules:{
            //验证用户名是否合法
            username: [ 
                { required: true, message:"请输入账号", trigger: "blur"},
                { min: 5, max: 10, message: '长度在 5 到 10 个字符', trigger: 'blur' }
            ],

            //验证密码是否合法
            password: [
            { required: true, message:"请输入登录密码", trigger: "blur"},
            { min: 3, max: 15, message: '长度在 3 到 15 个字符', trigger: 'blur' }  
            ]
        }
        }
        },
        methods: {
            login(){
                this.$refs.loginFormRef.validate(async valid =>{
                    if(!valid) return;
                    this.$router.replace('/search');
                })
            }
        }
    }
</script>

<style lang="less" scoped>
.snow-container {
  position: absolute;
  height:100%;
  width: 100%;
  max-width: 100%;
      height: 100%;
  top: 0;
  overflow: hidden;
  z-index: 2;
  pointer-events: none;
  background-color: #1b2b3b;
  opacity: .2;
}
.snow-container.two {
    height: 440px;
}
.snow {
  display: block;
  position: absolute;
  z-index: 2;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  pointer-events: none;
  -webkit-transform: translate3d(0, -100%, 0);
          transform: translate3d(0, -100%, 0);
  -webkit-animation: snow linear infinite;
          animation: snow linear infinite;
}
.snow.foreground {
  background-image: url("../assets/images/1.png");
  -webkit-animation-duration: 15s;
          animation-duration: 15s;
}
.snow.foreground.layered {
  -webkit-animation-delay: 7.5s;
          animation-delay: 7.5s;
}
.snow.middleground {
  background-image: url("../assets/images/2.png");
  -webkit-animation-duration: 20s;
          animation-duration: 20s;
}
.snow.middleground.layered {
  -webkit-animation-delay: 10s;
          animation-delay: 10s;
}
.snow.background {
  background-image: url("../assets/images/3.png");
  -webkit-animation-duration: 30s;
          animation-duration: 30s;
}
.snow.background.layered {
  -webkit-animation-delay: 15s;
          animation-delay: 15s;
}

@-webkit-keyframes snow {
  0% {
    -webkit-transform: translate3d(0, -100%, 0);
            transform: translate3d(0, -100%, 0);
  }
  100% {
    -webkit-transform: translate3d(15%, 100%, 0);
            transform: translate3d(15%, 100%, 0);
  }
}

@keyframes snow {
  0% {
    -webkit-transform: translate3d(0, -100%, 0);
            transform: translate3d(0, -100%, 0);
  }
  100% {
    -webkit-transform: translate3d(15%, 100%, 0);
            transform: translate3d(15%, 100%, 0);
  }
}

@media (max-width: 1366px){
  .snow-container {
		position: absolute;
		height: 628px;
	}
	
}
@media (max-width:1280px){
	.snow-container {
		position: absolute;
		height: 578px;
	}
}
@media (max-width:1080px){
	.snow-container {
		position: absolute;
		height: 498px;
	}
}
@media (max-width:1054px){
	
}
@media (max-width:1024px){

}
@media (max-width:991px){
	.snow-container.two {
		height: 365px;
	}

}
@media (max-width:800px){

	.snow-container {
		position: absolute;
		height: 375px;
	}
	.snow-container.two {
		height: 352px;
	}
}
@media (max-width:768px){
	.snow-container {
		position: absolute;
		height: 373px;
	}
}
@media (max-width:640px){
	
}
@media (max-width: 480px){
	
}
@media (max-width: 414px){

}
@media (max-width: 384px){

}

.login_container{
    background-color: #2b4b6b;
    height: 100%;
    position: relative;
    background-image: url(../assets/bg.jpg);
}

.login_box{
    width: 450px;
    height: 300px;
    background-color: #fff;
    border-radius: 4px;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
}

.avatar_box{
    height: 130px;
    width: 130px;
    border: 1px solid #eee;
    border-radius: 50%;
    padding: 10px;
    box-shadow: 0 0 10px #ddd;
    position: absolute;
    left: 50%;
    transform: translate(-50%,-50%);
    background-color: #fff;
    img{
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background-color: #fff;
    }
}

.submit-w3l input[type="submit"] {
    background: #ccc;
    color: #000;
    outline: none;
    display: block;
    margin: 0 auto;
    border: none;
    cursor: pointer;
    padding: 13px 38px;
    font-size: 14px;
    width: 50%;
    margin-top: 1em;
    font-weight: bold;
    text-transform: uppercase;
    transition: 0.3s all;
    -webkit-transition: 0.3s all;
    -moz-transition: 0.3s all;
    -o-transition: 0.3s all;
    -ms-transition: 0.3s all;
}

.submit-w3l input[type="submit"]:hover {
    background: #df5799;
    color: #ffffff;
    transition: 0.3s all;
    -webkit-transition: 0.3s all;
    -moz-transition: 0.3s all;
    -o-transition: 0.3s all;
    -ms-transition: 0.3s all;
}

.login_form{
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 30px 60px;
    box-sizing: border-box;
}
</style>