<!--<template>
  <div class="card">
    <div class="card-body">

      <div class="container-fluid">
        <div class="row">
          <div class="col-12 text-center">
            <span>
              <h4 class="card-title">
                <span class="pull-left">
                  Serviços
                </span>
                <span class="pull-right mb-3">
                  <b-btn v-if="crud=='read'" class="btn btn-success btn-rounded btn-icon btn-sm" @click="crud='create'" v-b-tooltip.html.left title="Adicionar">
                    <i class="fa fa-plus text-white"></i>
                  </b-btn>
                  <b-btn v-if="crud=='create'" class="btn btn-danger btn-rounded btn-icon btn-sm" @click="crud='read'" v-b-tooltip.html.left title="Exibir">
                    <i class="fa fa-angle-up text-white"></i>
                  </b-btn>
                -->
                  <!-- <router-link class="btn btn-danger btn-sm mr-2 btn-fw" to="/site/accounts/" v-b-tooltip.html.left title="Voltar"><i class="fa fa-angle-up"/></router-link> -->
                
                  <!--
                </span>
              </h4>
            </span>
          </div>
        </div>
        <div class="row">
          <div v-if="crud=='read'" class="col-12">
            <plg-account-services-table :items_account_services = items></plg-account-services-table>
          </div>
          <div v-if="crud=='create'" class="col-12">
            
            <form @submit.prevent="onSubmit" @reset.prevent="onReset" class="forms-sample mt-3">
              <div class="container-fluid">
                <b-form-group label="Serviço" label-for="input1">
                  <b-form-select v-model="service_selected"  :options="services"  size="sm"/>
                </b-form-group>
                <b-form-group label="Logistic Provider" label-for="input2">
                  <b-form-input v-model="newItem.preco" type="text" id="input2" placeholder="Valor" size="sm"></b-form-input>
                </b-form-group>
              </div>
              <div class="row">
                <div class="col-12">
                  <b-button type="submit" variant="danger" class="mb-2 mr-2 btn-sm"><i class="fa fa-check" v-b-tooltip.html.top title="Atualizar"></i></b-button>
                  <b-button type="reset" variant="light" class="mb-2 btn-sm"><i class="fa fa-eraser" v-b-tooltip.html.top title="Limpar"></i></b-button>
                </div>
              </div>
            </form>



          </div>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script>

const services = [
  {value:'Entrega em Lote',text: 'Entrega em Lote'},
  {value:'Logística Reversa',text: 'Logística Reversa'},
  {value:'Entrega Expressa',text: 'Entrega Expressa'},
]

const meus_items= 
[
  {
    IdDoServico: 1,
    arquivado: false,
    servico: "Entrega em Lote",
    preco: "35,90",
  },
  {
    IdDoServico: 2,
    arquivado: true,
    servico: "Logística Reversa",
    preco: "11,42",
  },
  {
    IdDoServico: 3,
    arquivado: false,
    servico: "Entrega Expressa",
    preco: "29,77",
  },
];

import PlgAccountServicesTable from './PlgAccountServicesTable.vue';

export default {
  /* eslint-disable no-console */
  components: {
    PlgAccountServicesTable,
  },

  name: "plg-account-services",

   props: {
            items_account: {
              type: [Array, Object],
              required: true,
            }
          },

  data() {
    return {

      items: meus_items,
      crud: 'read',

      newItem: {
        servico: '',
        preco: '',
      },

      services: services,
      service_selected: 'Entrega em Lote'

    }
  },

  filters: {
    booleanParaSimNao(dado) {
      return dado == false ? 'Não': dado == true ? 'Sim': 'notBool';
    },
  },

  methods: {

    onSubmit(){

      this.newItem.servico = this.service_selected;
      const maxId = this.maxItemsId();
      const newItem = {
        IdDoServico: maxId+1,
        arquivado: false,
        servico: this.newItem.servico,
        preco: this.newItem.preco,
      }

      this.items.push(newItem);

      alert("Vai fazer validações e ligar essa info ao banco de dados!");

      this.crud= 'read';

    },

    onReset(){

      this.service_selected= 'Entrega em Lote';
      this.newItem.preco = '';

    },

    maxItemsId(){
      var max = 0;

      for (var item in this.items){
        if (max < this.items[item].IdDoServico){
          max = this.items[item].IdDoServico;
        }
      }

      

      return max;
    },

    setup(){},

  },

  mounted() {

    this.setup();
    
  }
}
</script>