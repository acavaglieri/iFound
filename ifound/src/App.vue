<template>
  <div id="app">
    <notifications position="top center" width="60%"/>
      <transition name="slide-up" mode="out-in">
        <router-view @authenticated="setAuthenticated" v-slot="{ Component }">
              <component :is="Component" />
        </router-view>
      </transition>
  </div>
</template>

<script>

import './components/ui/autoComplete.css';

export default {
  name: 'app',
  data() {
    return {
      authenticated: false,
    }
  },
  components: {
  },
  created() {

    if(localStorage.getItem('authenticated')==null || localStorage.getItem('authenticated')==false){
      localStorage.setItem('authenticated',false);
    }
    const status = localStorage.getItem('authenticated');
    this.setAuthenticated(status);
  },
  mounted() {
    /* TODO: Criar navigation guard
    if(!this.authenticated) {
      this.$router.replace({ name: "login" });
    }*/
    const status = localStorage.getItem('authenticated');
    this.setAuthenticated(status);
  },
  methods: {
    setAuthenticated(status) {
      if(status=='true'){
        status=true
      }
      if(status=='false' || status==''){
        status=false
      }
      this.authenticated = status;
      localStorage.setItem('authenticated',status);
    },
    
  },
}
</script>

<style lang="scss">
@import "../node_modules/@mdi/font/css/materialdesignicons.min.css";
@import "../node_modules/flag-icon-css/css/flag-icon.min.css";
@import "../node_modules/font-awesome/css/font-awesome.min.css";
@import "../node_modules/simple-line-icons/css/simple-line-icons.css";
@import "../node_modules/ti-icons/css/themify-icons.css";
@import "../node_modules/sweetalert2/dist/sweetalert2.min.css";
@import "../node_modules/vue-snotify/styles/material.css";
@import "../node_modules/codemirror/lib/codemirror.css";
@import "../node_modules/fullcalendar/dist/fullcalendar.css";
@import "../node_modules/c3/c3.min.css";
@import "../node_modules/chartist/dist/chartist.min.css";
@import "./assets/scss/style";

// Transitions

// Slide Up
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s ease-out;
}
.slide-up-enter,
.slide-up-leave-to {
  transform: translateY(10px);
  opacity: 0;
}

// Slide Left
.slide-left-enter-active,
.slide-left-leave-active {
  transition: all 0.3s ease-out;
}
.slide-left-enter,
.slide-left-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>
