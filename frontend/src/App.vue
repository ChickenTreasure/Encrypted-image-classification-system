<template>
  <el-container>
    <!-- 顶部的bar -->
    <el-header style="height: 60px">
      <div style="display: flex; align-items: center;">
        <i class="el-icon-picture" style="margin-left: 1%;"></i>
        <span style="margin-left: 1%;font-weight: bold">Search what you want!</span>
        <el-menu default-active="/search" style="margin-left: 3%;" router mode="horizontal" background-color="#605051"
          text-color="#FCE8E8">
          <!-- active-text-color="#E6E6FA" -->
          <el-menu-item index="/">
            <i class="el-icon-star-off" style="margin-right: 8%"></i>
            <span slot="title" style="font-size: medium">登录</span>
          </el-menu-item>
          <el-menu-item index="/search">
            <i class="el-icon-search" style="margin-right: 8%"></i>
            <span slot="title" style="font-size: medium">图片分类search</span>
          </el-menu-item>
          <el-menu-item index="/collect">
            <i class="el-icon-star-off" style="margin-right: 8%"></i>
            <span slot="title" style="font-size: medium">模型结果show</span>
          </el-menu-item>
        </el-menu>
      </div>
    </el-header>
    <el-container>
      <el-container>
        <el-main> <router-view></router-view> </el-main>
        <!-- 底部的边框 -->
        <el-footer style="position:fixed;bottom:0px;width:100%;margin-left: 0px;">河北大学 20201204014 贾继宝</el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>
<script>
export default {
  name: "App",
};
</script>
<style scoped>
.el-main{
    height: 750px;
    margin: 0;
    padding: 0;
    min-width: 1366px;
    background-color: #B7CE73;
}

.el-header,
.el-footer {
  background-color: #605051;
  color: white;
}

.el-icon-picture {
  font-size: 1.5em;
}

.el-footer {
  line-height: 60px;
  text-align: center;
}
</style>
