<template>
  <section class="register">
    <Toasts ref="Toasts"></Toasts>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <div class="container-scroller">
      <div class="container-fluid page-body-wrapper full-page-wrapper">
        <div class="content-wrapper d-flex align-items-center auth">
          <div class="row w-100 flex-grow">
            <div class="col-lg-6 mx-auto">
              <div class="bg-white border rounded text-left p-5">
                <div class="brand-logo">
                  <img src="../../assets/images/Logo_Name.png" />
                </div>
                <h4>Novo por aqui?</h4>
                <h5 class="font-weight-light">Para se cadastrar é fácil!</h5>
                <h6 class="font-weight-light">
                  Basta preencher os campos abaixo:
                </h6>
                <b-form class="pt-3" @submit.prevent="userRegisterApi">
                  <b-form-group>
                    <b-form-input
                      v-model="userData.name"
                      
                      id="inputUsername"
                      placeholder="Nome Completo"
                      :class="{
                        'is-invalid': submitted && $v.userData.name.$error,
                      }"
                    >
                    </b-form-input>
                    <div
                      v-if="submitted && $v.userData.name.$error"
                      class="invalid-feedback"
                    >
                      <span v-if="!$v.userData.name.required"
                        >Nome é obrigatório.</span
                      >
                    </div>
                  </b-form-group>
                  <b-form-group>
                    <b-form-input
                      v-model="userData.email"
                      
                      id="inputEmail"
                      placeholder="Email"
                      :class="{
                        'is-invalid': submitted && $v.userData.email.$error,
                      }"
                    >
                    </b-form-input>
                    <div
                      v-if="submitted && $v.userData.email.$error"
                      class="invalid-feedback"
                    >
                      <span v-if="!$v.userData.email.required"
                        >Email é obrigatório.</span
                      >
                    </div>
                    <div
                      v-if="submitted && $v.userData.email.$error"
                      class="invalid-feedback"
                    >
                      <span v-if="!$v.userData.email.email"
                        >Email deve ser válido.</span
                      >
                    </div>
                  </b-form-group>
                  <b-row>

                    <b-col>
                      <b-form-group>
                        <b-form-input
                          v-model="userData.cellphone"
                          type="tel"
                          id="inputCellphone"
                          v-mask="['(##) ####-####', '(##) #####-####']"
                          placeholder="Celular"
                          :class="{
                            'is-invalid': submitted && $v.userData.cellphone.$error,
                          }"
                        >
                        </b-form-input>
                        <div
                          v-if="submitted && $v.userData.cellphone.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.userData.cellphone.required"
                            >Celular é obrigatório.</span
                          >
                        </div>
                      </b-form-group>
                    </b-col>
                    <b-col cols="6">
                      <b-form-group>
                        <b-input-group>
                          <b-form-input
                            v-model="userData.birthday"
                            v-mask="['##/##/####']"
                            id="inputBirthday"
                            placeholder="Data de Nascimento"
                            :class="{
                              'is-invalid': submitted && $v.userData.birthday.$error,
                            }"
                          >
                          </b-form-input>
                          <b-form-datepicker
                            v-model="birthdayFromDatePicker"
                            button-only
                            locale="pt-br"
                            :date-format-options="{
                              year: 'numeric',
                              month: 'numeric',
                              day: 'numeric',
                            }"
                            size="sm"
                            button-variant="primary"
                            placeholder="Data de Nascimento"
                            :max="maxDate"
                            :hide-header=true
                            @input="formatDateFromDatePicker()"
                            selected-variant="primary"
                            label-help="Use as setas para navegar"
                            :initial-date="initialDate"
                            label-no-date-selected
                            :class="{
                              'is-invalid': submitted && $v.userData.birthday.$error,
                            }"
                          >
                          </b-form-datepicker>
                          <div
                            v-if="submitted && $v.userData.birthday.$error"
                            class="invalid-feedback"
                          >
                            <span v-if="!$v.userData.birthday.required"
                              >Data de nascimento é obrigatória.</span
                            >
                          </div>
                        </b-input-group>
                      </b-form-group>
                    </b-col> 
                  </b-row>
                  <b-form-group>
                    <b-form-input
                      v-model="userData.federalId"
                      type="tel"
                      id="inputFederalId"
                      v-mask="['###.###.###-##']"
                      placeholder="CPF"
                      :class="{
                        'is-invalid': submitted && $v.userData.federalId.$error,
                      }"
                    >
                    </b-form-input>
                    <div
                      v-if="submitted && $v.userData.federalId.$error"
                      class="invalid-feedback"
                    >
                      <span v-if="!$v.userData.federalId.required"
                        >CPF é obrigatório.</span
                      >
                    </div>
                    <div
                      v-if="submitted && $v.userData.federalId.$error"
                      class="invalid-feedback"
                    >
                      <span v-if="!$v.userData.federalId.cpfValidCheck && userData.federalId"
                        >CPF deve ser válido.</span
                      >
                    </div>
                  </b-form-group>
                    <b-form-group>
                      <b-input-group>
                        <b-form-input
                          v-model="userData.password"
                          :type="seePassword ? 'text' : 'password'"
                          id="inputPassword"
                          placeholder="Senha"
                          :class="{
                            'is-invalid': submitted && $v.userData.password.$error,
                          }"
                        ></b-form-input>
                          <b-button
                            @click="seePassword = !seePassword"
                            :class="passwordIcon"
                            style="color: #fff;"
                            aria-hidden="true"
                            variant="primary"
                            size="sm"
                            squared
                          ></b-button>
                        <div
                          v-if="submitted && $v.userData.password.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.userData.password.required"
                            >Senha é obrigatória.</span
                          >
                        </div>
                      </b-input-group>
                    </b-form-group>
                    <b-form-group>
                      <b-input-group>
                        <b-form-input
                          :type="seeConfirmPassword ? 'text' : 'password'"
                          v-model="userData.rePassword"
                          id="inputRePassword"
                          placeholder="Confirme a senha"                      
                          :class="{
                            'is-invalid': submitted && $v.userData.rePassword.$error,
                          }"
                        ></b-form-input>
                        <b-button
                          @click="seeConfirmPassword = !seeConfirmPassword"
                          :class="confirmPasswordIcon"
                          style="color: #fff;"
                          aria-hidden="true"
                          variant="primary"
                          size="sm"
                          squared
                        ></b-button>
                        <div
                          v-if="submitted && $v.userData.rePassword.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.userData.rePassword.required"
                            >Confirme a senha.</span
                          >
                        </div>
                        <div
                          v-if="submitted && $v.userData.rePassword.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.userData.rePassword.sameAsPassword && $v.userData.rePassword.required"
                            >Senhas não conferem!</span
                          >
                        </div>
                      </b-input-group>
                    </b-form-group>
                  <!--<div class="">
                    <gmap-autocomplete
                      id="google-search-address"
                      placeholder="Endereço/Local ou CEP"
                      size="sm"
                      :options="{ 
                        fields: ['geometry'],
                        componentRestrictions: {
                          country: 'br'
                        }
                      }"
                      @place_changed="setAddressFromMap"
                      class="form-control"
                    ></gmap-autocomplete>
                  </div>
                  <div class="mt-3">
                    <GmapMap
                      ref="mapRef"
                      :center="{ lat: -23.550278, lng: -46.633889 }"
                      :zoom="10"
                      style="height: 300px"
                      map-type-id="roadmap"
                    >
                      <gmap-marker
                        v-for="(m, index) in mapMarkers"
                        :key="index"
                        :position="m.position"
                      ></gmap-marker>
                    </GmapMap>
                  </div>
                  -->
                  <div class="mb-4">
                    <b-form-group class="form-check">
                      <label class="form-check-label text-muted">
                        <input
                          type="checkbox"
                          :class="{
                            'is-invalid': submitted && $v.userData.termsCheck.$error,
                            'form-check-input': true
                          }"
                          v-model="userData.termsCheck"
                        />
                        Eu concordo com os <a href="https://drive.google.com/file/d/1HhX5IIPHqgYTklxeUq-bbPjsgjzMujCQ/view?usp=sharing" class="text-primary"> Termos e Condições</a>
                        <!--<a href="../src/assets/POLÍTICAdePRIVACIDADE_iFound.pdf">Eu concordo com os Termos e Condições</a>-->
                        <i class="input-helper"></i>
                        <div
                          v-if="submitted && $v.userData.termsCheck.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.userData.termsCheck.sameAsTrue">
                            É necessário que você concorde com os termos!
                          </span>
                        </div>
                      </label>
                    </b-form-group>
                  </div>
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
                      >Entrar</router-link
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
import { required, email, minLength, sameAs } from "vuelidate/lib/validators";
import customValidators from "../../plugins/vuelidateValidators";
import PlgUsersApi from "../../apis/PlgUsersApi.vue";
import googleApi from "../../apis/PlgGoogleApi";
import * as VueGoogleMaps from "vue2-google-maps";
import statesOptions from "../../helpers/users-opts/statesOptions";
import Vue from "vue";
import { cities } from "brazil-geodata";
import Toasts from "../../components/Toasts.vue";


Vue.use(VueGoogleMaps, {
  load: {
    key: `${process.env.VUE_APP_GOOGLE_API}`,
    libraries: "places",
    language: "pt-BR",
  },
});

export default {
  name: "register",
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
        email: null,
        cellphone: null,
        password: null,
        federalId: "",
        rePassword: null,
        termsCheck: null,
      },
      isLoading: false,
      submitted: false,
      sliceAddressRes: null,
      addressCheck: false,
      googleRenderParams: {
        width: 60,
        height: 37,
        longtitle: true,
      },
      currentMapPlace: null,
      mapCenter: { lat: -23.550278, lng: -46.633889 },
      mapMarkers: [],
      marker: "",
      map: undefined,
    };
  },
  validations() {
    return {
      userData: {
        name: {
          required,
        },
        email: {
          required,
          email,
        },
        cellphone: {
          required,
          minLength: minLength(11),
        },
        password: {
          required,
        },
        rePassword: {
          required,
          sameAsPassword: sameAs('password')
        },
        federalId: {
          required,
          cpfValidCheck: customValidators.cpfValidCheck(),
        },
        termsCheck: {
          sameAsTrue: sameAs( () => true )
        },
      },
    }
  },
  mixins: [googleApi],
  components: { 
    Toasts,
    PlgUsersApi
  },
  watch: {
    'userData.state'() {
      this.getCitiesOptions()
    }
  },
  computed: {
    passwordIcon() {
      return this.seePassword ? "mdi mdi-eye-off mdi-18px" : "mdi mdi-eye mdi-18px"
    },
    confirmPasswordIcon() {
      return this.seeConfirmPassword ? "mdi mdi-eye-off mdi-18px" : "mdi mdi-eye mdi-18px"
    },
    google: VueGoogleMaps.gmapApi,
  },
  methods: {
    checkIfCityIsInCitiesOptions() {
      this.citiesOptions.indexOf(this.userData.city) >= 0 ? true : this.userData.city = null;
    },
    async getCitiesOptions() {
      this.citiesOptions = await cities.getCitiesByState(this.userData.state);
			this.citiesOptions = this.citiesOptions.map((city) => {
				return city.text;
			})
      this.checkIfCityIsInCitiesOptions();
      this.citiesOptions.splice(0, 0, {text: "Cidade", value: null})
    },
    clearUserAddress() {
      const userAddressFields = ['street', 'houseNumber', 'district', 'city', 'state', 'zipCode'];
      Object.keys(this.userData).forEach((key) => {
        if (userAddressFields.includes(key)) {
          this.userData[key] = null;
        }
      }) 
    },
    setAddressFromMap(place) {
      if (place && place.geometry) {
        this.userData.fullAddress = document.getElementById(
          "google-search-address"
        ).value;
        this.currentMapPlace = place;
        this.latitude = place.geometry.location.lat();
        this.longitude = place.geometry.location.lng();
        this.mapCenter = {
          lat: this.latitude,
          lng: this.longitude,
        };
        this.mapMarkers = [{ position: this.mapCenter }];
        this.marker = [{ position: this.mapCenter }];
        var bounds = new this.google.maps.LatLngBounds();
        if (place.geometry.viewport) {
          bounds.union(place.geometry.viewport);
        } else {
          bounds.extend(place.geometry.location);
        }
        this.map.fitBounds(bounds);
        this.sliceAddressApi();
      }
    },
    async syncData(sliceAddressRes) {
      const keys = Object.keys(sliceAddressRes);

      function removeUndefinedFields(index) {
        if (!sliceAddressRes[index]) {
          delete sliceAddressRes[index];
        }
      }
      keys.forEach(removeUndefinedFields);
      this.sliceAddressRes = sliceAddressRes;

      Object.entries(sliceAddressRes).forEach((entry) => {
        const [key, value] = entry;
        this.userData[key] = value;
      });
    },
    async sliceAddressApi() {
      if (this.userData.fullAddress) {
        let response = await this.sliceAddress(this.userData.fullAddress);
        this.sliceAddressRes = response.data;
        this.clearUserAddress()
        this.syncData(this.sliceAddressRes);
        this.addressCheck = true;
      } else {
        this.sliceAddressRes = null;
      }
      return this.sliceAddressRes;
    },
    async getZipCodeData() {
      if (this.userData.zipCode) {
        let response = await this.$viaCep.buscarCep(this.userData.zipCode);
        this.clearUserAddress()
        this.userData.street = response.logradouro;
        this.userData.district = response.bairro;
        this.userData.city = response.localidade;
        this.userData.state = response.uf;
        this.userData.zipCode = response.cep;
        document.getElementById("inputHouseNumber").focus();
      }
    },
    async userRegisterApi() {
      
      this.submitted = true;
      this.$v.$touch();
      if (!this.$v.$invalid) {
        if (this.userData.termsCheck) {
          const userRegisterPayload = {
            user: {
              name: this.userData.name,
              email: this.userData.email.toLowerCase(),
              cellphone: this.userData.cellphone,
              password: this.userData.password,
              federal_id: this.userData.federalId,
              is_confirmed: false,
              role: "user",
            },
          };
          this.isLoading = true;
          const response = await this.$refs.PlgUsersApi.saveUserApi(userRegisterPayload);
          this.isLoading = false;
          if (response.data.status === "success") {
            this.$router.push({ name: "user_confirm_email_sent_warning" });
          } else {
            this.$refs.Toasts.showToast(
              response.data.status,
              response.data.message
            );
          }
        }
      }
    },
  },
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