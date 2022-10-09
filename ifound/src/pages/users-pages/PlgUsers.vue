<template>
  <div>
    <section class="header">
      <b-card class="p-2 border-0">
        <!-- Seção de Cabeçalho -->
        <div class="row">
          <div class="col-md-12">
            <h3 class="m-0">
              <span class="pull-left mt-2">Usuários</span>
            </h3>
            <span class="pull-right">
              <b-btn v-b-toggle.accordion_filter
                class="btn btn-primary btn-sm btn mr-2 bg-primary text-white"
                click="javascript:void(0);">
                  <i class="fa fa-filter"></i>
              </b-btn>
              <b-btn @click="newUserCall" variant="success" class="btn btn-success btn-sm btn bg-success text-white">
                <i class="mdi mdi-plus"></i>
              </b-btn>
            </span>
          </div>
        </div>
        <!-- Seção da Pesquisa -->
        <b-collapse id="accordion_filter" accordion="my-accordion">
          <b-card-body class="m-0 p-0">
            <div class="row">
              <div class="col-md-12">
                <section>
                  <form  @submit.prevent="onFilter" class="forms-sample mt-3">
                    <div class="row">
                      <div class="col-md-12 d-flex d-lg-block mt-3 justify-content-around">
                        <b-form-group label="Busca">
                          <b-input-group-append>
                            <b-form-input v-model="search" type="text" id="inputFilter" placeholder="Insira a busca" size="sm"></b-form-input>
                            <b-button v-b-toggle.accordion_filter type="submit" variant="primary" class="btn btn-sm mx-1" title="Filtrar">Filtrar</b-button>
                            <b-button v-b-toggle.accordion_filter @click="search = null" type="submit" variant="danger" class="btn btn-sm" title="Filtrar">Limpar</b-button>
                          </b-input-group-append>
                        </b-form-group>
                      </div>
                    </div>
                  </form>
                </section>
              </div>
            </div>
          </b-card-body>
        </b-collapse>
      </b-card>
    </section>
    <section class="text-center mx-3 mx-lg-0">
      <plg-users-table :search="search" ref="PlgUsersTable"></plg-users-table>
    </section>
  </div>
</template>

<script>
import PlgUsersTable from "../../components/users/PlgUsersTable.vue";


export default {
  name: 'via-users',
  components: {
    PlgUsersTable,
  },
  data: function() {
    return {
      search: null,
    };
  },
  methods: {
    onFilter(){
      this.$refs.PlgUsersTable.refreshUsers();
    },
    newUserCall() {
      this.$router.push({name: 'users_add'}).catch();
    },
  },
  mounted() {
    if(!this.$can('view', 'apis')) {
      this.$router.push({name: 'home'})
    }
  }
};
</script>
