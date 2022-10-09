<!--<template>
  <div>
    <section class="tables">
      <div class="row">
        <div class="col">
          <div class="card">
            <b-table
              :items="items"
              id="table-list"
              responsive
              :per-page="perPage"
              :current-page="currentPage"
              :fields="fields"
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
              small
            >
              <template v-slot:cell(nome)="data"><i v-if="data.item.arquivado" class="fa fa-archive text-danger"/> {{data.value}}</template>
              <template v-slot:cell(PJ)="data">{{data.value | booleanParaSimNao}}</template>
              <template v-slot:cell(acoes)="data">
                <router-link class="btn btn-warning btn-sm mr-2 btn-fw" :to="'/site/accounts/' + data.item.IdDaConta + '/address/'" v-b-tooltip.html.left title="Abrir">
                  <i class="fa fa-search"></i>
                </router-link> -->
                <!-- <router-link class="btn btn-warning btn-sm mr-2 btn-fw" :to="'/site/accounts/' + data.item.IdDaConta + '/address/edit'" v-b-tooltip.html.left title="Editar">
                  * <i class="fa fa-edit"></i>
                </router-link> -->
              <!--
              </template>
            </b-table>
            <div class="row">
              <div class="col">
                <h6 class="col-12">
                  <small class="text-muted ml-2 mr-2">Itens por Página</small>
                  <div class="btn-group" role="group" aria-label="Basic example">
                    <button type="button" class="btn btn-outline-primary btn-sm">10</button>
                    <button type="button" class="btn btn-outline-primary btn-sm">25</button>
                    <button type="button" class="btn btn-outline-primary btn-sm">50</button>
                    <button type="button" class="btn btn-outline-primary btn-sm">100</button>
                  </div>
                </h6>
              </div>
              <div class="col">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="table-list"
                  align="center"
                ></b-pagination>
              </div>
              <div class="col" align="right">
                <b-btn variant="primary" class="btn btn-success btn-rounded btn-icon btn-sm text-white mr-3" v-b-tooltip.html.left title="Exportar para Excel">
                  <i class="fa fa-download"></i>
                </b-btn>
                <span v-if="isCompact == true" align="center"><b-btn variant="info" class="btn btn-success btn-rounded btn-icon btn-sm text-white mr-3" v-on:click=changeIsCompact(false) v-b-tooltip.html.left title="Completo"><i class="fa fa-cubes"></i></b-btn></span>
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

const items= 
[
  {
    IdDaConta: 99,
    tipo: "Centro de Distribuição",
    nome: "JOSEFINA",
    telefone: "teste",
    celular: "teste",
    PJ: true,
    CpfCnpj: "9999999999",
    logradouro: "teste",
    numero: "teste",
    bairro: "teste",
    cidade: "teste",
    cep: "teste",
    estado: "teste",
    referencia: "teste",
    InformacaoAdicional: "teste",
    latitude: "teste",
    longitude: "teste",
  },
  {
    IdDaConta: 102,
    tipo: "Centro de Distribuição",
    nome: "JOSEFINA 2",
    telefone: "teste",
    celular: "teste",
    PJ: false,
    CpfCnpj: "0999999999",
    logradouro: "teste",
    numero: "teste",
    bairro: "teste",
    cidade: "teste",
    cep: "teste",
    estado: "teste",
    referencia: "teste",
    InformacaoAdicional: "teste",
    latitude: "teste",
    longitude: "teste",
  },
];

import Vue from "vue";
import SortedTablePlugin from "vue-sorted-table";

Vue.use(SortedTablePlugin, {
  ascIcon: '<i class="ti-arrow-down"></i>',
  descIcon: '<i class="ti-arrow-up"></i>'
});

export default {

  name: "plg-account-addresses-table",

  components: {
  },

  data: function() {
    return {
      sortBy: "nome",
      perPage: 5,
      currentPage: 1,
      sortDesc: false,
      sortByFormatted: true,
      filterByFormatted: true,
      sortable: true,
      fields: [],
      items: items,

      isCompact: true,
    };
  },

  methods: {

    changeIsCompact(valor){
      if(valor==true){
        this.seeCompact();
      }else{
        this.seeComplete();
      }
      // console.log(this.isCompact);
    },

    seeComplete(){
      this.fields=
      [
        { key: "tipo", label: "Tipo", sortable: true },
        { key: "nome", label: "Nome",  sortable: true },
        { key: "telefone", label: "Telefone",  sortable: true },
        { key: "celular", label: "Celular",  sortable: true },
        { key: "PJ", label: "PJ?",  sortable: true },
        { key: "CpfCnpj", label: "CPF/CNPJ",  sortable: true },
        { key: "logradouro", label: "Logradouro",  sortable: true },
        { key: "numero", label: "Número",  sortable: true },
        { key: "bairro", label: "Bairro",  sortable: true },
        { key: "cidade", label: "Cidade",  sortable: true },
        { key: "cep", label: "CEP",  sortable: true },
        { key: "estado", label: "Estado",  sortable: true },
        { key: "referencia", label: "Referência",  sortable: true },
        { key: "InformacaoAdicional", label: "Informação Adicional",  sortable: true },
        { key: "latitude", label: "Latitude",  sortable: true },
        { key: "longitude", label: "Longitude",  sortable: true },
        { key: "acoes", label: "Ações",  sortable: false }
      ];
      this.isCompact = false;
    },
    
    seeCompact(){
      this.fields=
      [
        { key: "tipo", label: "Tipo", sortable: true },
        { key: "nome", label: "Nome",  sortable: true },
        { key: "telefone", label: "Telefone",  sortable: true },
        { key: "celular", label: "Celular",  sortable: true },
        { key: "logradouro", label: "Logradouro",  sortable: true },
        { key: "numero", label: "Número",  sortable: true },
        { key: "cidade", label: "Cidade",  sortable: true },
        { key: "estado", label: "Estado",  sortable: true },
        { key: "acoes", label: "Ações",  sortable: false }
      ];
      this.isCompact = true;
    },

  },

  filters: {
    booleanParaSimNao(dado) {
      return dado == false ? 'Não': dado == true ? 'Sim': 'notBool';
    },
  },

  mounted() {

    this.changeIsCompact(true);

  },
  

  computed: {
    rows() {
      return this.items.length;
    }
  },

};
</script>
