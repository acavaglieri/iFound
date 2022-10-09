<!--<template>
  <div></div>
</template>

<script>
import axios from "axios";
import { authHeader } from "./authHeader"

export default {
  name: "PlgBankServicesApi",
  methods: {
    formatError(error) {
      error = { data: { message: error.response.data.detail, status: "error" } };
      return error;
    },
    async previewBrCodePayment(payload) {
      let response = null;
      try {
        response = await axios.post(`${process.env.VUE_APP_API_URL}/preview/brcode/${process.env.VUE_APP_BANK_API}`, payload, authHeader());
      }catch(error) {
        return this.formatError(error);
      }
      return response;
    },
    async payByBrCode(payload) {
      let response = null;
      try {
        response = await axios.post(`${process.env.VUE_APP_API_URL}/pay/brcode/${process.env.VUE_APP_BANK_API}`, payload, authHeader());
      }catch(error) {
        return this.formatError(error);
      }
      return response;
    },
    async generateChargeInfo(payload) {
      let response = null;
      try {
        response = await axios.post(`${process.env.VUE_APP_API_URL}/receive/charge/${process.env.VUE_APP_BANK_API}`, payload, authHeader())
      }catch(error) {
        return this.formatError(error);
      }
      return response;
    },
    async seeDefaultWorkspaceBalance() {
      let response = null;
      try {
        response = await axios.get(`${process.env.VUE_APP_API_URL}/see/balance/starkbank/default/workspace`, authHeader())
      }catch(error) {
        return this.formatError(error);
      }
      return response
    },
    async seeDefaultWorkspaceStatement(payload) {
      let response = null;
      try {
        response = await axios.post(`${process.env.VUE_APP_API_URL}/see/bank/statement/starkbank/default/workspace`, payload, authHeader())
      }catch(error) {
        return this.formatError(error);
      }
      return response
    },
    async seeAccountBalance() {
      let response = null;
      try {
        response = await axios.get(`${process.env.VUE_APP_API_URL}/see/balance/${process.env.VUE_APP_BANK_API}`, authHeader())
      }catch(error) {
        return this.formatError(error);
      }
      return response
    },
    async seeAccountStatement(payload) {
      let response = null;
      try {
        response = await axios.post(`${process.env.VUE_APP_API_URL}/see/bank/statement/${process.env.VUE_APP_BANK_API}`, payload, authHeader())
      }catch(error) {
        return this.formatError(error);
      }
      return response
    },
    async getSingleTransaction(payload) {
      let response = null;
      try {
        response = await axios.post(`${process.env.VUE_APP_API_URL}/get/single/transaction/${process.env.VUE_APP_BANK_API}`, payload, authHeader())
      }catch(error) {
        return this.formatError(error);
      }
      return response
    } 
  },
};
</script>