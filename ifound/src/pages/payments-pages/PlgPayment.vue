<!--<template>
  <div>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <Toasts ref="Toasts"></Toasts>
    <div>
      <div class="col-xl-12 mb-3">
        <div class="row">
          <div class="col-6">
            <h4>
              {{ formTitle }}
            </h4>
          </div>
          <div class="col-6 text-right">
            <b-btn
              :disabled="isLoading"
              class="btn btn-success btn-sm text-white mr-2"
              @click="sendPaymentDataApi()"
              v-b-tooltip.html.bottom
              title="Confirmar"
              >
              <div class="text-center align-items-center">
                <b-spinner v-if="isLoading" small></b-spinner>
                <i v-else class="mdi mdi-check" />
              </div>
            </b-btn>
            <b-btn
              class="btn btn-danger btn-sm text-white mr-2"
              @click="goToFinds()"
              v-b-tooltip.html.bottom
              title="Cancelar"
              ><i class="mdi mdi-close" />
            </b-btn>
          </div>
        </div>
      </div>
      <form class="forms-sample mt-3">
        <div class="col-xl-12">
          <div class="row">
            <div class="col-xl-12 grid-margin stretch-card">
              <div class="card border rounded">
                <div class="card-body">
                  <h4 class="card-title">Pagamento</h4>
                  <div class="container-fluid">
                    <b-form-group v-if="!paymentId" label="CPF do Recebedor" label-for="inputReceiverFederalId">
                      <b-form-input
                        v-model="payment.receiver_federal_id"
                        id="inputReceiverFederalId"
                        type="tel"
                        @input="searchReceiversByFederalId"
                        v-mask="['###.###.###-##']"
                        placeholder="CPF do Recebedor"
                        size="sm"
                        :class="{
                          'is-invalid': submitted && $v.payment.receiver_federal_id.$error,
                        }"
                      ></b-form-input>
                      <div 
                        v-show="items.length > 0 && payment.receiver_federal_id.length < 14"
                        class="autocomplete"
                      >
                        <ul
                          class="autocomplete-results"
                        >
                          <li
                            v-for="(item, index) in items"
                            :key="index"
                            class="autocomplete-result"
                            @click="getFederalIdFromResult(item.federal_id)"
                          >
                            {{ item.name }} - {{ item.federal_id }}
                          </li>
                        </ul>
                      </div>
                      <div
                        v-if="submitted && $v.payment.receiver_federal_id.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.payment.receiver_federal_id.required"
                          >CPF é obrigatório.</span
                        >
                      </div>
                      <div
                        v-if="submitted && $v.payment.receiver_federal_id.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.payment.receiver_federal_id.cpfValidCheck && payment.receiver_federal_id"
                          >CPF deve ser válido.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Quantia" label-for="inputAmount">
                      <money
                        v-model="payment.amount"
                        type="text"
                        id="inputAmount"
                        placeholder="Quantia"
                        size="sm"
                        v-bind="money"
                        maxlength="10"
                        class="form-control form-control-sm"
                        :class="{
                          'is-invalid': submitted && $v.payment.amount.$error,
                        }"
                      ></money>
                      <div
                        v-if="submitted && $v.payment.amount.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.payment.amount.required || !$v.payment.amount.minValue"
                          >Quantia é obrigatória.</span
                        >
                      </div>
                    </b-form-group>
                    <b-form-group label="Data do Pagamento" label-for="inputScheduledDate">
                      <b-input-group>
                        <b-form-input
                          v-model="payment.scheduled_date"
                          v-mask="['##/##/####']"
                          id="inputScheduledDate"
                          placeholder="Data do Pagamento"
                          :class="{
                            'is-invalid': submitted && $v.payment.scheduled_date.$error,
                          }"
                        >
                        </b-form-input>
                        <b-form-datepicker
                          v-model="scheduledDateFromDatePicker"
                          button-only
                          locale="pt-br"
                          :date-format-options="{
                            year: 'numeric',
                            month: 'numeric',
                            day: 'numeric',
                          }"
                          id="inputScheduledDate"
                          button-variant="primary"
                          :hide-header=true
                          placeholder="Data do Pagamento"
                          @input="formatDateFromDatePicker()"
                          selected-variant="primary"
                          label-help="Use as setas para navegar"
                          label-no-date-selected
                          size="sm"
                          dropright
                          :min="minDate"
                          :class="{
                            'is-invalid': submitted && $v.payment.scheduled_date.$error,
                          }"
                        ></b-form-datepicker>
                        <div
                          v-if="submitted && $v.payment.scheduled_date.$error"
                          class="invalid-feedback"
                        >
                          <span v-if="!$v.payment.scheduled_date.required"
                            >Data do pagamento é obrigatória.</span
                          >
                        </div>
                      </b-input-group>
                    </b-form-group>
                    <b-form-group label="Raça" label-for="inputDescription">
                      <b-form-textarea
                        v-model="payment.description"
                        id="inputDescription"
                        placeholder="Raça"
                        rows="9"
                        :class="{
                          'is-invalid': submitted && $v.payment.description.$error,
                        }"
                      ></b-form-textarea>
                      <div
                        v-if="submitted && $v.payment.description.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.payment.description.required"
                          >Raça é obrigatório.</span
                        >
                        <span v-if="$v.payment.description.required && !$v.payment.description.minLength"
                          >Raça tem que ter no mínimo 2 caracteres.</span
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
    </div>
  </div>
</template>

<script>
import { required, minValue, minLength, requiredIf } from "vuelidate/lib/validators";
import PlgPaymentsApi from "../../apis/PlgPaymentsApi.vue";
import PlgUsersApi from "../../apis/PlgUsersApi.vue";
import Toasts from "../../components/Toasts.vue";
import customValidators from "../../plugins/vuelidateValidators";
import moment from 'moment';


export default {
  name: "PlgPaymentForm",
  components: { 
    Toasts,
    PlgUsersApi,
  },
  mixins: [PlgPaymentsApi],
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    const minDate = new Date(today);
    minDate.setMonth(minDate.getMonth());
    minDate.setDate(now.getDate());
    let formattedMinDate = moment(minDate, "YYYY-MM-DD").toISOString().split('T')[0]
    return {
      minDate: formattedMinDate,
      isLoading: false,
      payment: {
        receiver_federal_id: null,
        amount: 0,
        scheduled_date: null,
        description: null,
      },
      scheduledDateFromDatePicker: null,
      items: [],
      paymentId: null,
      formTitle: "",
      submitted: false,
      money: {
        decimal: ',',
        thousands: '.',
        prefix: 'R$ ',
        precision: 2,
        masked: false,
      }
    };
  },
  validations() {
      return {
        payment: {
          receiver_federal_id: {
            required: requiredIf(function () {
              return !this.paymentId;
            }),
            cpfValidCheck: customValidators.cpfValidCheck(),
          },
          amount: {
            required,
            minValue: minValue(0.001)
          },
          scheduled_date: {
            required,
          },
          description: {
            required,
            minlength: minLength(10)
          },
        }
      }
  },
  methods: {
    async searchReceiversByFederalId() {
      if (this.payment.receiver_federal_id.length > 2) {
        const payload = {
          filter: {federal_id: this.payment.receiver_federal_id}
        }
        let response = await this.$refs.PlgUsersApi.getUsersApi(payload);
        this.items = response.data.users;
        this.rows = response.data.users_count;
      }
    },
    getFederalIdFromResult(result) {
      this.payment.receiver_federal_id = result;
      this.items = [];
    },
    goToFinds() {
      this.$router.push({ name: "payments_table" }).catch();
    },
    async loadPayment() {
      this.paymentId = this.$route.params.id;
      if (this.paymentId) {
        let response = await this.getPaymentApi(this.paymentId);
        if (response.data.status) {
          this.$refs.Toasts.showToast(
            response.data.status,
            response.data.message
          );
          this.goToFinds()
        } else {
          this.payment = response.data.payments[0];
          this.payment.amount /= 100;
          this.payment.scheduled_date = moment(this.payment.scheduled_date).format("DD/MM/YYYY");
        }
      }
    },
    formatDateFromDatePicker() {
      this.payment.scheduled_date = moment(this.scheduledDateFromDatePicker).format("DD/MM/YYYY");
    },
    async sendPaymentDataApi() {
      this.submitted = true;
      this.$v.$touch();
      if (!this.$v.$invalid) {
        const payload = {
          new_payment_data: {
            receiver_federal_id: this.payment.receiver_federal_id,
            amount: this.payment.amount * 100,
            scheduled_date: moment(this.payment.scheduled_date, "DD/MM/YYYY").format("YYYY-MM-DD"),
            description: this.payment.description,
          },
        };
        this.isLoading = true;
        const response = this.paymentId ? await this.updatePaymentApi(this.paymentId, payload) : await this.createPaymentApi(payload);
        this.isLoading = false;
        if (response.data.status === "success") {
          this.goToFinds()
        }
        this.$refs.Toasts.showToast(
          response.data.status,
          response.data.message
        );
      }
    },
  },
  async mounted() {
    if(this.$route.params.id) await this.loadPayment();
    this.formTitle = this.$route.params.id ? `Editar pagamento para ${this.payment.receiver_name}` : "Criar Pagamento"
    if(!this.$can('view', 'apis')) {
      this.$router.push({name: 'home'})
    }
  },
};
</script>

<style>
  .autocomplete {
    position: absolute;
  }
  .autocomplete-results {
    padding: 0;
    background-color: #fff;
    margin: 0;
    border: 1px solid #eee;
  }
  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }
  .autocomplete-result:hover {
    background-color: #65C89B;
    color: white;
  }
</style>
-->