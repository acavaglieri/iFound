<template>
  <section class="login">
    <Toasts ref="Toasts"></Toasts>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <div class="container-scroller">
      <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="content-wrapper d-flex align-items-center auth">
          <div class="row w-100 flex-grow">
            <div class="col-lg-6 mx-auto">
              <div class="rounded auth-form-light text-left p-5 border">
                <div class="brand-logo">
                  <img src="../../assets/images/Logo_Name.png" />
                </div>
                <h4>Olá!</h4>
                <h6 class="font-weight-light">Faça login para entrar.</h6>
                <form class="pt-3">
                  <div class="form-group">
                    <input
                      type="email"
                      v-model="input.email"
                      class="form-control form-control-lg"
                      id="inputEmail"
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
                    <div
                      v-if="submitted && $v.input.email.$error"
                      class="invalid-feedback"
                    >
                      <span v-if="!$v.input.email.email"
                        >Insira um email válido.</span
                      >
                    </div>
                  </div>
                  <div class="my-2 d-flex">
                    <router-link to="forgot/password" class="auth-link text-black">Esqueceu a senha?</router-link>
                  </div>
                  <div class="form-group">
                    <b-input-group>
                      <input
                        :type="seePassword ? 'text' : 'password'"
                        v-model="input.password"
                        class="form-control form-control-lg"
                        id="inputPassword"
                        placeholder="Senha"                      
                        :class="{
                          'is-invalid': submitted && $v.input.password.$error,
                        }"
                      />
                      <b-button
                        @click="seePassword = !seePassword"
                        :class="seePasswordIcon"
                        style="background-color: #65C89B; color: #fff;"
                        aria-hidden="true"
                        variant="light"
                        size="sm"
                        squared
                      ></b-button>
                      <div
                        v-if="submitted && $v.input.password.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.input.password.required"
                          >Insira sua senha.</span
                        >
                      </div>
                    </b-input-group>
                  </div>
                  <div class="mt-3">
                    <button
                      class="
                        btn btn-block btn-primary btn-lg
                        font-weight-medium
                        auth-form-btn
                      "
                      :disabled="isLoading"
                      @click.prevent="login(input.email, input.password)"
                    >
                      <div class="text-center align-items-center">
                        <span v-if="!isLoading">ENTRAR</span>
                        <b-spinner v-else small></b-spinner>
                      </div>
                    </button>
                  </div>
                  <div class="mt-3 text-center pt-3 font-weight-light">
                    Não tem uma conta? <router-link :to="{ name: 'register' }" class="text-primary">Cadastre-se</router-link>
                  </div>
                  <br>
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
import { required, email } from "vuelidate/lib/validators";
import PlgUsersApi from '../../apis/PlgUsersApi.vue';
import { getAbilities } from "../../config/ability";
import Toasts from '../../components/Toasts.vue';

export default {
  name: 'Login',
  data() {
    return {
      input: {
        email: "",
        password: "",
      },
      seePassword: false,
      isLoading: false,
      submitted: false,
      items: [],
      msg: {
        status: false,
        msg: '',
      }

    }
  },
  validations: {
    input: {
      email: {
        required,
        email,
      },
      password: {
        required,
      }
    }
  },
  computed: {
    seePasswordIcon() {
      return this.seePassword ? "mdi mdi-eye-off mdi-18px" : "mdi mdi-eye mdi-18px"
    }
  },
  components: { 
    Toasts,
    PlgUsersApi
  },
  async mounted(){
    var authenticated = localStorage.getItem('authenticated');
    if (authenticated=="true"){
      this.$router.replace({ name: "home" }).catch(err => err);
    }else{
      this.$router.replace({ name: "login" }).catch(err => err);
    }
  },
  methods: {
    async login() {
      this.submitted = true;
      this.$v.$touch();
      if (!this.$v.$invalid) {
        const payload = {
            email: this.input.email,
            password: this.input.password,
        }
        if(this.input.email != "" && this.input.password != "") {
          this.isLoading = true;
          let response = await this.$refs.PlgUsersApi.getLoginApi(payload);
          if(response.data.status != "success"){
            this.isLoading = false;
            this.$emit("authenticated", false);
            this.$refs.Toasts.showToast("error", response.data.message);
            this.deleteLocalStorage();
          } else {
            this.isLoading = false;
            this.$emit("authenticated", true);
            localStorage.setItem("access_token", response.data.access_token)
            this.setLocalStorage(true, response.data.user.email, response.data.user.role, response.data.user.workspace, response.data.user.name);
            this.$ability.update(getAbilities());
            this.$router.replace({name: 'home'});
          }
        }
      }
    },
    setLocalStorage(authenticated, email, role, workspace, name){
      localStorage.setItem('authenticated', authenticated);
      localStorage.setItem('email', email);
      localStorage.setItem('role', role);
      localStorage.setItem('workspace', workspace);
      localStorage.setItem('name', name);
    },
    deleteLocalStorage(){
      localStorage.removeItem('authenticated');
      localStorage.removeItem('email');
      localStorage.removeItem('name');
    },
  }
}
</script>
