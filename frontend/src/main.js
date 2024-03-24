import Vue from 'vue';
import ElementUI from 'element-ui';
import "./theme/index.css";
import App from './App.vue';

import service from './utils/request';
Vue.prototype.$axios = service;

import router from './router'

Vue.use(ElementUI);

new Vue({
  el: '#app',
  router,
  render: h => h(App)
});