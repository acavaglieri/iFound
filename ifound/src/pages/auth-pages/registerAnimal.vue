<template>
    <section class="registerAnimal">
      <Toasts ref="Toasts"></Toasts>
      <PlgpetsApi ref="PlgpetsApi"></PlgpetsApi>
      <div class="container-scroller">
        <div class="container-fluid page-body-wrapper full-page-wrapper">
          <div class="content-wrapper d-flex align-items-center auth">
            <div class="row w-100 flex-grow">
              <div class="col-lg-6 mx-auto">
                <div class="bg-white border rounded text-left p-5">
                  <div class="brand-logo">
                    <img src="../../assets/images/Logo_Name.png" />
                  </div>
                  <h4>Novo animal?</h4>
                  <h5 class="font-weight-light">Para se cadastrar é fácil!</h5>
                  <h6 class="font-weight-light">
                    Basta preencher os campos abaixo:
                  </h6>
                  <b-form class="pt-3" @submit.prevent="petRegisterApi">
                    <b-form-group>
                      <b-form-input
                        v-model="petData.name"
                        
                        id="inputpetname"
                        placeholder="Nome Completo"
                        :class="{
                          'is-invalid': submitted && $v.petData.name.$error,
                        }"
                      >
                      </b-form-input>
                      <div
                        v-if="submitted && $v.petData.name.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.petData.name.required"
                          >Nome é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    
                    



                    <div  class="mt-3">
                      <b-button block size="lg" :disabled="isLoading" variant="primary" type="submit">
                        <div class="text-center align-items-center">
                          <span v-if="!isLoading">ENVIAR</span>
                          <b-spinner v-else small></b-spinner>
                        </div>
                      </b-button>
                    </div>
                    <div class="text-center mt-4 font-weight-light">
                      Já tem uma conta?
                      <router-link to="login" class="text-primary"
                        >Cadastrar</router-link
                      >
                    </div>
                  </b-form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import { required, raca, minLength, sameAs } from "vuelidate/lib/validators";
  import customValidators from "../../plugins/vuelidateValidators";
  import PlgpetsApi from "../../apis/PlgpetsApi.vue";
  import Vue from "vue";
  import Toasts from "../../components/Toasts.vue";
  
  
  export default {
    name: "registerAnimal",
    data() {
      const now = new Date();
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
      const initialDate = new Date(today);
      initialDate.setFullYear(initialDate.getFullYear() - 18);
      const maxDate = new Date(today);
      maxDate.setMonth(maxDate.getMonth());
      maxDate.setDate(now.getDate());
  
      return {
        maxDate: maxDate,
        initialDate: initialDate,
        states: statesOptions.statesOptions,
        seePassword: false,
        seeConfirmPassword: false,
        userData: {
          name: null,
          raca: null,
        },
        isLoading: false,
        submitted: false,
        sliceAddressRes: null,
        addressCheck: false,
        };
    },
    validations() {
      return {
        userData: {
          name: {
            required,
          },
          raca: {
            required,
          },
        },
      }
    },
    components: { 
      Toasts,
      PlgpetsApi
    },

      async petRegisterApi() {
        
        this.submitted = true;
        this.$v.$touch();
        if (!this.$v.$invalid) {
          if (this.userData.termsCheck) {
            const petRegisterPayload = {
              user: {
                name: this.userData.name,
                raca: this.userData.raca,
                is_confirmed: false,
                role: "user",
              },
            };
            this.isLoading = true;
            const response = await this.$refs.PlgpetsApi.saveUserApi(petRegisterPayload);
            this.isLoading = false;
              this.$refs.Toasts.showToast(
                response.data.status,
                response.data.message
              );
            }
          }
        }

  };
  </script>
  
  <style scoped>
  .select-field {
    height: 46px;
  }
  .placeholder-text {
    color: #d6d5d5;
  }
  </style>