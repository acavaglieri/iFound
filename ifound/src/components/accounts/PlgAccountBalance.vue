<!--<template>
  <div>
    <h5 class="text-muted">Saldo</h5>
    <h4
        class="d-flex mb-0 font-weight-bold"
    >
      <span v-if="showBalance && !loading">R$ {{ balance }}</span>
      <b-skeleton v-else-if="loading" width="100%"></b-skeleton>
      <h3 v-else-if="!showBalance">
        <i class="mdi mdi-eye-off text-muted"></i>
      </h3>
    </h4>
  </div>
</template>
-->

<script>
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";

export default {
  data() {
    return {
      balance: 0,
      loading: null,
    }
  },
  props: {
    showBalance: {
      type: Boolean,
      default: true,
    },
    isDefaultWorkspace: {
      type: Boolean,
      default: false,
    }
  },
  mixins: [PlgBankServicesApi],
  methods: {
    async getAccountBalance() {
      this.loading = true;
      const response = this.isDefaultWorkspace ? await this.seeDefaultWorkspaceBalance() : await this.seeAccountBalance();
      this.balance = response.data.balance / 100;
      this.balance = this.balance.toLocaleString('pt-BR', {minimumFractionDigits: 2});
      this.loading = false;
    },
  },
  async mounted() {
    await this.getAccountBalance();
  }
}
</script>