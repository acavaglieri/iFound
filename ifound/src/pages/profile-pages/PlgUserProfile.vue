<template>
  <div>
    <Toasts ref="Toasts"></Toasts>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <section v-if="user" class="profile">
      <div class="row">
        <div class="col-12">
          <div class="card border rounded">
            <div class="card-body">
              <div class="row">
                <div class="col-lg-4">
                  <div class="border-bottom text-center pb-4">
                    <img
                      src="../../assets/images/faces/user-placeholder.png"
                      alt="profile"
                      class="img-lg rounded-circle mb-3"
                    />
                    <b-row align-h="center" class="my-2">
                      {{user.name}}
                    </b-row>
                    <div>
                      <b-button-group vertical>
                        <b-button variant="primary" @click="userInfoForm = true, addressForm = false">Informações Pessoais</b-button>
                        <!--<b-button variant="primary" @click="addressForm = true, userInfoForm = false" class="mt-2">Endereço</b-button> -->
                        <!-- <b-button v-show="!isLoadingResetPass" variant="primary" @click="sendResetEmail" class="mt-2">Alterar Senha</b-button> -->
                        <b-button v-show="isLoadingResetPass" variant="primary" disabled class="mt-2"><b-spinner small></b-spinner></b-button>
                      </b-button-group>
                    </div>
                  </div>
                </div>
                <div class="col-lg-8">
                  <form v-show="userInfoForm && !addressForm" @submit.prevent="" @reset.prevent="" class="forms-sample mt-3">
                    <div class="col-xl-12">
                      <div class="row">
                        <!--DETALHES-->
                        <div class="col-xl-12"> 
                          <div class="">
                            <div class="">
                              <h4 class="card-title">Detalhes</h4>
                                <div class="text-right">
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
                                </div>
                              <div class="container-fluid">
                                <b-form-group label="Nome" label-for="inputName">
                                  <b-form-input
                                    v-model="user.name"
                                    type="text"
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
                                      :date-format-options="{
                                        year: 'numeric',
                                        month: 'long',
                                        day: '2-digit',
                                      }"
                                      :max="maxDate"
                                      hide-header
                                      size="sm"
                                      selected-variant="primary"
                                      :initial-date="initialDate"
                                      label-no-date-selected
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
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </form>
                  <!--<form v-show="addressForm && !userInfoForm" class="forms-sample mt-3">
                    <div class="col-xl-12">
                      <div class="row"> -->
                        <!--ENDEREÇO DO USUÁRIO-->
                        <!--
                        <div class="col-xl-12">
                          <div class="">
                            <div class="">
                              <h4 class="card-title">Endereço</h4>
                                <div class="text-right">
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
                                </div>
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
                                    :options="userStatesOpts"
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
                        </div> 
                      </div>
                    </div>
                  </form>-->
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import PlgUsersApi from "../../apis/PlgUsersApi.vue";
import moment from "moment";
import { required, email, minLength } from "vuelidate/lib/validators";
import customValidators from "../../plugins/vuelidateValidators";
import states from "../../helpers/users-opts/statesOptions";
import roles from "../../helpers/users-opts/usersRolesOpts";
import Toasts from "../../components/Toasts.vue";



export default {
  name: "profile",
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const initialDate = new Date(today);
    initialDate.setFullYear(initialDate.getFullYear() - 18);
    const maxDate = new Date(today);
    maxDate.setMonth(maxDate.getMonth());
    maxDate.setDate(now.getDate());
    return {
      isLoading: false,
      userStatesOpts: states.statesOptions,
      userRolesOpts: roles.userRolesOpts,
      birthdayFromDatePicker: null,
      initialDate: initialDate,
      maxDate: maxDate,
      userId: null,
      isLoadingResetPass: false,
      user: null,
      addressForm: false,
      userInfoForm: true,
      submitted: false,
    };
  },
  components: { 
    Toasts,
    PlgUsersApi, 
  },
  validations: {
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
      /*address: {
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
  },
  methods: {
    formatDateFromDatePicker() {
      this.user.birthday = moment(this.birthdayFromDatePicker).format("DD/MM/YYYY");
    },
    async sendResetEmail() {
      const UserTokenPayload = {
        email: this.user.email,
      };
      this.isLoadingResetPass = true;
      let response = await this.$refs.PlgUsersApi.getTokenApi(UserTokenPayload);
      this.isLoadingResetPass = false;
      this.$refs.Toasts.showToast(response.data.status, response.data.message);
    },
    async sendUserDataApi() {
      this.submitted = true;
      this.$v.$touch();
      if (!this.$v.$invalid) {
        this.userId = this.user.id;
        const payload = {
          user: {
            name: this.user.name,
            cellphone: this.user.cellphone,
            email: this.user.email,
            birthday: moment(this.user.birthday, "DD-MM-YYYY").toISOString(),
            role: this.user.role,
            password: this.user.password,
            federal_id: this.user.federal_id,
          },
        };
        this.isLoading = true;
        let response = await this.$refs.PlgUsersApi.updateUserApi(this.userId, payload);
        this.isLoading = false;
        this.$refs.Toasts.showToast(
          response.data.status,
          response.data.message
        );
      }
    },
  },
  watch: {
    birthdayFromDatePicker() {
      this.formatDateFromDatePicker()
    }
  },
  async mounted() {
    let response = await this.$refs.PlgUsersApi.getCurrentUser();
    let formattedBirthday = moment(response.data.birthday).format("DD/MM/YYYY");
    this.user = response.data;
    this.user.birthday = formattedBirthday;
  }
};
</script>