<template>
  <section class="">
    <div class="container-scroller">
      <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="content-wrapper d-flex align-items-center auth">
          <div class="row w-100 flex-grow">
            <div class="col-xl-6 col-lg-6 mx-auto">
              <div class="rounded auth-form-light border text-left p-5">
                <div class="brand-logo">
                  <img src="../../assets/images/logo.png" />
                </div>
                <h4>Bem-vindo(a) ao iFound!</h4>
                <p v-show="!isLoading" class="font-weight-light">
                  Enviamos um email para que você possa confirmar sua conta.
                </p>
                <p>
                  Certifique-se de checar sua caixa de entrada e spam.
                </p>
                <div class="d-flex justify-content-end pt-3 mb-0">
                  <router-link class="btn btn-primary" :to="{name: 'login'}">LOGIN</router-link>
                </div>
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
export default {
  name: "ConfirmationEmailSent",
};
</script>
