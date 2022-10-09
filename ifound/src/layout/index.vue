<template>
  <section class="main-view">
    <div class="container-scroller">
      <Header />
      <div :class="{ 'container-fluid': true, 'page-body-wrapper': true }">
        <Sidebar />
        <div class="main-panel">
          <div
            :class="{
              'content-wrapper': true,
              'align-items-end': !checkRoute,
            }"
          >
            <!-- <router-view></router-view> -->
            <router-view :key="$route.fullPath"></router-view>
          </div>
          <!-- content wrapper ends -->
          <Footer />
        </div>
        <!-- main panel ends -->
      </div>
      <!-- page-body-wrapper ends -->
    </div>
  </section>
</template>

<script>
import Header from "./partials/Header";
import Sidebar from "./partials/Sidebar";
import Footer from "./partials/Footer";
export default {
  name: "layout",

  components: {
    Header,
    Sidebar,
    Footer,
  },

  computed: {
    checkRoute() {
      let routesBlackList = ["pix_qrcode_scan"];
      if (routesBlackList.includes(this.$route.name)) {
        return false;
      } else {
        return true;
      }
    },
    checkMobile() {
      let screenWidth = screen.availWidth;
      if (screenWidth > 440) {
        return false;
      }
      return true;
    },
  },
};
</script>
