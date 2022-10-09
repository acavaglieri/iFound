<template>
  <div>
    <PlgBankServicesApi ref="PlgBankServicesApi"></PlgBankServicesApi>
    <Toasts ref="Toasts"></Toasts>
    <section>
      <div class="row">
        <div class="col-12">
          <div class="card border rounded">
            <div class="card-body" v-if="!isLoadingPreview && !invalidBrCode">
              <b-row>
                <b-col lg="11">
                  <h3 class="my-3 mx-3 text-center">Pagar com QRCode</h3>
                </b-col>
                <b-col lg="1" class="py-3 d-none d-md-block">
                  <router-link :to="{ name: 'home' }" style="color: black">
                    <h3><i class="mdi mdi-arrow-left"></i></h3>
                  </router-link>
                </b-col>
              </b-row>
              <hr />
              <b-row>
                <b-col cols="6" class="pr-0">
                  <div>
                    <h4>Quantia:</h4>
                  </div>
                </b-col>
                <b-col>
                  <div class="text-right">
                    <h4>R${{ paymentInfo.amount }}</h4>
                  </div>
                </b-col>
              </b-row>
              <hr>
              <b-row>
                <b-col cols="6" class="pr-0">
                  <div>
                    <h4>Para:</h4>
                  </div>
                </b-col>
                <b-col>
                  <div class="text-right">
                    <h4>{{ paymentInfo.name }}</h4>
                  </div>
                </b-col>
              </b-row>
              <hr>
              <b-row>
                <b-col cols="6" class="pr-0">
                  <div>
                    <h4>CPF:</h4>
                  </div>
                </b-col>
                <b-col>
                  <div class="text-right">
                    <h4>{{ paymentInfo.federalId }}</h4>
                  </div>
                </b-col>
              </b-row>
              <hr>
              <b-row>
                <b-col cols="6" class="pr-0">
                  <div>
                    <h4>Código da Transação:</h4>
                  </div>
                </b-col>
                <b-col>
                  <div class="text-right">
                    <input v-model="paymentInfo.code" readonly class="form-control-plaintext" />
                  </div>
                </b-col>
              </b-row>
              <hr>
              <b-row>
                <b-col cols="6" class="pr-0">
                  <div>
                    <h4>Conta:</h4>
                  </div>
                </b-col>
                <b-col>
                  <div class="text-right">
                    <h4>{{ paymentInfo.accountNumber }}</h4>
                  </div>
                </b-col>
              </b-row>
              <hr>
              <b-row>
                <b-col cols="6" class="pr-0">
                  <div>
                    <h4>Agência:</h4>
                  </div>
                </b-col>
                <b-col>
                  <div class="text-right">
                    <h4>{{ paymentInfo.branch }}</h4>
                  </div>
                </b-col>
              </b-row>
              <hr>
              <div class="text-right mx-3 my-3">
                <b-row align-h="end">
                  <b-col sm="12" lg="4">
                    <b-button
                      v-show="!isLoading"
                      @click="payByBrCode"
                      block
                      class="rounded"
                      variant="primary"
                      size="md"
                    >
                      Pagar
                    </b-button>
                    <b-button
                      v-show="isLoading"
                      class="rounded"
                      block
                      disabled
                      variant="primary"
                    >
                      <b-spinner small></b-spinner>
                    </b-button>
                  </b-col>
                </b-row>
              </div>
            </div>
            <div v-if="!isLoadingPreview && invalidBrCode">
              <div class="card border-0 my-5" style="text-align: center">
                <i class="mdi mdi-alert-circle-outline text-muted" style="font-size: 50px"></i>
                <h3 class="text-muted">Não encontramos sua transação!</h3>
                <h4 class="text-muted">Por favor, verifique seu código.</h4>
              </div>
            </div>
            <div v-if="isLoadingPreview">
              <div class="card-body text-center mt-5">
                <h4><b-spinner></b-spinner></h4>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";
import Toasts from "../../components/Toasts.vue";

export default {
  name: "PlgPixChargeInfo",
  data() {
    return {
      paymentInfo: {
        amount: null,
        name: null,
        federalId: null,
        accountNumber: null,
        branch: null,
        code: null,
      },
      invalidBrCode: null,
      isLoading: false,
      isLoadingPreview: false,
    };
  },
  components: {
    PlgBankServicesApi,
    Toasts,
  },
  methods: {
    async getPreviewBrCodePayment(brCode) {
      this.isLoadingPreview = true;
      const payload = {
        preview_data: {
          br_code: brCode,
        },
      };
      let response = await this.$refs.PlgBankServicesApi.previewBrCodePayment(
        payload
      );
      if(!response.data.account_number) {
        this.invalidBrCode = true;
        this.isLoadingPreview = false;
      } else {
        this.paymentInfo.code = this.$route.params.brCode;
        this.paymentInfo.amount = (response.data.amount / 100).toLocaleString('pt-BR', {minimumFractionDigits: 2});
        this.paymentInfo.name = response.data.name;
        this.paymentInfo.federalId = response.data.federal_id;
        this.paymentInfo.accountNumber = response.data.account_number;
        this.paymentInfo.branch = response.data.branch_code;
        this.isLoadingPreview = false;
      }
    },
    async payByBrCode() {
      const payload = {
        payment_data: {
          br_code: this.paymentInfo.code,
          federal_id: this.paymentInfo.federalId,
        },
      };
      this.isLoading = true;
      let response = await this.$refs.PlgBankServicesApi.payByBrCode(payload);
      this.isLoading = false;
      this.$refs.Toasts.showToast(response.data.status, response.data.message);
    },
  },
  async mounted() {
    if (this.$route.params.brCode) {
      await this.getPreviewBrCodePayment(this.$route.params.brCode);
    }
  },
};
</script>

<style scoped>
.border-line {
  border-bottom: lightgray;
}
</style>