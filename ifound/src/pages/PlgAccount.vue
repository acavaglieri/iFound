<template>
  <div class="order-page">
    <div class="row">
      <div class="col-md-12 grid-margin">
        <div class="row">
          <div class="col-8">
            <h4 class="font-weight-bold">

              <b-button v-if="crud=='read' || crud=='update'" class="btn btn-rounded text-white btn-fw btn-sm btn-block" 
                :variant=retornoVariantDeArquivado() 
                disabled=""
              >
                Conta {{items[0].nome}} ({{ $route.params.id }}) {{crud}}
              </b-button>
              <b-button v-if="crud=='create'" class="btn btn-rounded text-white btn-fw btn-sm btn-block" 
                variant="danger" 
                disabled=""
              >
                Nova Conta {{crud}}
              </b-button>

            </h4>
          </div>
          <div class="col-4 text-right">
            <router-link v-if="crud=='read'" class="btn btn-warning btn-sm mr-2 btn-fw"  v-b-tooltip.html.bottom title="Editar"
              :to="'/site/accounts/'
              + $route.params.id + '/edit'"
              v-on:click="setCrud('update')"><i class="fa fa-edit"/>
            </router-link>
            <!-- <router-link class="btn btn-danger btn-sm mr-2 btn-fw" to="/site/accounts/" v-b-tooltip.html.bottom title="Voltar"><i class="fa fa-angle-up"/></router-link> -->
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-xl-12 grid-margin">
         <plg-account-details :items_account = items :crud = crud></plg-account-details>
      </div>

      <div v-if="crud=='read'" class="col-xl-12 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">

            <div class="container-fluid">
              <div class="row">
                <div class="col-12 text-center">
                  <span>
                    <h4 class="card-title">
                      <span class="pull-left">
                        Endereços Cadastrados
                      </span>
                      <span class="pull-right mb-3">
                        <b-btn class="btn btn-success btn-rounded btn-icon btn-sm"  v-b-tooltip.html.left title="Novo">
                          <i class="fa fa-plus text-white"></i>
                        </b-btn>
                      </span>
                    </h4>
                  </span>
                </div>
              </div>
              <div class="row">
                <div class="col-12">
                  <plg-account-addresses-table></plg-account-addresses-table>
                </div>
              </div>
            </div>
            
          </div>
        </div>
      </div>

      <div v-if="crud=='read'" class="col-xl-12 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">

            <div class="container-fluid">
              <div class="row">
                <div class="col-12 text-center">
                  <span>
                    <h4 class="card-title">
                      <span class="pull-left">
                        Usuários da Conta
                      </span>
                      <span class="pull-right mb-3">
                        <b-btn class="btn btn-success btn-rounded btn-icon btn-sm"  v-b-tooltip.html.left title="Novo">
                          <i class="fa fa-plus text-white"></i>
                        </b-btn>
                      </span>
                    </h4>
                  </span>
                </div>
              </div>
              <div class="row">
                <div class="col-12">
                  <plg-users-table></plg-users-table>
                </div>
              </div>
            </div>
            
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>



const meus_items=
[
  {
    IdDaConta: -8,
    arquivado: false,
    tipo: "Cliente",
    nome: "JOSEFINA",
    email: "teste",
    telefone: "teste",
    celular: "teste",
    PJ: true,
    CpfCnpj: "999",
    logradouro: "teste",
    numero: "teste",
    bairro: "teste",
    cidade: "teste",
    cep: "teste",
    estado: "teste",
    pais: "teste",
    referencia: "teste",
    InformacaoAdicional: "teste",
    latitude: "teste",
    longitude: "teste",
    banco: "teste",
    agencia: "9999",
    agenciaDigito: "9",
    conta: "999999999",
    contaDigito: "9",
    criadoEm: "2020-06-14 17:42:45 -0300",
    alteradoEm: "2020-06-14 17:42:45 -0300",
    enviaOcorrênciasParaIntelipost: '',
    logisticProvider: "",
    logisticProviderID: "",
    logisticProviderFederalTaxID: "",
    shipper: "",
    shipperFederalTaxID: "",
    logisticProviderApiKeyPRD: "",
    logisticProviderApiKeyHML: "",
    plataformaIntelipost: "",
  },
];

import PlgAccountDetails from '../components/accounts/PlgAccountDetails.vue';
import PlgAccountAddressesTable from '../components/accounts/PlgAccountAddressesTable.vue';
import PlgUsersTable from '../components/users/PlgUsersTable.vue';

export default {

  name: 'plg-account',

  components: {
    PlgAccountDetails,
    PlgAccountAddressesTable,
    PlgUsersTable,
  },

  data() {
    return {
      items: meus_items,
      crud: 'read',
    }
  },

  computed: {

    rows() {
      return this.items.length;
    },

  },

  methods: {

    setup(){
      this.items[0].ocorrencia = this.$route.params.id;
    },

    setCrud(value){
      this.crud=value;
    },

    isNewOrEdit(url){
      if (url.indexOf('new') >= 0) {this.setCrud('create')}
      if (url.indexOf('edit')>= 0) {this.setCrud('update')}
    },

    retornoVariantDeArquivado() {
      if(this.items[0].arquivado){
        return "warning";
      } else {
        return "success";
      }
    },

  },

  created() {

    this.setup();
    this.isNewOrEdit(this.$route.path);

  },
}
</script>