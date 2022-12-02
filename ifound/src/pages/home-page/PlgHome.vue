<template>
  <section class="dashboard">
    <div class="grid-margin">
      <div class="px-5">
        <transition name="slide-up" appear>
          <b-row class="mb-2">
            <b-col md="9" cols="5" class="p-0">
              <h3 class="font-weight-bold">Olá {{ name }} </h3>
              <!--<h3 class="font-weight-bold">Olá {{ user.name }} </h3>-->
              <span class="text-left text-muted">
                <!--<div>
                  Olá {{ name }}
                </div>
                <div>
                  Olá {{ email }}
                </div>-->
              </span>
            </b-col>
            <b-col md="2" cols="4" class="text-right d-flex justify-content-end my-2">
              <PlgAccountBalance :showBalance="showPetInfoCheck" />
            </b-col>
            <b-col md="1" cols="3" class="text-right px-0 px-md-auto">
              <!--<div>
                <b-button
                  @click="seePetInfo()"
                  :class="eyeIcon"
                  class="mt-1 text-left"
                  variant="link"
                  size="sm"
                ></b-button>
              </div>-->
            </b-col>
          </b-row>
        </transition>
      </div>

      <div class="row px-4 mt-5 grid-margin text-center d-flex">
        <transition name="slide-left" appear mode="out-in">

          <b-button @click="goToFind" variant="light">
            <i class="mdi mdi-qrcode-scan mr-1"></i>
            Encontrei um animal!
          </b-button>

        </transition>
      </div>
    </div>

    <template>
      <div id="app" >
        <Pets/>
      </div>
    </template>

  </section>
</template>


<script>
//import PlgAccountBalance from "../../components/accounts/PlgAccountBalance.vue";
//import PlgBankStatement from "../../components/bank-statement/PlgBankStatement.vue";
import Pets from '../../components/Pets.vue'
//import { name } from "vuelidate/lib/validators";

export default {
  name: "dashboard",
  data() {
    return {
      loader: false,
      showPetInfoCheck: true,
      balance: 0,
      totalIns: null,
      totalOuts: null,
      insPercentage: null,
      outsPercentage: null,
      tableFields: [],
      data: null,
      //eyeIcon: "mdi mdi-eye-off mdi-36px",
      name: localStorage.getItem('name'),
      email: localStorage.getItem('email'),
    };
  },
  components: {

    Pets,
  },
  mounted() {
    this.environment = process.env.VUE_APP_ENVIRONMENT
    this.version = process.env.VUE_APP_VERSION
  },
};
</script>

<style scoped>
.item-card {
  border-radius: 30%;
}
.home-button {
  border-radius: 100px; 
  height: 8em; 
  width: 109.2px;
}
@media (max-width: 440px) {
  .item-card {
    width: 33%;
  }
}
#app {
  font-size: 16px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
