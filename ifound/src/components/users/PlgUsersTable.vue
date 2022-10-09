<template>
  <div>
    <Toasts ref="Toasts"></Toasts>
    <PlgUsersApi ref="PlgUsersApi"></PlgUsersApi>
    <section class="tables">
      <div class="row">
        <div class="col-12">
          <div class="card border-0">
            <b-table
              :items="items"
              id="table-list"
              responsive
              :fields="fields"
              @sort-changed="sortChanged"
              small
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
            >
              <template v-slot:cell(name)="data"><i v-if="data.item.is_inactive" class="fa fa-archive text-danger"/> {{data.value}}</template>
              <template v-slot:cell(acoes)="data">
                <router-link class="btn btn-warning btn-sm text-white mr-2 btn-fw" :to="'/site/users/' + data.item.id + '/edit'" title="Abrir">
                  <i class="fa fa-search"></i>
                </router-link>
                <b-button variant="danger" size="sm" class="text-white" @click="deleteId = data.item.id" v-b-modal.modal-del>
                  <i class="fa fa-trash"></i>
                </b-button>
              </template>
            </b-table>
            <div class="row">
              <div class="col-12" v-show="rows > perPage">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="table-list"
                  align="center"
                  @input="refreshLastPage();"
                ></b-pagination>
              </div>
              <div class="col">
                <div class="btn-group ml-3 pull-left mt-2 mt-lg-0" role="group" aria-label="items-per-page">
                  <b-button variant="outline-primary" size="sm" title="Items por Página" @click="changePerPage(25)">25</b-button>
                  <b-button variant="outline-primary" size="sm" title="Items por Página" @click="changePerPage(50)">50</b-button>
                  <b-button variant="outline-primary" size="sm" title="Items por Página" @click="changePerPage(100)">100</b-button>
                  <b-button variant="outline-primary" size="sm" title="Items por Página" @click="changePerPage(200)">200</b-button>
                </div>
              </div>
              <div class="d-flex justify-items-end mb-2">
                <b-button @click="generateXlsxApi" variant="success" size="sm" title="Exportar para Excel">
                  <i class="fa fa-file-excel-o"></i>
                </b-button>
                <div class="col pl-2" align="right">
                  <span v-if="isCompact" align="center"><b-btn variant="info" class="btn btn-success btn-icon btn-sm text-white mr-3" v-on:click=changeIsCompact(false) title="Completo"><i class="fa fa-cubes"></i></b-btn></span>
                  <span v-if="!isCompact" align="center"><b-btn variant="success" class="btn btn-success btn-icon btn-sm mr-3" v-on:click=changeIsCompact(true) title="Resumido"><i class="fa fa-cube"></i></b-btn></span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <b-modal header-bg-variant="danger" header-text-variant="light" id="modal-del" title="Deletar Usuário" centered no-fade>
      <p class="my-4">Tem certeza que deseja deletar esse usuário? Essa ação não pode ser desfeita.</p>
      <template #modal-footer="{ cancel, hide }">
        <b-button size="md" variant="danger" @click="cancel()">
          Cancelar
        </b-button>
        <b-button size="md" variant="success" @click="deleteUser(deleteId), hide()">
          OK
        </b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
import PlgUsersApi from '../../apis/PlgUsersApi.vue';
import Toasts from '../Toasts.vue';


export default {
  name: "plg-users-table",
  props: {
    search: String
  },
  components: {
    Toasts,
    PlgUsersApi
  },
  data() {
    return {
      sortBy: "id",
      perPage: 25,
      lastPage: 1,
      currentPage: 1,
      fields: [],
      items: [],
      rows: 0,
      sortDesc: false,
      deleteId: null,
      isCompact: false,
    };
  },
  methods: {
    sortChanged(e) {
      this.sortBy = e.sortBy;
      if (e.sortDesc)
        this.sortBy = e.sortBy;
      this.refreshUsers();
    },
    changePerPage(perPage) {
      this.perPage = perPage;
      this.refreshUsers();
    },
    refreshLastPage() {
      if (this.currentPage != this.lastPage) {
        this.lastPage = this.currentPage;
        this.refreshUsers();
      }
    },
    async generateXlsxApi() {
      let userFilter = this.$refs.PlgUsersApi.getFilterForUsersApi();
      const filterPayload = {
        full_search: userFilter.full_search,
        limit: this.totalRows
      }
      this.$refs.PlgUsersApi.generateXlsx(filterPayload);
    },
    async refreshUsers() {
      let filter = this.$refs.PlgUsersApi.getFilterForUsersApi();
      filter.limit = this.perPage; 
      filter.sort = this.sortBy; 
      filter.full_search = this.search;
      const payload = {
        filter: filter
      }
      let response = await this.$refs.PlgUsersApi.getUsersApi(payload);
      if(response.data.status != "success") {
        this.$refs.Toasts.showToast(response.data.status, response.data.message);
      }
      this.items = response.data.users;
      this.rows = response.data.users_count;
    },
    changeIsCompact(valor){
      if(valor==true){
        this.seeCompact();
      }else{
        this.seeComplete();
      }
    },
    seeComplete(){
      this.fields =
      [
        { key: "name", label: "Nome", sortable: true },
        { key: "email", label: "Email", sortable: true },
        { key: "cellphone", label: "Celular", sortable: true },
        { key: "state", label: "UF", sortable: true },
        { key: "acoes", label: "Ações", sortable: false }
      ];
      this.isCompact = false;
    },
    seeCompact(){
      this.fields =
      [
        { key: "name", label: "Nome", sortable: true },
        { key: "cellphone", label: "Telefone", sortable: true },
        { key: "email", label: "Email", sortable: true },
        { key: "acoes", label: "Ações", sortable: false }
      ];
      this.isCompact = true;
    },
    async deleteUser(id) {
      let response = await this.$refs.PlgUsersApi.deleteUserApi(id);
      this.$refs.Toasts.showToast(response.data.status, response.data.message)
      this.refreshUsers();
    }
  },
  mounted() {
    this.changeIsCompact(true);
    this.refreshUsers();
  },
};
</script>