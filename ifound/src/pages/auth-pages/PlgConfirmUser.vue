<template>
  <section class="">
    <div class="container-scroller">
      <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="content-wrapper d-flex align-items-center auth">
          <div class="row w-100 flex-grow">
            <div class="col-xl-4 col-lg-6 mx-auto">
              <div class="auth-form-light text-left p-5">
                <div class="brand-logo">
                  <img src="../../assets/images/logo.png" />
                </div>
                <h4>Confirmação de Conta</h4>
                <h6 v-show="!isLoading" class="font-weight-light">
                  Conta confirmada! Faça <router-link :to="{name: 'login'}">login</router-link> para prosseguir.
                </h6>
                <h6 v-show="isLoading">
                  <b-spinner></b-spinner>
                </h6>
              </div>
            </div>
          </div>
        </div>
        <!-- content-wrapper ends -->
      </div>
      <!-- page-body-wrapper ends -->
    </div>
  </section>
</template>

<script>
import usersApi from '../../apis/PlgUsersApi.vue';


export default {
  name: "ConfirmUser",
  data() {
    return {
      isLoading: false,
    }
  },
  mixins: [usersApi],
  async mounted() {
    if(this.$route.query.token) {
      this.isLoading = true;
      const payload = {
        token: this.$route.query.token,
      }
      await this.confirmUser(payload);
      this.isLoading = false;
    }
  },
};
</script>
