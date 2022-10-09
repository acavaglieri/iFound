<template>
  <section class="">
    <Toasts ref="Toasts"></Toasts>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <div class="container-scroller">
      <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="content-wrapper d-flex align-items-center auth">
          <div class="row w-100 flex-grow">
            <div class="col-lg-6 mx-auto">
              <div class="border rounded auth-form-light text-left p-5">
                <div class="brand-logo">
                  <img src="../../assets/images/logo.png" />
                </div>
                <h4>Redefinir Senha</h4>
                <h6 class="font-weight-light">
                  Insira seu e-mail abaixo para redefinir sua senha.
                </h6>
                <form class="pt-3">
                  <div class="form-group">
                    <input
                      type="email"
                      v-model="input.email"
                      class="form-control form-control-lg"
                      id="exampleInputEmail1"
                      placeholder="Email"                      
                      :class="{
                        'is-invalid': submitted && $v.input.email.$error,
                      }"
                    />
                    <div
                      v-if="submitted && $v.input.email.$error"
                      class="invalid-feedback"
                    >
                      <span v-if="!$v.input.email.required"
                        >Insira seu email.</span
                      >
                    </div>
                  </div>
                  <div class="mt-3">
                    <button
                      v-show="!isLoading"
                      class="
                        btn btn-block btn-primary btn-lg
                        font-weight-medium
                        auth-form-btn
                      "
                      @click.prevent="sendResetEmail"
                    >
                      ENVIAR
                    </button>
                    <button
                      v-show="isLoading"
                      disabled
                      class="
                        btn btn-block btn-primary btn-lg
                        font-weight-medium
                        auth-form-btn
                      "
                      @click.prevent="sendResetEmail"
                    >
                      <div class="text-center align-items-center">
                        <b-spinner small></b-spinner>
                      </div>
                    </button>
                  </div>
                  <!-- <br>
                  <span>{{items}}</span> -->
                </form>
                <div>
                  <h6 class="mt-3 text-center font-weight-light">Lembrou? <router-link :to="{name: 'login'}">Logar</router-link></h6>
                </div>
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
import { required, } from "vuelidate/lib/validators";
import PlgUsersApi from '../../apis/PlgUsersApi.vue';
import Toasts from '../../components/Toasts.vue';


export default {
  name: "ForgotPassword",
  data() {
    return {
      input: {
        email: "",
      },
      isLoading: false,
      submitted: false,
      items: [],
      msg: {
        status: false,
        msg: "",
      },
    };
  },
 validations: {
    input: {
      email: {
        required,
      },
    }
  },
  components: {
    Toasts,
    PlgUsersApi
  },
  async mounted() {
    var authenticated = localStorage.getItem("authenticated");

    if(this.$route.query.token){
      let token = this.$route.query.token;
      this.$router.push({path: "/forgot/password/sent", query: {token}});
    }
    if (authenticated == "true") {
      this.$router.push("/site/home");
    }
  },
  methods: {
    async sendResetEmail() {
      this.submitted = true;
      this.$v.$touch();
      if (!this.$v.$invalid) {
        const UserTokenPayload = {
          email: this.input.email,
        };
        this.isLoading = true;
        let response = await this.$refs.PlgUsersApi.getTokenApi(UserTokenPayload);
        this.isLoading = false;
        this.$refs.Toasts.showToast(response.data.status, response.data.message);
      } 
    }
  },
};
</script>
