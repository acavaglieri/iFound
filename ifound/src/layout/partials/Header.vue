<template>
  <b-navbar
    id="template-header"
    class="default-layout-navbar col-lg-12 col-12 p-0 fixed-top d-flex flex-row"
    toggleable="lg"
  >
    <div class="text-center navbar-brand-wrapper d-flex align-items-center justify-content-center">
      <router-link class="navbar-brand brand-logo py-2 h-100 w-100" :to="{name: 'home'}">
        <img src="@/assets/images/Logo_Name.png" alt="logo" class="h-100 w-auto" />
      </router-link>
      <router-link class="navbar-brand brand-logo-mini py-2 h-100 w-100" :to="{name: 'home'}">
        <img src="@/assets/images/logo.png" alt="logo" class="h-100 w-auto" />
      </router-link>
    </div>
    <div class="navbar-menu-wrapper d-flex align-items-center ml-auto ml-lg-0">
      <button
        class="navbar-toggler navbar-toggler align-self-center d-lg-block"
        type="button"
        @click="toggleSidebar()"
      >
        <span class="ti-layout-grid2"></span>
      </button>

      <span v-if="!isMobile">
        <!-- alterar para outra coisa que cliente requerer futuramente -->
        <!-- <span class="ml-3">Concluído (dia)<span><b-badge pill variant="outline-success" class="ml-2">{{items[0].orders_today_done.quantity}} <b-badge pill variant="success" class="ml-1">{{items[0].orders_today_done.quantity_scheduled}}</b-badge></b-badge></span></span>
        <span class="ml-3">Ocorrência (dia)<span><b-badge pill variant="outline-danger" class="ml-2">{{items[0].orders_today_final_occurrence.quantity}} <b-badge pill variant="danger" class="ml-1">{{items[0].orders_today_final_occurrence.quantity_scheduled}}</b-badge></b-badge></span></span>
        <span class="ml-3">Produtividade (%)<span><b-badge pill variant="outline-info" class="ml-2">{{items[0].orders_productivity.quantity}}% <b-badge pill variant="info" class="ml-1">{{items[0].orders_productivity.quantity_scheduled}}%</b-badge></b-badge></span></span> -->
      </span>
      <button
        class="navbar-toggler navbar-toggler-right"
        type="button"
        @click="toggleMobileSidebar()"
      >
        <span class="mdi mdi-menu"></span>
      </button>
      <b-navbar-nav class="navbar-nav-right ml-auto">
      <b-nav-item-dropdown right class="nav-profile">
        <template slot="button-content">
          <span
            class="nav-link dropdown-toggle"
            id="profileDropdown"
            href="javascript:void(0);"
            data-toggle="dropdown"
            aria-expanded="false"
          >
            <div>
              <img src="../../assets/images/faces/user-placeholder.png" height="30px" />
            </div>
          </span>
        </template>
        <b-dropdown-item class="preview-item" @click="goToProfile()">
        <div>
          <i class="fa fa-user"></i> 
          <span>Perfil</span>
        </div>
        </b-dropdown-item>
        <b-dropdown-item class="preview-item" @click="logout()">
          <div>
            <i class="fa fa-power-off menu-icon"></i>
            <span class="menu-title">Sair</span>
          </div>
        </b-dropdown-item>
      </b-nav-item-dropdown>
      </b-navbar-nav>
    </div>
  </b-navbar>
</template>

<script>

const items=
[
  {
    orders_today_done: {
      quantity: 4,
      quantity_scheduled: 2,
    },
    orders_today_final_occurrence: {
      quantity: 2,
      quantity_scheduled: 0,
    },
    orders_productivity: {
      quantity: 67,
      quantity_scheduled: 100,
    },
  }
]

export default {

  name: "app-header",

  data() {
    return {
      windowWidth: '',
      item: [],
      timer: '',
    }
  },

  created() {
    
  },

  mounted() {
    //trazer via axios
    this.items = items;

    this.changeItems();
    this.timer = setInterval(this.changeItems, 30000);

    this.windowWidth = window.innerWidth;
    window.addEventListener('resize', () => {
      this.windowWidth = window.innerWidth
    });

  },

  computed: {
    isMobile() {
      return this.windowWidth <= 820
    }
  },

  methods: {
    logout() {
      localStorage.setItem('authenticated', false);
      localStorage.removeItem('email');
      localStorage.removeItem('name');
      localStorage.removeItem('role');
      localStorage.removeItem('workspace'); 
      localStorage.removeItem('cellphone'); 

      this.$router.replace({ name: "login" }).catch(err => err);
    },
    goToProfile(){
      this.$router.push("/site/profile")
    },
    changeItems(){
      //trocar essas linhas por get em api
      this.items[0].orders_today_done.quantity+=1;
      this.items[0].orders_today_done.quantity_scheduled+=1;
      this.items[0].orders_today_final_occurrence.quantity+=1;
      this.items[0].orders_today_final_occurrence.quantity_scheduled+=1;

      const limite = 10;

      this.items[0].orders_today_done.quantity > (limite * 4) ? this.items[0].orders_today_done.quantity = 0 : this.items[0].orders_today_done.quantity;
      this.items[0].orders_today_done.quantity_scheduled > (limite * 3) ? this.items[0].orders_today_done.quantity_scheduled = 0 : this.items[0].orders_today_done.quantity_scheduled;
      this.items[0].orders_today_final_occurrence.quantity > (limite * 2) ? this.items[0].orders_today_final_occurrence.quantity = 0 : this.items[0].orders_today_final_occurrence.quantity;
      this.items[0].orders_today_final_occurrence.quantity_scheduled > limite ? this.items[0].orders_today_final_occurrence.quantity_scheduled = 0 : this.items[0].orders_today_final_occurrence.quantity_scheduled;

      var orders_productivity = this.productivity(
        this.items[0].orders_today_done.quantity,
        this.items[0].orders_today_done.quantity_scheduled,
        this.items[0].orders_today_final_occurrence.quantity,
        this.items[0].orders_today_final_occurrence.quantity_scheduled
      );

      this.items[0].orders_productivity.quantity=orders_productivity[0];
      this.items[0].orders_productivity.quantity_scheduled=orders_productivity[1];
      //até aqui

      this.$forceUpdate();
    },

    //esse método não será necessário quando valores de header vierem via axios
    productivity(orders_today_done_quantity, orders_today_done_quantity_scheduled, orders_today_final_occurrence_quantity, orders_today_final_occurrence_quantity_scheduled){
      var productivity = orders_today_done_quantity / (orders_today_done_quantity + orders_today_final_occurrence_quantity);
      var productivity_scheduled = orders_today_done_quantity_scheduled / (orders_today_done_quantity_scheduled + orders_today_final_occurrence_quantity_scheduled);

      isNaN(productivity) ? productivity=0 : productivity = Math.ceil(parseFloat(productivity).toFixed(2)*100);
      isNaN(productivity_scheduled) ? productivity_scheduled=0 : productivity_scheduled = Math.ceil(parseFloat(productivity_scheduled).toFixed(2)*100);

      return [productivity,productivity_scheduled]
    },

    cancelAutoUpdate() {
      clearInterval(this.timer)
    },

    toggleSidebar: () => {
      document.querySelector("body").classList.toggle("sidebar-icon-only");
    },
    toggleMobileSidebar: () => {
      document.querySelector("#sidebar").classList.toggle("active");
    },
    togglesettingsPannel: () => {
      document.querySelector("#right-sidebar").classList.toggle("open");
    },
    clearSession() {
      this.$router.replace({ name: "login" });
      localStorage.removeItem('authenticated');
      localStorage.removeItem('email');
      localStorage.removeItem('name');
      localStorage.removeItem('role');
      localStorage.removeItem('cellphone');
    },
  },

  destroyed(){
    this.cancelAutoUpdate;
  },

  beforeDestroy(){
    clearInterval(this.timer);
  }
};
</script>

<style scoped>
</style>