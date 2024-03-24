<template>
  <div class="container">
    <div class="search-content">
      <div class="search-upload">
        <h3 class="search-content-title" style="display:inline-block;">点我上传图片哦～</h3>
        <!-- 上传图片的按钮 -->
        <el-upload :action=uploadUrl :limit="1" list-type="picture" :auto-upload="false" :multiple="false"
          :file-list="fileList" :on-success="uploadSuccess" :on-change="handleChange" :on-remove="handleRemove"
          accept="image/png, image/jpeg" ref="uploadRef" :class="fileList.length >= 1 ? 'styleA' : 'styleB'">
          <!-- 上传图片的按钮 -->
          <el-button size="medium" type="primary" style="display:inline-block;">
            <i slot="default" class="el-icon-plus" style="margin-right: 5%"></i>点击上传
          </el-button>
        </el-upload>
      </div>
      <!-- 显示上传的图片 -->
      <el-dialog :visible.sync="dialogVisible">
        <img width="70%" height="70%" :src="dialogImageUrl" alt="" />
      </el-dialog>
      <!-- 选择图片展示的数量 -->
      <el-row class="input-row">
        <div style="display: flex;">
          <div style="font-size: medium;font-weight: revert;width: 144px;position:relative;top:5px;">图像分类结果数:</div>
          <el-input-number style="margin-left: 1%;" size="small" v-model="num" :min="1" :max="9"></el-input-number>
          <!-- 搜索按钮 -->
          <el-button :disabled="fileList.length === 0 || isSearching" @click="searchRes"
            style="margin-top: 2%; z-index: 1000;margin-left: 2%;position:relative;top:-11px;" type="primary"><i
              :class="isSearching ? 'el-icon-loading' : 'el-icon-search'" style="margin-right: 5%;" />
            搜索</el-button>
        </div>
      </el-row>
    </div>


    <!-- 分割线 -->
    <el-divider></el-divider>
    <div v-if="responseImage.length === 0" style="display: flex; align-items: center; justify-content: center;">
      <el-empty description="No result" />
      <img style="width: 10%; height: 10%; margin-left: 10px;" src="../assets/avatar.jpeg" alt="" />
    </div>
    <div v-else>
      <el-row>
        <el-col :span="24">
          <!--tag list-->
          <div class="label-list">
            <el-row>
              <el-col v-for="(item, index) in tags" :key="index" :span="2">
                <el-tag :type="labelColor[index % labelColor.length]" :hit="true" style="margin-top: 10px">
                  <el-checkbox v-model="item.status" @change="tagChange" />
                  {{ item.label }}({{ item.size }})
                </el-tag>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>

      <el-divider></el-divider>
      <el-row style="width: 100%">
        <el-col :span="24">
          <div style="width: 90%; margin: 0 auto">
            <el-row>
              <el-col v-for="(item, index) in responseImage.slice(0, num)" :key="index" :span="6">
                <ImageCard :disallowedTags="disallowedTags" :hideTags="true" :imageId="item" />
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script>
import ImageCard from "@/components/ImageCard.vue";

export default {
  // eslint-disable-next-line
  name: "Search",
  components: {
    ImageCard,
  },
  data() {
    return {
      dialogImageUrl: "",
      dialogVisible: false,
      disabled: false,
      uploadUrl: process.env.VUE_APP_BASE_API + "/upload_img",
      fileList: [],
      labelColor: ["", "success", "info", "warning", "danger"],
      responseImage: [],
      filterImage: [],
      tags: [],
      disallowedTags: [],
      collectImage: [],
      currentPage: 1,
      isSearching: false,
      isCollectionLoading: false,

      num: 9,
    };
  },
  created() {
    this.$axios({
      method: "get",
      url: "/tags",
    }).then((response) => {
      this.tags = response.data.map((item) => {
        item.status = true;
        return item;
      });
      this.disallowedTags = [];
    });
  },
  methods: {
    handleRemove() {
      this.fileList.splice(0, 1);
    },
    uploadSuccess(response) {
      console.log("上传成功！");
      this.responseImage = response;
      this.isSearching = false;
    },
    handleChange(file) {
      if (this.fileList.length === 1) {
        return;
      }
      this.fileList = [];
      this.fileList.push(file);
    },
    searchRes() {
      this.isSearching = true;
      this.$refs.uploadRef.submit();
    },
    tagChange() {
      let disallowedTags = [];
      this.tags.forEach((item) => {
        if (!item.status) {
          disallowedTags.push(item.label);
        }
      });
      this.disallowedTags = disallowedTags;
    },
    handleCurrentChange(val) {
      this.currentPage = val;
    },
    getCollection() {
      this.isCollectionLoading = true;
      this.$axios({
        method: "get",
        url: "/collect/all",
      })
        .then((response) => {
          this.collectImage = response.data;
        })
        .finally(() => {
          this.isCollectionLoading = false;
        });
    },
  },
};
</script>
<style scoped>

.search-upload,
.select-show-num {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.input-row {
  display: flex;
  margin-top: 15px;
  justify-content: center;
  align-items: center;
}

.input-row > * + * {
  margin-left: 10px;
}

.input-row span {
  font-size: medium;
  font-weight: revert;
}

.el-button {
  margin-top: 20px;
  margin-bottom: 20px;
}
/* .el-input-number__decrease:before, 
.el-input-number__increase:before, 
.el-input-number__decrease:after, 
.el-input-number__increase:after {
  padding-top: 10px;
} */
</style>
