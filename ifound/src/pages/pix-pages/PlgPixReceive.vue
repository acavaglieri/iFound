<template>
  <div>
    <PlgBankServicesApi ref="PlgBankServicesApi"></PlgBankServicesApi>
    <Toasts ref="Toasts"></Toasts>
    <section v-show="!generated">
      <div class="row">
        <div class="col-12">
          <div class="card border rounded">
            <div class="card-body">
              <b-row>
                <b-col lg="11">
                  <h3 class="my-3 mx-3 text-center">Gerar QR Code</h3>
                </b-col>
                <b-col lg="1" class="py-3 d-none d-lg-block">
                  <router-link :to="{ name: 'home' }" style="color: black;">
                    <h3><i class="mdi mdi-arrow-left"></i></h3>
                  </router-link>
                </b-col>
              </b-row>
              <hr>
            </div>
            <div class="row">
              <div class="col-12">
                <form @submit.prevent="generateChargeInfo">
                  <div class="container-fluid">
                    <b-form-group class="mx-3" label="Quanto você quer receber?" label-for="chargeAmount">
                      <money
                        v-model="chargeForm.amount"
                        id="chargeAmount"
                        v-bind="money"
                        maxlength="10"
                        class="form-control form-control-sm"
                        :class="{
                          'is-invalid': submitted && $v.chargeForm.amount.$error,
                        }"
                      ></money>
                      <div
                        v-if="submitted && $v.chargeForm.amount.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.chargeForm.amount.required || !$v.chargeForm.amount.minValue"
                          >Campo obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <div class="text-right mx-3 my-3">
                      <b-row align-h="end">
                        <b-col sm="1" md="2">
                          <b-button v-show="!isLoading" type="submit" block class="rounded" variant="primary" size="md">
                            <i class="fa fa-check"></i>
                          </b-button>
                          <b-button v-show="isLoading" class="rounded" block disabled variant="primary">
                            <b-spinner small></b-spinner>
                          </b-button>
                        </b-col>
                      </b-row>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <plg-pix-charge-info v-show="generated" 
      :amount="formattedAmount"
      :brCode="generatedChargeInfo.brCode">
    </plg-pix-charge-info>
  </div>
</template>

<script>
import { required, minValue } from "vuelidate/lib/validators";
import PlgBankServicesApi from '../../apis/PlgBankServicesApi.vue'; 
import Toasts from '../../components/Toasts.vue';
import PlgPixChargeInfo from './PlgPixChargeInfo.vue';


export default {
  data() {
    return {
      chargeForm: {
        amount: 0
      },
      formattedAmount: null,
      toDefaultWorkspace: null,
      submitted: false,
      isLoading: false,
      generatedChargeInfo: {
        brCode: null,
      },
      generated: false,
      money: {
        decimal: ',',
        thousands: '.',
        prefix: 'R$ ',
        precision: 2,
        masked: false,
      }
    }
  },
  validations() {
    return {
      chargeForm: {
        amount: {
          required,
          minValue: minValue(0.001)
        }
      }
    }
  },
  components: {
    PlgBankServicesApi,
    Toasts,
    PlgPixChargeInfo,
  },
  methods: {
    async generateChargeInfo() {
      this.toDefaultWorkspace = this.$route.params.toDefaultWorkspace
      if(this.toDefaultWorkspace && this.chargeForm.amount) this.chargeForm.amount += 0.5
      this.submitted = true
      this.$v.$touch();
      if(!this.$v.$invalid) {
        const payload = {
          charge_data: {
            amount: this.chargeForm.amount,
            to_default_workspace: this.toDefaultWorkspace
          }
        }
        this.isLoading = true;
        let response = await this.$refs.PlgBankServicesApi.generateChargeInfo(payload);
        this.generated = true;
        this.isLoading = false;
        this.generatedChargeInfo.brCode = response.data.br_code
        this.formattedAmount = this.chargeForm.amount.toLocaleString('pt-BR', {minimumFractionDigits: 2})
        this.$refs.Toasts.showToast(response.data.status, response.data.message);
      }
    },
  },
}
</script>