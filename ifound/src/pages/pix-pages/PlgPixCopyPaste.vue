<!-- <template>
  <div>
    <PlgBankServicesApi ref="PlgBankServicesApi"></PlgBankServicesApi>
    <Toasts ref="Toasts"></Toasts>
    <section>
      <div class="row">
        <div class="col-12">
          <div class="card border rounded">
            <div class="card-body">
              <b-row>
                <b-col lg="11">
                  <h3 class="my-3 mx-3 text-center">PIX Copia e Cola</h3>
                </b-col>
                <b-col lg="1" class="py-3 d-none d-lg-block">
                  <router-link :to="{ name: 'home' }" style="color: black">
                    <h3><i class="mdi mdi-arrow-left"></i></h3>
                  </router-link>
                </b-col>
              </b-row>
              <hr />
            </div>
            <div class="row">
              <div class="col-12">
                <form @submit.prevent="payByBrCode">
                  <div class="container-fluid">
                    <b-form-group
                      class="mx-3"
                      label="Código PIX:"
                      label-for="pixBrcode"
                    >
                      <b-form-input
                        v-model="paymentForm.brCode"
                        type="text"
                        id="pixBrcode"
                        size="sm"
                        placeholder="Cole o código da transação aqui"
                        :class="{
                          'is-invalid':
                            submitted && $v.paymentForm.brCode.$error,
                        }"
                      ></b-form-input>
                      <div
                        v-if="submitted && $v.paymentForm.brCode.$error"
                        class="invalid-feedback"
                      >
                        <span v-if="!$v.paymentForm.brCode.required"
                          >Campo obrigatório.</span
                        >
                      </div>
                    </b-form-group>
                    <div class="text-right mx-3 my-3">
                      <b-row align-h="end">
                        <b-col sm="1" md="2">
                          <b-button
                            v-show="!isLoading"
                            type="submit"
                            block
                            class="rounded"
                            variant="primary"
                            size="md"
                          >
                            <i class="fa fa-check"></i>
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
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { required } from "vuelidate/lib/validators";
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";
import Toasts from "../../components/Toasts.vue";

export default {
  data() {
    return {
      paymentForm: {
        brCode: null,
        description: null,
      },
      submitted: false,
      isLoading: false,
    };
  },
  validations: {
    paymentForm: {
      brCode: {
        required,
      },
    },
  },
  components: {
    PlgBankServicesApi,
    Toasts,
  },
  methods: {
    async payByBrCode() {
      this.$router.push({name: 'preview_pet', params: {brCode: this.paymentForm.brCode}})
    },
  },
};
</script>
-->