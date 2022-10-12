<!--<template>
  <div>
    <PlgBankServicesApi ref="PlgBankServicesApi"></PlgBankServicesApi>
    <section>
      <div class="row">
        <div class="col-12">
          <div class="card border rounded">
            <div class="card-body">
              <b-row>
                <b-col lg="11">
                  <h3 class="my-3 mx-3 text-center">Transação {{ transactionId }}</h3>
                </b-col>
                <b-col lg="1" class="py-3 d-none d-md-block">
                  <router-link :to="{ name: 'animais' }" style="color: black">
                    <h3><i class="mdi mdi-arrow-left"></i></h3>
                  </router-link>
                </b-col>
              </b-row>
              <hr />
              <b-row>
                <b-col>
                  <div class="text-center">
                    <h4>Quantia: R${{ newAmount }}</h4>
                  </div>
                </b-col>
              </b-row>
              <hr>
              <b-row align-v="center">
                <b-col cols="6" class="border-right">
                  <div v-if="this.amount > 0" class="text-center">
                    <h4>Enviado por:</h4>
                    <span>{{ senderId }}</span>
                  </div>
                  <div v-else class="text-center">
                    <h4>Enviado para:</h4>
                    <span>{{ receiverId }}</span>
                  </div>
                  <div class="text-center my-3">
                    <h4>Data:</h4>
                    <span>{{ date }}</span>
                  </div>
                </b-col>
                <b-col cols="6">
                  <div class="text-center">
                    <h4>Taxa:</h4>
                    <span>R${{ fee }}</span>
                  </div>
                  <div class="text-center my-3">
                    <h4>Descrição:</h4>
                    <span>{{ description }}</span>
                  </div>
                </b-col>
              </b-row>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";
import moment from "moment";

export default {
  name: "PlgBankStatementInfo",
  data() {
    return {
      transactionId: null,
      amount: null,
      newAmount: null,
      receiverId: null,
      senderId: null,
      date: null,
      fee: null,
      description: null,
    };
  },
  components: {
    PlgBankServicesApi,
  },
  methods: {
    async getTransactionInfo() {
      this.transactionId = this.$route.params.id;
      const payload = {
        id: this.$route.params.id,
        account_type: this.$route.params.account_type
      };
      let response = await this.$refs.PlgBankServicesApi.getSingleTransaction(
        payload
      );
      this.amount = response.data.amount / 100;
      if (this.amount > 0) {
        this.newAmount = this.amount
        this.senderId = response.data.sender_id;
      } else {
        this.newAmount = this.amount * -1;
        this.receiverId = response.data.receiver_id;
      }
      this.date = moment(response.data.created).format("DD/MM/YYYY");
      this.fee = response.data.fee / 100;
      this.description = response.data.description;
    },
  },
  async mounted() {
    if (this.$route.params.id) {
      this.getTransactionInfo();
    }
  },
};
</script>