<template>
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
    getFilterForUsersApi() {
      let filter = {
        status: null,
        message: null,
        id: null,
        name: null,
        email: null,
        cellphone: null,
        birthday_ini: null,
        birthday_end: null,
        is_inactive: false,
        skip: 0,
        limit: 0,
        full_search: null,
        order: true,
        sort: null
      }
      return filter;
    },
    async generateXlsx(filter) {
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/user/xlsx/generate`,
          filter,
          { responseType: "blob" }
        );
        const url = window.URL.createObjectURL(
          new Blob([response.data], { type: "application/excel" })
        );
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "users-list.xlsx");
        document.body.appendChild(link);
        link.click();
      } catch (error) {
        return this.formatError(error);
      }
    },
    async addNewUserAsAdmin(newUserPayload) {
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/user/save/`,
          newUserPayload, authHeader()
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async updateUserApi(userID, userUpdatePayload) {
      let response = null;
      try {
        response = await axios.put(
          `${process.env.VUE_APP_API_URL}/user/update/${userID}`,
          userUpdatePayload, authHeader()
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async deleteUserApi(id) {
      let response = null;
      try {
        response = await axios.delete(
          `${process.env.VUE_APP_API_URL}/user/delete/${id}`, authHeader()
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async confirmUser(token) {
      let response = null;
      try {
        response = await axios.post(`${process.env.VUE_APP_API_URL}/user/confirm/`, token);
      }catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async getUserApi(id) {
      let response = null;
      let filter = this.getFilterForUsersApi();
      filter.id = id;
      const payload = {
        filter: filter
      }
      try {
        response = await this.getUsersApi(payload);
        if (response != null) return response.data.users[0];
      } catch (error) {
        return this.formatError(error);
      }
    },
    async getCurrentUser() {
      let response = null;
      try {
        response = await axios.get(`${process.env.VUE_APP_API_URL}/user/me`, authHeader());
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async getLoginApi(user) {
      let payload = new FormData();
      payload.append("username", user.email);
      payload.append("password", user.password)
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/user/login`,
          payload
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async getTokenApi(UserTokenPayload) {
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/user/get/token`,
          UserTokenPayload
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async resetPasswordApi(UserResetPassPayload) {
      let response = null;
      try {
        response = await axios.put(
          `${process.env.VUE_APP_API_URL}/user/reset/password`,
          UserResetPassPayload
        );
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async getUserEmailByToken(token) {
      let response = null;
      try {
        response = await axios.get(`${process.env.VUE_APP_API_URL}/user/token/${token}`);
      } catch (error) {
        return this.formatError(error);
      }
      return response;
    },
    async getUsersApi(filter) {
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/users/list`,
          filter, authHeader()
        );
        if (response != null) return response;
      } catch (error) {
        return this.formatError(error);
      }
    },
    async saveUserApi(user) {
      let response = null;
      try {
        response = await axios.post(
          `${process.env.VUE_APP_API_URL}/user/register`,
          user
        );
      } catch (error) {
        console.log(error)
        return this.formatError(error);
      }
      return response;
    },
    setGlobalUser(user) {
      this.$global.user = user;
    },
  },
};
</script>