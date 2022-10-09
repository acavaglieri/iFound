<template>
  <div id="secure">
    <h1>Secure Area</h1>
    <p>
      This is a secure area
      <router-link to="/login" v-on:click.native="logout()" replace>Logout</router-link>
      <button class="btn btn-block btn-primary btn-lg font-weight-medium auth-form-btn" @click.prevent.stop="logout()">Logout</button>
    </p>
  </div>
</template>

<script>
  export default {
    name: 'Secure',
    data() {
      return {};
    },
    methods: {
      logout() {
        this.$emit("authenticated", false);
        this.$router.replace({ name: "login" });
      },  
    }
  }
</script>

<style scoped>
  #secure {
    background-color: #FFFFFF;
    border: 1px solid #CCCCCC;
    padding: 20px;
    margin-top: 10px;
  }
</style>