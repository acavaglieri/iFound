<!--<template>
  <div></div>
</template>

<script>
import axios from "axios";
import { authHeader } from "./authHeader"

export default {
  name: "PlgUsersApi",
  methods: {
    formatError(error) {
      error = { data: { message: error.response.data.detail, status: "error" } };
      return error;
    },
    getFilterForPaymentsApi() {
      let filter = {
        id: null,
        skip: 0,
        limit: 0,
        order: true,
        sort: null,
        scheduled_date: null,
        amount: null,
        receiverFederalId: null,
      }
      return filter;
    },
    async getPaymentsApi(filter) {
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/payments/list`,
          filter, authHeader()
        );
        if (response != null) return response;
      } catch (error) {
        return this.formatError(error);
      }
    },
    async getPaymentApi(id) {
      let response = null;
      let filter = this.getFilterForPaymentsApi();
      filter.id = id;
      const payload = {
        filter: filter
      }
      try {
        response = await this.getPaymentsApi(payload);
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async createPaymentApi(payload) {
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/payments/create`,
          payload, authHeader()
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response
    },
    async updatePaymentApi(paymentId, payload) {
      let response = null;
      try {
        response = await axios.put(
          `${process.env.VUE_APP_API_URL}/payments/update/${paymentId}`,
          payload, authHeader()
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response
    },
    async payPaymentApi(paymentId, payload) {
      let response = null;
      try {
        response = await axios.put(
          `${process.env.VUE_APP_API_URL}/payments/${process.env.VUE_APP_BANK_API}/pay/${paymentId}`,
          payload, authHeader()
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response
    },
    async payScheduledPayments() {
      let response = null;
      try {
        response = await axios.get(
          `${process.env.VUE_APP_API_URL}/payments/pay/scheduled`,
          authHeader()
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response
    },
  }
}
</script>