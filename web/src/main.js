import Vue from 'vue'
import App from './App.vue'
import DataTable from 'laravel-vue-datatable';

Vue.use(DataTable);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
