<template>
  <div>
    <section class="header">
      <div class="row">
        <div class="col">
          <div class="card">

            <div class="container-fluid mt-3">
              <div class="row">
                <div class="col-lg-12">
                  <div class="accordion">
                    <b-card>

                      <!-- Seção de Cabeçalho -->
                      <b-card-title>
                        <div class="row">
                          <div class="col-md-12">
                            <h4 class="card-title mt-3 ml-3 vertical-align: middle">
                              <span class="pull-left">Contas</span>
                              <span class="pull-right">
                                <b-btn v-b-toggle.accordion1
                                  class="btn btn-primary btn-rounded btn-icon btn-sm mr-2 bg-primary text-white"
                                  click="javascript:void(0);"
                                   v-b-tooltip.html.left title="Filtro">
                                    <i class="fa fa-filter"></i>
                                </b-btn>
                                <b-btn class="btn btn-dark btn-rounded btn-icon btn-sm mr-2" v-b-tooltip.html.bottom title="Conta Principal">
                                  <i class="fa fa fa-id-card text-white"></i>
                                </b-btn>
                                <router-link 
                                  class="btn btn-success btn-rounded btn-icon btn-sm mr-3" 
                                   v-b-tooltip.html.bottom title="Nova Conta"
                                  :to="'/site/accounts/new'">
                                    <i class="fa fa-plus text-white mt-2"/>
                                </router-link>
                              </span>
                            </h4>
                          </div>
                        </div>
                      </b-card-title>

                      <!-- Seção da Pesquisa -->
                      <b-collapse id="accordion1" accordion="my-accordion">
                        <b-card-body>
                          <div class="row">
                            <div class="col-md-12">
                              <section>
                                <form  @submit.prevent="onSubmit" class="forms-sample mt-3">
                                  <b-form-group label="Busca" >
                                    <b-form-input v-model="search" type="text" placeholder="Insira a busca aqui..." size="sm"></b-form-input>
                                  </b-form-group>
                                  <b-form-group label="Tipo" >
                                    <b-form-select v-model="search_kind" :options="options_search_kind" size="sm" />
                                  </b-form-group>
                                  <b-button type="submit" variant="primary" class="mt-3 mr-2 btn-sm" v-b-tooltip.html.top title="Filtrar"><i class="fa fa-filter"></i></b-button>
                                  <b-button type="reset" variant="danger" class="mt-3 mr-2 btn-sm" v-b-tooltip.html.top title="Limpar"><i class="fa fa-window-close text-white"></i></b-button>
                                </form>
                              </section>
                            </div>
                          </div>
                        </b-card-body>
                      </b-collapse>

                    </b-card>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <plg-accounts-table ref="plgAccountPlgAccountsTable"></plg-accounts-table>
  </div>
</template>


<script>
import PlgAccountsTable from '../components/accounts/PlgAccountsTable.vue';

export default {
  
  name: 'plg-accounts',

  components: {
    PlgAccountsTable,
  },

  data: function() {
    return {
      search: '',
      search_kind: 'Cliente',
      options_search_kind:
        [
          { value: 'Cliente', text: 'Cliente' },
          { value: 'Fornecedor', text: 'Fornecedor' },
        ],
    };
  },

  methods: {
    onSubmit(){
      this.$refs.plgAccountPlgAccountsTable.search = this.search;
      this.$refs.plgAccountPlgAccountsTable.search_kind = this.search_kind;
      this.$refs.plgAccountPlgAccountsTable.refreshAccounts();
    },
  },
};
</script>
