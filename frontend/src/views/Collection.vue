<template>
  <div>
    <el-table
      :data="tableData"
      style="width: 50%; margin-left: 25%; "
    >
      <el-table-column prop="epoch" label="Epoch"></el-table-column>
      <el-table-column prop="trainLoss" label="Train Loss"></el-table-column>
      <el-table-column prop="valLoss" label="Validation Loss"></el-table-column>
      <el-table-column prop="trainAcc" label="Train Accuracy"></el-table-column>
      <el-table-column prop="valAcc" label="Validation Accuracy"></el-table-column>
    </el-table>
    <img style="width: 50%; height: 10%; margin-left: 25%;" src="../assets/modelImage/fan_image.png" alt="" />
    <img style="width: 50%; height: 10%; margin-left: 25%;" src="../assets/modelImage/zhu_image.png" alt="" />
    <img style="width: 50%; height: 10%; margin-left: 25%;" src="../assets/modelImage/trainloss and valloss.png" alt="" />
    <img style="width: 50%; height: 10%; margin-left: 25%; margin-bottom: 20%;" src="../assets/modelImage/trainacc and valacc.png" alt="" />
  </div>
</template>

<script>
export default {
  name: "Collection",
  data() {
    return {
      tableData: [
      { epoch: 1, trainLoss: 0.3057, valLoss: 0.1498, trainAcc: 0.9192, valAcc: 0.9658 },
      { epoch: 2, trainLoss: 0.1202, valLoss: 0.1222, trainAcc: 0.9719, valAcc: 0.9743 },
      { epoch: 3, trainLoss: 0.0880, valLoss: 0.1104, trainAcc: 0.9797, valAcc: 0.9767 },
      { epoch: 4, trainLoss: 0.0698, valLoss: 0.1006, trainAcc: 0.9851, valAcc: 0.9787 },
      { epoch: 5, trainLoss: 0.0614, valLoss: 0.1016, trainAcc: 0.9870, valAcc: 0.9753 },
      { epoch: 6, trainLoss: 0.0506, valLoss: 0.1024, trainAcc: 0.9899, valAcc: 0.9820 },
      { epoch: 7, trainLoss: 0.0471, valLoss: 0.0798, trainAcc: 0.9907, valAcc: 0.9838 },
      { epoch: 8, trainLoss: 0.0399, valLoss: 0.0883, trainAcc: 0.9928, valAcc: 0.9808 },
      { epoch: 9, trainLoss: 0.0360, valLoss: 0.1009, trainAcc: 0.9941, valAcc: 0.9805 },
      { epoch: 10, trainLoss: 0.0351, valLoss: 0.1209, trainAcc: 0.9940, valAcc: 0.9793 },
      { epoch: 11, trainLoss: 0.0331, valLoss: 0.0925, trainAcc: 0.9942, valAcc: 0.9813 },
      { epoch: 12, trainLoss: 0.0292, valLoss: 0.0980, trainAcc: 0.9954, valAcc: 0.9813 },
      { epoch: 13, trainLoss: 0.0303, valLoss: 0.1010, trainAcc: 0.9950, valAcc: 0.9795 },
      { epoch: 14, trainLoss: 0.0266, valLoss: 0.0925, trainAcc: 0.9959, valAcc: 0.9812 },
      { epoch: 15, trainLoss: 0.0264, valLoss: 0.0876, trainAcc: 0.9959, valAcc: 0.9832 },
      { epoch: 16, trainLoss: 0.0219, valLoss: 0.0942, trainAcc: 0.9971, valAcc: 0.9833 },
      { epoch: 17, trainLoss: 0.0234, valLoss: 0.0955, trainAcc: 0.9967, valAcc: 0.9847 },
      { epoch: 18, trainLoss: 0.0241, valLoss: 0.1113, trainAcc: 0.9964, valAcc: 0.9802 },
      { epoch: 19, trainLoss: 0.0245, valLoss: 0.1043, trainAcc: 0.9962, valAcc: 0.9798 },
      { epoch: 20, trainLoss: 0.0200, valLoss: 0.1012, trainAcc: 0.9976, valAcc: 0.9832 },
      { epoch: 21, trainLoss: 0.0211, valLoss: 0.1063, trainAcc: 0.9970, valAcc: 0.9838 },
      { epoch: 22, trainLoss: 0.0222, valLoss: 0.1011, trainAcc: 0.9967, valAcc: 0.9825 },
      { epoch: 23, trainLoss: 0.0187, valLoss: 0.1370, trainAcc: 0.9977, valAcc: 0.9787 },
      { epoch: 24, trainLoss: 0.0226, valLoss: 0.1125, trainAcc: 0.9964, valAcc: 0.9810 },
      { epoch: 25, trainLoss: 0.0202, valLoss: 0.1029, trainAcc: 0.9976, valAcc: 0.9828 },
      { epoch: 26, trainLoss: 0.0190, valLoss: 0.1080, trainAcc: 0.9975, valAcc: 0.9823 },
      { epoch: 27, trainLoss: 0.0176, valLoss: 0.1390, trainAcc: 0.9978, valAcc: 0.9770 },
      { epoch: 28, trainLoss: 0.0194, valLoss: 0.1313, trainAcc: 0.9974, valAcc: 0.9778 },
      { epoch: 29, trainLoss: 0.0204, valLoss: 0.1141, trainAcc: 0.9971, valAcc: 0.9827 },
      { epoch: 30, trainLoss: 0.0164, valLoss: 0.1401, trainAcc: 0.9979, valAcc: 0.9747 },
      { epoch: 31, trainLoss: 0.0195, valLoss: 0.1141, trainAcc: 0.9972, valAcc: 0.9823 },
      { epoch: 32, trainLoss: 0.0165, valLoss: 0.1092, trainAcc: 0.9982, valAcc: 0.9828 },
      { epoch: 33, trainLoss: 0.0169, valLoss: 0.1146, trainAcc: 0.9979, valAcc: 0.9797 },
      { epoch: 34, trainLoss: 0.0189, valLoss: 0.0965, trainAcc: 0.9974, valAcc: 0.9845 },
      { epoch: 36, trainLoss: 0.0186, valLoss: 0.0965, trainAcc: 0.9972, valAcc: 0.9852 },
      { epoch: 37, trainLoss: 0.0109, valLoss: 0.0901, trainAcc: 0.9996, valAcc: 0.9853 },
      { epoch: 38, trainLoss: 0.0208, valLoss: 0.1067, trainAcc: 0.9967, valAcc: 0.9830 },
      { epoch: 39, trainLoss: 0.0164, valLoss: 0.0959, trainAcc: 0.9982, valAcc: 0.9833 },
      { epoch: 40, trainLoss: 0.0130, valLoss: 0.1164, trainAcc: 0.9990, valAcc: 0.9817 },
      { epoch: 41, trainLoss: 0.0141, valLoss: 0.1119, trainAcc: 0.9984, valAcc: 0.9820 },
      { epoch: 42, trainLoss: 0.0182, valLoss: 0.1322, trainAcc: 0.9973, valAcc: 0.9808 },
      { epoch: 43, trainLoss: 0.0149, valLoss: 0.1053, trainAcc: 0.9985, valAcc: 0.9840 },
      { epoch: 44, trainLoss: 0.0110, valLoss: 0.1411, trainAcc: 0.9992, valAcc: 0.9793 },
      { epoch: 45, trainLoss: 0.0193, valLoss: 0.1205, trainAcc: 0.9969, valAcc: 0.9835 },
      { epoch: 46, trainLoss: 0.0125, valLoss: 0.1002, trainAcc: 0.9990, valAcc: 0.9833 },
      { epoch: 47, trainLoss: 0.0150, valLoss: 0.1245, trainAcc: 0.9981, valAcc: 0.9820 },
      { epoch: 48, trainLoss: 0.0164, valLoss: 0.1234, trainAcc: 0.9978, valAcc: 0.9830 },
      { epoch: 49, trainLoss: 0.0168, valLoss: 0.1104, trainAcc: 0.9979, valAcc: 0.9822 },
      { epoch: 50, trainLoss: 0.0101, valLoss: 0.1368, trainAcc: 0.9995, valAcc: 0.9823 }
        // Add more data here
      ]
    };
  },
};
</script>

<style scoped>

</style>
