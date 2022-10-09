<template>
  <section class="">
    <Toasts ref="Toasts"></Toasts>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <div class="container-scroller">
      <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="content-wrapper d-flex align-items-center auth">
          <div class="row w-100 flex-grow">
            <div class="col-xl-4 col-lg-6 mx-auto">
              <div class="auth-form-light text-left p-5">
                <div class="brand-logo">
                  <img src="../../assets/images/Logo_Name.png" />
                </div>
                <h4>Olá!</h4>
                <h6 class="font-weight-light">
                  Preencha os campos abaixo para redefinir sua senha.
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
                  <div class="form-group">
                    <b-input-group>
                      <input
                        type="password"
                        v-model="input.password"
                        class="form-control form-control-lg"
                        id="inputPassword"
                        placeholder="Senha"                      
                        :class="{
                          'is-invalid': submitted && $v.input.password.$error,
                        }"
                      />
                      <b-button
                        @click="passwordFieldCheck ='password', seePassword()"
                        :class="eyeIconPass"
                        style="color: #fff;"
                        aria-hidden="true"
                        variant="primary"
                        size="sm"
                        squared
                      ></b-button>
                      <div
                        v-if="submitted && $v.input.password.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.input.password.required"
                          >Insira sua nova senha.</span
                        >
                      </div>
                    </b-input-group>
                  </div>
                  <div class="form-group">
                    <b-input-group>
                      <input
                        type="password"
                        v-model="input.rePassword"
                        class="form-control form-control-lg"
                        id="inputRePassword"
                        placeholder="Confirme sua senha"                      
                        :class="{
                          'is-invalid': submitted && $v.input.rePassword.$error,
                        }"
                      />
                      <b-button
                        @click="passwordFieldCheck ='rePassword', seePassword()"
                        :class="eyeIconRePass"
                        style="color: #fff;"
                        aria-hidden="true"
                        variant="primary"
                        size="sm"
                        squared
                      ></b-button>
                      <div
                        v-if="submitted && $v.input.rePassword.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.input.rePassword.required"
                          >Confirme sua nova senha.</span
                        >
                      </div>
                      <div
                        v-if="submitted && $v.input.rePassword.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.input.rePassword.sameAsPassword && $v.input.rePassword.required"
                          >Senhas não conferem!</span
                        >
                      </div>
                    </b-input-group>
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
                      Enviar
                    </button>
                    <button
                      v-show="isLoading"
                      class="
                        btn btn-block btn-primary btn-lg
                        font-weight-medium
                        auth-form-btn disabled
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
import { required, sameAs, } from "vuelidate/lib/validators";
import PlgUsersApi from "../../apis/PlgUsersApi.vue";
import Toasts from "../../components/Toasts.vue";


export default {
  name: "ForgotPasswordSent",
  data() {
    return {
      input: {
        email: "",
        password: "",
        rePassword: "",
      },
      passwordFieldCheck: null,
      eyeIconPass: "mdi mdi-eye mdi-18px",
      eyeIconRePass: "mdi mdi-eye mdi-18px",
      isLoading: false,
      token: null,
      submitted: null,
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
      password: {
        required,
      },
      rePassword: {
        required, sameAsPassword: sameAs('password')
      },
    }
  },  
  components: {
    Toasts,
    PlgUsersApi
  },
  async mounted() {
    var authenticated = localStorage.getItem("authenticated");
    if (this.$route.query.token) {
      this.token = this.$route.query.token;
    }
    if (authenticated == "true") {
      this.$router.push("/site/home");
    }
  },
  methods: {
    seePassword() {
      if(this.passwordFieldCheck == "password") {
        let passValidation = document.getElementById("inputPassword");
        if (passValidation.type == "password") {
          passValidation.type = "text";
          this.eyeIconPass = "mdi mdi-eye-off mdi-18px";
        } else if (passValidation.type == "text") {
          passValidation.type = "password";
          this.eyeIconPass = "mdi mdi-eye mdi-18px";
        }
      }
      if(this.passwordFieldCheck == "rePassword") {
        let passValidation = document.getElementById("inputRePassword");
        if (passValidation.type == "password") {
          passValidation.type = "text";
          this.eyeIconRePass = "mdi mdi-eye-off mdi-18px";
        } else if (passValidation.type == "text") {
          passValidation.type = "password";
          this.eyeIconRePass = "mdi mdi-eye mdi-18px";
        }
      }
    },
    async sendResetEmail() {
      this.submitted = true;
      this.$v.$touch();
      if (!this.$v.$invalid) {
      const userResetPassPayload = {
        user: {
          email: this.input.email,
          new_password: this.input.password,
        },
        token: {
          token: this.token,
        },
      };
      this.isLoading = true;
      let response = await this.$refs.PlgUsersApi.resetPasswordApi(
        userResetPassPayload
      );
      this.isLoading = false;
      if(response.data.status === "success"){
        this.$router.replace({name:'login'});
      }
      this.$refs.Toasts.showToast(response.data.status, response.data.message);
      }
    }  
  },
};
</script>
