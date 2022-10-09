<template>
  <section>
    <div class="row">
      <div class="col-md-12 grid-margin">
        <div class="row">
          <div class="col-lg-4 col-md-12 my-auto">
            <b-form-group label="ROTA" label-for="input1">
              <b-form-select :options="routes"
              v-model="route"
              @change="routeselected"/>
            </b-form-group>
          </div>
          <div class="col-lg-4 col-md-12 my-auto">
            <div>
              <b-form-group label="CONTA" label-for="input2">
                <Autocomplete @emite-selected-item-null="valueSelectedItemNull"
                :items="accounts"
                filterby="name"
                title="Selecione a conta"
                @selected="accountselected"/>
              </b-form-group>
            </div>
          </div>
          <div class="col-lg-4 col-md-12 my-auto">
            <button class="btn btn-success text-white btn-sm" v-on:click="createOrAddArrayWithRoutesAndAccounts()" v-b-tooltip.html.bottom title="Adicionar"><i class="fa fa-plus-square"></i></button>
          </div>
          <br><br><br>
        </div>

        <div class="row">
          <div class="col">
            <div v-for="routeAndAccounts in accountsInRoutes" :key="routeAndAccounts.id">
              <ol class="breadcrumb breadcrumb-arrow">
                <button class="btn btn-warning text-white btn-sm"><i class="fa fa-map-marker"></i> {{routeAndAccounts[0].route_id}}</button>
                <li v-for="(routeAndAccount, index) in routeAndAccounts" :key="routeAndAccount.id">
                  <a> {{routeAndAccount.account_name}}</a>
                  <span v-if="index == routeAndAccounts.length -1" class="bg-danger text-white">
                    <button class="btn btn-danger btn-sm" v-on:click="deleteLastAccountOfRoute(routeAndAccount.id, routeAndAccount.route_id)" v-b-tooltip.html.left title="Deletar"><i class="fa fa-window-close"></i></button>
                  </span>
                </li>
              </ol>
            </div>
          </div>
        </div>

        <hr>

        <!--
        <div class="row">
          <div class="col">
            Contas Ajustadas nas Rotas:
            <br>
            <ul>
              <li v-for="accountInRoutes in accountsInRoutes" :key="accountInRoutes.id">
                Rota {{accountInRoutes[0].route_id}}
                <ul>
                  <li v-for="data in accountInRoutes" :key="data.id">
                    Conta {{data.account_id}} {{ data }}
                  </li>
                </ul>
              </li>
            </ul>

            Contas nas Rotas (array):
            <br>
            {{accountsInRoutes}}
            <br>
            Rotas:<br>
            <ul><li v-for="dado in routes" :key="dado.id"> {{ dado }} </li></ul>
            Rota selecionada:<br>{{route}}<br><br>
            Contas:<br>
            <ul><li v-for="dado in accounts" :key="dado.id"> {{ dado }} </li></ul>
            Conta selecionada:<br>{{account}}<br><br>
            Contas nas Rotas:<br>
            <ul><li v-for="dado in accountsInRoutes" :key="dado.id"> {{ dado }} </li></ul>

          </div>

        </div>
        -->

      </div>
    </div>
  </section>
</template>

<script>
/* eslint-disable */
  const routes = [];

  import Autocomplete from '../components/ui/autoComplete'
  import axios from 'axios';

  export default {
    name: 'plg-account-walks',

    components: {
      Autocomplete
    },

    data() {
      return {
        accounts: [],
        account: [],
        routes: [],
        route: '',
        accountsInRoutes: [],

        errorMsg: '',

        showDismissibleAlert: false,
      };
    },

    mounted() {
      axios.get(`${process.env.VUE_APP_API_URL}/accounts`)
        .then(response => (this.accounts = response.data))
        .catch(error => {
          this.$notify({
            title: 'Erro ao atualizar lista de contas.',
            text: error,
            type: 'error'
          });
        })

      this.refreshAccountsInRoutes();
      this.refreshRoutes();
    },

    methods: {

      createOrAddArrayWithRoutesAndAccounts(){
        if (this.account=='') {
          this.$notify({
            title: 'Selecione uma conta.',
            type: 'warn'
          });
        } else {
          this.createNewRoute();
        }
      },

      accountselected(account) {
        this.account = account;
      },

      routeselected(route) {
        this.route = route;
      },

      valueSelectedItemNull(payload){
        if(payload==null){
          this.account = [];
        }
      },

      refreshRoutes() {
        axios.get(`${process.env.VUE_APP_API_URL}/account_walks/only_routes`)
          .then(response => {
              this.routes = response.data;
              this.routes.unshift('Nova');
              this.route = 'Nova';
            })
          .catch(error => {
            this.$notify({
              title: 'Erro ao atualizar lista de rotas.',
              text: error,
              type: 'error'
            });
          })
      },

      refreshAccountsInRoutes() {
        axios.get(`${process.env.VUE_APP_API_URL}/account_walks/by_arrays`)
          .then(response => (this.accountsInRoutes = response.data))
          .catch(error => {
            this.$notify({
              title: 'Erro ao atualizar rotas.',
              text: error,
              type: 'error'
            });
          })
      },

      createRealRoutesWithoutNova(){
        var realRoutes = this.routes.slice();
        realRoutes.splice(realRoutes.indexOf('Nova'),1);
        return realRoutes;
      },

      createNewRoute(){
        this.errorMsg = '';
        this.showDismissibleAlert=false;

        var jsonData = {"account_id": this.account.id
                       };
        if (this.route != "Nova") jsonData.route_id = this.route;

        axios({
          method: 'post',
          url: `${process.env.VUE_APP_API_URL}/account_walks/add`,
          data: {jsonData: jsonData}
        })
        .then(
          (response) => {
            this.refreshRoutes();
            this.refreshAccountsInRoutes();
          }, 
          (error) => {
            this.$notify({
              title: 'Erro ao salvar rota.',
              text: error,
              type: 'error'
            });
          });
      },

      deleteLastAccountOfRoute(id_ext, route_id_ext){
        axios.delete(`${process.env.VUE_APP_API_URL}/account_walks/delete?id=${id_ext}`)
          .then(response => {
            this.refreshRoutes();
            this.refreshAccountsInRoutes();
          })
          .catch(error => {
            this.$notify({
              title: 'Erro ao salvar rota.',
              text: error,
              type: 'error'
            });
          });
      },

    },

  }
</script>