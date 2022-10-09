<template>
  <div>
    <section class="tables">
      <div class="row">
        <div class="col">
          <div class="card">
            <!-- {{rows}}<br>{{items}} -->
            <b-table
              :items="items"
              id="table-list"
              responsive
              :fields="fields"
              @sort-changed="sortChanged"
              small
            >
              <template v-slot:cell(name)="data"><i v-if="data.item.is_inactive" class="fa fa-archive text-danger"/> {{data.value}}</template>
              <template v-slot:cell(acoes)="data">
                <router-link class="btn btn-warning btn-sm mr-2 btn-fw" :to="'/site/accounts/' + data.item.IdDaConta" v-b-tooltip.html.left title="Abrir">
                  <i class="fa fa-search"></i>
                </router-link>
              </template>
            </b-table>
            <div class="row">
              <div class="col" align="left">
                <div class="btn-group ml-3" role="group" aria-label="items-per-page">
                  <b-button variant="outline-primary" size="sm" v-b-tooltip.html.top title="Items por Página" @click="changePerPage(25)">25</b-button>
                  <b-button variant="outline-primary" size="sm" v-b-tooltip.html.top title="Items por Página" @click="changePerPage(50)">50</b-button>
                  <b-button variant="outline-primary" size="sm" v-b-tooltip.html.top title="Items por Página" @click="changePerPage(100)">100</b-button>
                  <b-button variant="outline-primary" size="sm" v-b-tooltip.html.top title="Items por Página" @click="changePerPage(200)">200</b-button>
                </div>
              </div>
              <div class="col">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="table-list"
                  align="center"
                  @input="refreshLastPage();"
                ></b-pagination>
              </div>
              <div class="col" align="right">
                <b-btn variant="primary" class="btn btn-success btn-rounded btn-icon btn-sm text-white mr-3" v-b-tooltip.html.left title="Exportar para Excel">
                  <i class="fa fa-download"></i>
                </b-btn>
                <span v-if="isCompact == true" align="center"><b-btn variant="info"  class="btn btn-success btn-rounded btn-icon btn-sm text-white mr-3" v-on:click=changeIsCompact(false) v-b-tooltip.html.left title="Completo"><i class="fa fa-cubes"></i></b-btn></span>
                <span v-if="isCompact == false" align="center"><b-btn variant="success" class="btn btn-success btn-rounded btn-icon btn-sm mr-3" v-on:click=changeIsCompact(true) v-b-tooltip.html.left title="Resumido"><i class="fa fa-cube"></i></b-btn></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>

import axios from 'axios';

export default {

  name: "plg-accounts-table",

  data: function() {
    return {
      search: null,
      search_kind: null,

      sortBy: "id",
      perPage: 25,
      lastPage: 1,
      currentPage: 1,
      fields: [],
      items: [],
      rows: 0,
      isCompact: true,
    };
  },

  methods: {
    sortChanged(e) {
      this.sortBy = e.sortBy;
      if (e.sortDesc)
        this.sortBy = e.sortBy+" desc";
      this.refreshAccounts();
    },

    changePerPage(perPage) {
      this.perPage = perPage;
      this.refreshAccounts();
    },

    refreshLastPage() {
      if (this.currentPage != this.lastPage) {
        this.lastPage = this.currentPage;
        console.log(this.lastPage);
        this.refreshAccounts();
      }
    },

    refreshAccounts() {
      axios.get(`${process.env.VUE_APP_API_URL}/accounts/crud`, {
        params: {
          page: this.lastPage,
          itens_per_page: this.perPage,
          sort_by: this.sortBy,
          search: this.search,
          search_kind: this.search_kind
        }
      })
        .then(response => {
          this.items = response.data.accounts;
          this.rows = response.data.accounts_count;
        })
        .catch(error => {
          this.$notify({
            title: 'Erro ao atualizar.',
            text: error,
            type: 'error'
          });
          console.log(error.response);
        })
    },

    changeIsCompact(valor){
      if(valor==true){
        this.seeCompact();
      }else{
        this.seeComplete();
      }
    },

    seeComplete(){
      this.fields=
      [
        { key: "kind", label: "Tipo", sortable: true},
        { key: "name", label: "Nome",  sortable: true},
        { key: "phone", label: "Telefone",  sortable: true},
        { key: "email", label: "Email",  sortable: true},
        { key: "cellphone", label: "Celular",  sortable: true},
      ];
      this.isCompact = false;
    },
    
    seeCompact(){
      this.fields=
      [
        { key: "kind", label: "Tipo", sortable: true},
        { key: "name", label: "Nome",  sortable: true},
        { key: "phone", label: "Telefone",  sortable: true},
        { key: "email", label: "Email",  sortable: true},
      ];
      this.isCompact = true;
    },

  },

  mounted() {
    this.changeIsCompact(true);
    this.refreshAccounts();
  },

};
</script>
