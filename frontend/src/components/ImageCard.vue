<template>
  <div>
    <div v-if="isTagDisallowed" class="CardContainer">
      <div
        class="CardType"
      >
        <!---->
        <el-image
          fit="fill"
          style="
            width: 100%;
            height: 62%;
            border-radius: 10px 10px 0 0;
            box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
              rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
          "
          :src= "url + imageId"
        >
        </el-image>
        <el-row style="margin-top: 10px">
          <el-col :span="3">
            <!--收藏图片-->
            <el-tooltip
              class="item"
              effect="dark"
              :content="
                isCollectedLoading
                  ? '加载中...'
                  : isCollected
                  ? '取消收藏'
                  : '收藏'
              "
              placement="top-start"
            >
              <div v-if="!isCollectedLoading">
                <em
                  :class="isCollected ? 'el-icon-star-on' : 'el-icon-star-off'"
                  style="font-size: 20px"
                  @click="collectImage"
                ></em>
              </div>
              <div v-else>
                <em class="el-icon-loading" style="font-size: 20px"></em>
              </div>
            </el-tooltip>
          </el-col>
          <el-col :span="3">
            <!--查看大图-->
            <el-tooltip
              class="item"
              effect="dark"
              content="查看大图"
              placement="top-start"
            >
              <em
                class="el-icon-zoom-in"
                style="font-size: 20px"
                @click="viewImageDetail"
              ></em>
            </el-tooltip>
          </el-col>
          <el-col :span="18">
            <span> No. {{ imageId }} </span>
          </el-col>
        </el-row>

        <div class="label-list">
          <el-tag
            type="primary"
            v-for="(i, index) in showTags"
            :key="index"
            effect="dark"
            :color="labelColor[index]"
            :hit="true"
          >
            {{ i }}
          </el-tag>
        </div>

        <el-dialog :visible.sync="dialogVisible" modal width="40%">
          <img
            :src="url + imageId"
            alt=""
            style="width: 100%; height: 100%; object-fit: contain;"
          />
        </el-dialog>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ImageCard",

  data() {
    return {
      url:  process.env.VUE_APP_BASE_API + "/image?id=",
      colors: ["#a3c6ea", "#70a8c4", "#559bcb"],
      labelColor: ["#77C9D4", "#57BC90", "#015249"],
      imageSource: "",
      isMouseOn: false,
      tags: [],
      isCollected: false,
      dialogVisible: false,
      isCollectedLoading: false,
    };
  },

  computed: {
    showTags() {
      if (this.tags.length !== 0) {
        return this.tags.slice(0, 3);
      } else {
        return ["none"];
      }
    },
    isTagDisallowed() {
      if (!this.hideTags) {
        return true;
      }
      for (let i = 0; i < this.tags.length; ++i) {
        if (this.disallowedTags.indexOf(this.tags[i]) !== -1) {
          return false;
        }
      }
      return true;
    },
  },

  props: {
    imageId: String,
    disallowedTags: Array,
    hideTags: Boolean,
  },

  created() {
    // 获取图片详细信息
    this.$axios({
      method: "get",
      url: "/info",
      params: {
        id: this.imageId,
      },
    })
      .then((response) => {
        this.isCollected = response.data.isCollected;
        this.tags = response.data.tags;
      })
      .catch(() => {});
  },

  methods: {
    collectImage() {
      this.isCollectedLoading = true;
      this.$axios({
        method: "post",
        url: "/collect",
        data: {
          id: this.imageId,
        },
      })
        .then(() => {
          this.isCollected = !this.isCollected;
          if (this.isCollected) {
            this.$message({
              message: "收藏成功！",
              type: "success",
            });
          } else {
            this.$message({
              message: "已取消收藏",
              type: "success",
            })
          }
          this.isCollectedLoading = false;
        })
        .catch(() => {
          this.isCollectedLoading = false;
        })
        .finally(() => {
          this.$emit("changeCollect");
        });
    },
    viewImageDetail() {
      this.dialogVisible = true;
    },
  },
};
</script>

<style>
.CardType {
  width: 95%;
  height: 95%;
  margin: 5px auto 0;
  border-radius: 10px !important;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 20px 25px -5px,
    rgba(0, 0, 0, 0.04) 0px 10px 10px -5px !important;
  background-color: rgba(229, 225, 225, 0.34);
  cursor: pointer;
  -webkit-transition: all 200ms ease-in;
}
</style>

<style scoped>
.el-divider--vertical {
  height: 4em !important;
  width: 2px !important;
}

.icon-love {
  position: absolute;
  left: 40%;
  bottom: 40%;
}

/* 标签列表 */
.label-list {
  padding: 1px 1px;
  margin: 1px 1px;
}
.el-tag {
  float: left;
  white-space: pre-line;
  word-break: break-all;
  margin-top: 5px;
  margin-left: 5px;
  max-height: 4vh;
  color: white;
}

.CardContainer {
  width: 270px;
  height: 290px;
  margin-bottom: 20px;
  margin-left: 25px;
}
</style>
