import Vue from 'vue'
import App from './App.vue'
import Vuelidate from 'vuelidate'
import router from './router'
import BootstrapVue from 'bootstrap-vue'
import VueSweetalert2 from 'vue-sweetalert2'
import Notifications from 'vue-notification'
import './registerServiceWorker'
import { abilitiesPlugin } from '@casl/vue';
import ability from './config/ability';
import VueTheMask from 'vue-the-mask';
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
//import money from 'v-money';
//import ViaCep from 'vue-viacep'


//Vue.use(ViaCep);
//Vue.use(money);
Vue.use(Toast);
Vue.use(VueTheMask);
Vue.use(abilitiesPlugin, ability);
Vue.use(BootstrapVue);
Vue.use(VueSweetalert2);
Vue.use(Vuelidate);
Vue.use(Notifications);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
