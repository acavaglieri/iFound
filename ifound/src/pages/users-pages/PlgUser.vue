<template>
  <div>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <Toasts ref="Toasts"></Toasts>
    <div v-if="user">
      <div class="col-xl-12 mb-3">
        <div class="row">
          <div class="col-6">
            <h4 class="font-weight-bold mt-2">
              {{ getTitleForm }}
            </h4>
          </div>
          <div class="col-6 text-right">
            <b-btn
              v-show="!isLoading"
              class="btn btn-success btn-sm text-white mr-2"
              @click="sendUserDataApi()"
              v-b-tooltip.html.bottom
              title="Confirmar"
              ><i class="mdi mdi-check" />
            </b-btn>
            <b-btn
              v-show="isLoading"
              class="btn btn-success btn-sm text-white mr-2"
              @click="sendUserDataApi()"
              v-b-tooltip.html.bottom
              disabled
              >
              <div class="text-center align-items-center">
                <b-spinner small></b-spinner>
              </div>
            </b-btn>
            <b-btn
              class="btn btn-danger btn-sm text-white mr-2"
              @click="goToListUsers()"
              v-b-tooltip.html.bottom
              title="Cancelar"
              ><i class="mdi mdi-close" />
            </b-btn>
          </div>
        </div>
      </div>
      <form @submit.prevent="" @reset.prevent="" class="forms-sample mt-3">
        <div class="col-xl-12">
          <div class="row">
            <!--DETALHES-->
            <div class="col-xl-6 grid-margin stretch-card">
              <div class="card border-0">
                <div class="card-body">
                  <h4 class="card-title">Detalhes</h4>
                  <div class="container-fluid">
                    <b-form-group label="Nome" label-for="inputName">
                      <b-form-input
                        v-model="user.name"
                        type="text"
                        placeholder="Nome"
                        id="inputName"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.name.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.name.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.name.required"
                          >Nome é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Celular" label-for="inputCellphone">
                      <b-form-input
                        v-model="user.cellphone"
                        v-mask="['(##) ####-####', '(##) #####-####']"
                        type="text"
                        id="inputCellphone"
                        placeholder="Celular"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.cellphone.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.cellphone.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.cellphone.required"
                          >Celular é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Data de Nascimento" label-for="inputBirthday">
                      <b-input-group>
                        <b-form-input
                            v-model="user.birthday"
                            v-mask="['##/##/####']"
                            id="inputBirthday"
                            placeholder="Data de Nascimento"
                            :class="{
                              'is-invalid': submitted && $v.user.birthday.$error,
                            }"
                          >
                          </b-form-input>
                          <b-form-datepicker
                            v-model="birthdayFromDatePicker"
                            button-only
                            button-variant="primary"
                            placeholder="Escolha uma data"
                            locale="pt-br"
                            size="sm"
                            label-help="Use as setas para navegar"
                            label-no-date-selected
                            :date-format-options="{
                              year: 'numeric',
                              month: 'long',
                              day: '2-digit',
                            }"
                            :max="maxDate"
                            selected-variant="primary"
                            hide-header
                            :initial-date="initialDate"
                            :class="{
                              'is-invalid': submitted && $v.user.birthday.$error,
                            }"
                          ></b-form-datepicker>
                      </b-input-group>
                      <div
                        v-if="submitted && $v.user.birthday.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.birthday.required"
                          >Data de nascimento é obrigatória.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Email" label-for="inputEmail">
                      <b-form-input
                        v-model="user.email"
                        type="text"
                        placeholder="Email"
                        id="inputEmail"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.email.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.email.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.email.required"
                          >Email é obrigatório.</span
                        >
                      </div>
                      <div
                        v-if="submitted && $v.user.email.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.email.email"
                          >Email deve ser válido.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group
                      v-show="!this.userId"
                      label="Senha"
                      label-for="inputPassword"
                    >
                      <b-input-group>
                        <b-form-input
                          v-model="user.password"
                          type="password"
                          id="inputPassword"
                          placeholder="Senha"
                          size="sm"
                          :class="{
                            'is-invalid': submitted && $v.user.password.$error,
                          }"
                        ></b-form-input>
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
                          v-if="submitted && $v.user.password.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.user.password.required"
                            >Senha é obrigatória.</span
                          >
                        </div>
                      </b-input-group>
                    </b-form-group>
                    <b-form-group v-show="!this.userId">
                      <b-input-group>
                        <b-form-input
                          type="password"
                          v-model="user.rePassword"
                          id="inputRePassword"
                          size="sm"
                          placeholder="Confirme a senha"                      
                          :class="{
                            'is-invalid': submitted && $v.user.rePassword.$error,
                          }"
                        ></b-form-input>
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
                          v-if="submitted && $v.user.rePassword.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.user.rePassword.required"
                            >Confirme a senha.</span
                          >
                        </div>
                        <div
                          v-if="submitted && $v.user.rePassword.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.user.rePassword.sameAsPassword && $v.user.rePassword.required"
                            >Senhas não conferem!</span
                          >
                        </div>
                      </b-input-group>
                    </b-form-group>
                    <b-form-group label="CPF" label-for="inputFederalId">
                      <b-form-input
                        v-model="user.federal_id"
                        type="text"
                        v-mask="['###.###.###-##']"
                        id="inputFederalId"
                        placeholder="CPF"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.federal_id.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.federal_id.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.federal_id.required"
                          >CPF é obrigatório.</span
                        >
                      </div>
                      <div
                        v-if="submitted && $v.user.federal_id.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.federal_id.cpfValidCheck && user.federal_id"
                          >CPF deve ser válido.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Permissões" label-for="inputRole">
                      <b-form-select
                        v-model="user.role"
                        :options="userRolesOpts"
                        id="inputRole"
                        size="md"
                        :class="{
                          'is-invalid': submitted && $v.user.role.$error,
                        }"
                      ></b-form-select>
                      <div
                        v-if="submitted && $v.user.role.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.role.required"
                          >Permissões do usuário devem ser especificadas.</span
                        >
                      </div>
                    </b-form-group>
                  </div>
                </div>
              </div>
            </div>
            <!--ENDEREÇO DO USUÁRIO-->
            <!--
            <div class="col-xl-6 grid-margin stretch-card">
              <div class="card border-0">
                <div class="card-body">
                  <h4 class="card-title">Endereço</h4>
                  <div class="container-fluid">
                    <b-form-group label="Logradouro" label-for="inputAddress">
                      <b-form-input
                        v-model="user.address"
                        type="text"
                        id="inputAddress"
                        placeholder="Logradouro"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.address.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.address.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.address.required"
                          >Logradouro é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Número" label-for="inputHouseNumber">
                      <b-form-input
                        v-model="user.house_number"
                        type="text"
                        id="inputHouseNumber"
                        placeholder="Número"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.house_number.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.house_number.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.house_number.required"
                          >Número é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Bairro" label-for="inputQuarter">
                      <b-form-input
                        v-model="user.quarter"
                        type="text"
                        id="inputQuarter"
                        placeholder="Bairro"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.quarter.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.quarter.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.quarter.required"
                          >Bairro é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Cidade" label-for="inputCity">
                      <b-form-input
                        v-model="user.city"
                        type="text"
                        id="inputCity"
                        placeholder="Cidade"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.city.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.city.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.city.required"
                          >Cidade é obrigatória.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="CEP" label-for="inputZipCode">
                      <b-form-input
                        v-model="user.zip_code"
                        type="text"
                        id="inputZipCode"
                        v-mask="['#####-###']"
                        placeholder="CEP"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.user.zip_code.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.user.zip_code.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.zip_code.required"
                          >CEP é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Estado" label-for="inputState">
                      <b-form-select
                        v-model="user.state"
                        :options="states"
                        id="inputState"
                        placeholder="Estado"
                        size="md"
                        :class="{
                          'is-invalid': submitted && $v.user.state.$error,
                        }"
                      ></b-form-select>
                      <div
                        v-if="submitted && $v.user.state.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.user.state.required"
                          >Estado é obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                  </div>
                </div>
              </div>
            </div> -->
          </div> 
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { required, email, minLength, sameAs } from "vuelidate/lib/validators";
import customValidators from "../../plugins/vuelidateValidators";
import PlgUsersApi from "../../apis/PlgUsersApi.vue";
import statesOptions from "../../helpers/users-opts/statesOptions";
import roles from "../../helpers/users-opts/usersRolesOpts";
import Toasts from "../../components/Toasts.vue";
import moment from "moment";


export default {
  name: "PlgUserForm",
  components: { 
    Toasts,
    PlgUsersApi,
  },
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const initialDate = new Date(today);
    initialDate.setFullYear(initialDate.getFullYear() - 18);
    const maxDate = new Date(today);
    maxDate.setMonth(maxDate.getMonth());
    maxDate.setDate(now.getDate());
    return {
      birthdayFromDatePicker: null,
      isLoading: false,
      states: statesOptions.statesOptions,
      userRolesOpts: roles.userRolesOpts,
      initialDate: initialDate,
      maxDate: maxDate,
      userId: null,
      user: null,
      eyeIconPass: "mdi mdi-eye mdi-18px",
      eyeIconRePass: "mdi mdi-eye mdi-18px",
      submitted: false,
    };
  },
  validations() {
    if(!this.userId) {
      return {
        user: {
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
          birthday: {
            required,
          },  
          federal_id: {
            required,
            cpfValidCheck: customValidators.cpfValidCheck(),
          },
          password: {
            required,
          },
          rePassword: {
            required, 
            sameAsPassword: sameAs('password')
          },
          /*role: {
            required,
          },
          address: {
            required,
          },
          house_number: {
            required,
          },
          quarter: {
            required,
          },
          city: {
            required,
          },
          zip_code: {
            required,
          },
          state: {
            required,
          },*/
        }
      }
    }else {
      return {
        user: {
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
          birthday: {
            required,
          },  
          federal_id: {
            required,
            cpfValidCheck: customValidators.cpfValidCheck(),
          },
          /*role: {
            required,
          },
          address: {
            required,
          },
          house_number: {
            required,
          },
          quarter: {
            required,
          },
          city: {
            required,
          },
          zip_code: {
            required,
          },
          state: {
            required,
          },*/
        },
      }
    }
  },
  methods: {
    goToListUsers() {
      this.$router.push({ name: "users" }).catch();
    },
    formatDateFromDatePicker() {
      this.user.birthday = moment(this.birthdayFromDatePicker).format("DD/MM/YYYY");
    },
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
    async sendUserDataApi() {
      this.submitted = true;
      this.$v.$touch();
      if (!this.$v.$invalid) {
        const payload = {
          user: {
            name: this.user.name,
            cellphone: this.user.cellphone,
            email: this.user.email,
            birthday: moment(this.user.birthday, "DD-MM-YYYY").toISOString(),
            role: this.user.role,
            password: this.user.password,
            federal_id: this.user.federal_id,
            /*address: this.user.address,
            house_number: this.user.house_number,
            quarter: this.user.quarter,
            zip_code: this.user.zip_code,
            city: this.user.city,
            state: this.user.state,
            is_confirmed: true,
            country: "Brazil",*/
          },
        };
        this.isLoading = true;
        if (!this.userId) {
          let response = await this.$refs.PlgUsersApi.addNewUserAsAdmin(payload);
          this.isLoading = false;
          if (response.data.status === "success") {
            this.$router.push({ name: "users" }).catch();
          }
          this.$refs.Toasts.showToast(
            response.data.status,
            response.data.message
          );
        } else {
          let response = await this.$refs.PlgUsersApi.updateUserApi(this.userId, payload);
          this.isLoading = false;
          if (response.data.status === "success") {
            this.$router.push({ name: "users" }).catch();
          }
          this.$refs.Toasts.showToast(
            response.data.status,
            response.data.message
          );
        }
      }
    },
  },
  computed: {
    getTitleForm() {
      return this.user != null && this.user.id != null
        ? `Usuário Nº: ${this.user.id}`
        : "Novo usuário";
    },
  },
  watch: {
    birthdayFromDatePicker() {
      this.formatDateFromDatePicker()
    }
  },
  async mounted() {
    this.userId = this.$route.params.id;
    if (this.userId != null) {
      let response = await this.$refs.PlgUsersApi.getUserApi(this.userId);
      let formattedBirthday = moment(response.birthday).format("DD/MM/YYYY");
      this.user = response;
      this.user.birthday = formattedBirthday;
    } else {
      this.user = {};
      this.user.id = null;
    }
    if(!this.$can('view', 'apis')) {
      this.$router.push({name: 'home'})
    }
  },
};
</script>