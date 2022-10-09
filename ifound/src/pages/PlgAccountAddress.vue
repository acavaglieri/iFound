<!--<template>
  <div class="order-page">
    <div class="row">
      <div class="col-md-12 grid-margin">
        <div class="row">
          <div class="col-8">
            <h4 class="font-weight-bold">
              <b-button class="btn btn-rounded text-white btn-fw btn-sm btn-block" 
                :variant=retornoVariantDeArquivado() 
                disabled=""
              >
                Conta {{items[0].nome}} ({{ items[0].IdDaConta }}) , Endereço {{items[0].nomeEndereco}} ({{ $route.params.id }})
              </b-button>
            </h4>
          </div>
          <div class="col-4 text-right"> 
            <router-link class="btn btn-warning btn-sm mr-2 btn-fw" to="" v-b-tooltip.html.left title="Novo">*<i class="fa fa-edit"/></router-link>
          -->
            <!-- <router-link class="btn btn-danger btn-sm mr-2 btn-fw" :to="'/site/accounts/' + items[0].IdDaConta" v-b-tooltip.html.left title="Voltar"><i class="fa fa-angle-up"/></router-link> -->
          <!--
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-xl-6 grid-margin stretch-card">
         <plg-account-address-details :items_account = items></plg-account-address-details>
      </div>

      <div class="col-xl-6 grid-margin stretch-card">
        <plg-account-address :items_account = items></plg-account-address>
      </div>

    </div>
  </div>
</template>

<script>



const meus_items=
[
  {
    IdDaConta: -8,
    IdDoEndereco: 122,
    arquivado: false,
    tipo: "Centro de Distribuição",
    nome: "JOSEFINA",
    nomeEndereco: "JOSEFINA LOJA",
    email: "teste",
    telefone: "teste",
    celular: "teste",
    PJ: true,
    CpfCnpj: 999,
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
    criadoEm: "2020-06-14 17:42:46 -0300",
    alteradoEm: "2020-06-14 17:42:45 -0300",
  },
];

import PlgAccountAddressDetails from '../components/accounts/PlgAccountAddressDetails.vue';
import PlgAccountAddress from '../components/accounts/PlgAccountAddress.vue';

export default {

  name: 'plg-account-address',

  components: {
    PlgAccountAddressDetails,
    PlgAccountAddress,
  },

  /* eslint-disable no-console */
  data() {
    return {
      items: meus_items,
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
      // eslint-disable-next-line
      // console.log(this.items[0]);
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

  },
}
</script>