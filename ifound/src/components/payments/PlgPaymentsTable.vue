<!--<template>
  <div>
    <Toasts ref="Toasts"></Toasts>
    <PlgPaymentsApi ref="PlgPaymentsApi"></PlgPaymentsApi>
    <section class="tables">
      <div class="card border rounded">
        <div class="mb-5">
          <slot name="header"></slot>
          <div class="mr-4 mt-2">
            <b-row>
              <b-col cols="5" lg="3">
                <div class="mr-lg-5">
                  <b-button
                    variant="success"
                    size="sm"
                    class="text-white ml-3 mr-lg-2"
                    @click="goToNewPayment()"
                  >
                    <i class="fa fa-plus"></i>
                  </b-button>
                  <b-button v-b-toggle.accordion_filter
                    class="mr-lg-5 mr-4 text-white"
                    size="sm"
                    variant="primary"
                  >
                      <i class="fa fa-filter"></i>
                  </b-button>
                </div>
              </b-col>
              <b-col cols="4" lg="7"></b-col>
              <b-col cols="3" lg="2">
                <b-button-group>
                  <b-button
                    variant="success"
                    size="sm"
                    class="text-white ml-lg-5"
                    @click="openModalPayments('confirm')"
                    v-b-modal.modal-payments
                  >
                    <i class="fa fa-check-square"></i>
                  </b-button>
                  <b-button
                    variant="danger"
                    size="sm"
                    class="text-white mr-lg-3"
                    @click="openModalPayments('decline')"
                    v-b-modal.modal-payments
                  >
                    <i class="fa fa-window-close"></i>
                  </b-button>
                </b-button-group>
              </b-col>
            </b-row>
          </div>
          <b-collapse id="accordion_filter" accordion="inputFilter">
            <b-card-body class="mx-2">
              <div class="row">
                <div class="col-md-12">
                  <section>
                    <form class="forms-sample mt-3">
                      <div class="row">
                        <b-col lg="6">
                          <b-form-group label="Data Agendada:">
                            <b-form-input
                              v-model="filterPayments.scheduledDate"
                              type="date"
                              id="inputScheduledDate"
                              size="sm"
                            ></b-form-input>
                          </b-form-group>
                          <b-form-group label="CPF do Recebedor:">
                            <b-form-input
                              v-model="filterPayments.receiverFederalId"
                              type="tel"
                              v-mask="['###.###.###-##']"
                              id="inputFederalId"
                              size="sm"
                            ></b-form-input>
                          </b-form-group>
                        </b-col>
                        <b-col lg="6">  -->
                          <!---<b-form-group label="Quantia:">
                            <money
                              v-model="filterPayments.petName"
                              type="tel"
                              id="inputAmount"
                              placeholder="Quantia"
                              size="sm"
                              v-bind="money"
                              maxlength="10"
                              class="form-control form-control-sm"
                            ></money> 
                          </b-form-group>-->
                          <!--
                          <b-form-group label="PetName:">
                            <b-form-input
                              v-model="filterPayments.petName"
                              type="text"
                              id="inputPetName"
                              size="sm">
                            </b-form-input>
                          </b-form-group>
                          <b-form-group label="Raça:">
                            <b-form-input
                              v-model="filterPayments.description"
                              type="text"
                              id="inputFederalId"
                              size="sm">
                            </b-form-input>
                          </b-form-group>
                        </b-col>
                      </div>
                    </form>
                  </section>
                  <b-row>
                    <b-col cols="6">
                      <b-button-toolbar>
                        <b-button-group size="sm" class="mt-lg-3 ml-lg-2">
                          <b-button
                            @click="searchByDateFilter(7)"
                            class="
                              border-right
                              text-decoration-none text-dark
                            "
                            variant="link"
                            >7 dias</b-button
                          >
                          <b-button
                            @click="searchByDateFilter(15)"
                            class="
                              border-right
                              text-decoration-none text-dark
                            "
                            variant="link"
                            >15 dias</b-button
                          >
                          <b-button
                            @click="searchByDateFilter(30)"
                            class="text-decoration-none text-dark"
                            variant="link"
                            >30 dias</b-button
                          >
                        </b-button-group>
                      </b-button-toolbar>
                    </b-col>
                    <b-col cols="6">
                      <div class="text-right mt-lg-3">
                        <b-button
                          class="ml-5"
                          @click="filterPaymentsApi()"
                          size="md"
                          variant="primary"
                          >Filtrar</b-button
                        >
                      </div>
                    </b-col>
                  </b-row>
                </div>
              </div>
            </b-card-body>
          </b-collapse>
        </div>
        <div class="mx-3">
          <b-table
            :items="items"
            id="table-list"
            :busy="loading"
            responsive
            :fields="fields"
            @sort-changed="sortChanged"
            :sort-by.sync="sortBy"
            :sort-desc.sync="sortDesc"
          >
            <template #table-busy>
              <div>
                <b-skeleton-table
                  class="mt-2"
                  :columns="5"
                  :rows="3"
                />
              </div>
            </template>
            <template #head(select)="data">
              <b class="table-font">{{ data.label }}</b>
            </template>
            <template class="table-font" v-slot:cell(select)="data">
              <b-form-group>
                <b-form-checkbox
                  v-model="selectedPayments"
                  :value="data.item.id"
                ></b-form-checkbox>
              </b-form-group>
            </template>
            <template #head(receiver_name)="data">
              <b class="table-font">{{ data.label }}</b>
            </template>
            <template v-slot:cell(receiver_name)="data">
              <b class="table-font">{{ data.item.receiver_name }}</b>
            </template>
            <template #head(amount)="data">
              <b class="table-font">{{ data.label }}</b>
            </template>
            <template v-slot:cell(amount)="data">
              <b class="table-font"> R$ {{ formatAmount(data.item.amount) }}</b>
            </template>
            <template #head(description)="data">
              <b class="table-font">{{ data.label }}</b>
            </template>
            <template v-slot:cell(description)="data">
              <b class="table-font"> {{ data.item.description }}</b>
            </template>
            <template #head(scheduled_date)="data">
              <b class="table-font">{{ data.label }}</b>
            </template>
            <template v-slot:cell(scheduled_date)="data">
              <b class="table-font">{{ formatDate(data.item.scheduled_date) }}</b>
            </template>
            <template #head(actions)="data">
              <b class="table-font">{{ data.label }}</b>
            </template>
            <template v-slot:cell(actions)="data">
              <b class="table-font">
              <router-link
                class="btn btn-warning btn-sm text-white btn-fw"
                :to="{name: 'payments_edit', params: {id: data.item.id}}"
                title="Editar"
              >
                <i class="fa fa-pencil"></i>
              </router-link>
              </b>
            </template>
          </b-table>
        </div>
        <div class="row" v-show="!rows">
          <div class="col">
            <div class="card border-0 my-5" style="text-align: center">
              <i class="mdi mdi mdi-account-cash text-muted" style="font-size: 50px">!</i>
              <h3 class="text-muted">Não há pagamentos!</h3>
              <h4 class="text-muted">Crie um novo ou cheque os filtros.</h4>
            </div>
          </div>
        </div>
        <div class="row my-4">
          <div class="col-12" v-show="rows > perPage">
            <b-pagination
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              aria-controls="table-list"
              align="center"
              @input="refreshLastPage()"
            ></b-pagination>
          </div>
          <div class="col text-center">
            <div
              class="btn-group text-center mt-2 mt-lg-0"
              role="group"
              aria-label="items-per-page"
            >
              <b-button
                variant="outline-primary"
                size="sm"
                title="Items por Página"
                @click="changePerPage(25)"
                >25</b-button
              >
              <b-button
                variant="outline-primary"
                size="sm"
                title="Items por Página"
                @click="changePerPage(50)"
                >50</b-button
              >
              <b-button
                variant="outline-primary"
                size="sm"
                title="Items por Página"
                @click="changePerPage(100)"
                >100</b-button
              >
              <b-button
                variant="outline-primary"
                size="sm"
                title="Items por Página"
                @click="changePerPage(200)"
                >200</b-button
              >
            </div>
          </div>
        </div>
      </div>
    </section>
    <b-modal id="modal-payments" centered>
      <template #modal-header>
        <span>{{ modalPayments.title }}</span>
      </template>
      <p class="my-4">
        Ao fazer isso os pagamentos selecionados serão
        {{ modalPayments.action }}. Tem certeza de que quer continuar?
      </p>
      <template #modal-footer="{ cancel, hide }">
        <b-button size="md" variant="secondary" @click="cancel()">
          <span class="cancel-button">Cancelar</span>
        </b-button>
        <b-button
          size="md"
          :variant="modalPayments.button"
          @click="modalPayments.askForSchedule ? handleScheduleModal() : executePaymentsActions(modalPayments.var), hide()"
        >
          Confirmar
        </b-button>
      </template>
    </b-modal>
    <b-modal v-model="askForScheduleModal" centered>
      <template #modal-header>
        <span>Realizar pagamento instantâneo?</span>
      </template>
      <p class="my-1">Deseja realizar o(s) pagamento(s) agora?</p>
      <template #modal-footer>
        <b-button size="md" variant="secondary" @click="executePaymentsActions(modalPayments.var, true)">
          <span class="cancel-button">Manter data agendada</span>
        </b-button>
        <b-button
          size="md"
          :variant="modalPayments.button"
          @click="executePaymentsActions(modalPayments.var, false)"
        >
          Pagar agora
        </b-button>
      </template>
    </b-modal>
  </div>
</template>

<script>
import PlgPaymentsApi from "../../apis/PlgPaymentsApi.vue";
import Toasts from "../Toasts.vue";
import moment from "moment";

export default {
  name: "plg-payments-table",
  props: {
    search: String,
  },
  components: {
    Toasts,
    PlgPaymentsApi,
  },
  data() {
    return {
      sortBy: "id",
      perPage: 25,
      lastPage: 1,
      currentPage: 1,
      filterPayments: {
        scheduledDate: null,
        receiverFederalId: null,
        amount: 0,
        description: null,
      },
      submitted: null,
      money: {
        decimal: ',',
        thousands: '.',
        prefix: 'R$ ',
        precision: 2,
        masked: false,
      },
      fields: [
        { key: "select", label: "Selecionar", sortable: false, class: "table-font" },
        { key: "receiver_name", label: "Para", sortable: false, class: "table-font" },
        { key: "petName", label: "PetName", sortable: true, class: "table-font" },
        { key: "description", label: "Raça", sortable: true, class: "table-font" },
      ],
      modalPayments: {
        title: null,
        action: null,
        button: null,
        askForSchedule: false,
      },
      loading: false,
      askForScheduleModal: false,
      items: [],
      selectedPayments: [],
      rows: 0,
      sortDesc: false,
      deleteId: null,
    };
  },
  methods: {
    goToNewPayment() {
      this.$router.replace({name: 'payments_new'})
    },
    handleScheduleModal() {
      this.askForScheduleModal = !this.askForScheduleModal
    },
    openModalPayments(action) {
      if (action === "confirm") {
        this.modalPayments.title = "Aprovar Pagamentos";
        this.modalPayments.action = "aprovados";
        this.modalPayments.button = "success";
        this.modalPayments.askForSchedule = true
        this.modalPayments.var = action;
      } else if (action === "decline") {
        this.modalPayments.title = "Recusar Pagamentos";
        this.modalPayments.action = "recusados";
        this.modalPayments.button = "danger";
        this.modalPayments.var = action;
      }
    },
    formatDate(date) {
      let newDate = moment(date, "YYYY-MM-DD").format("DD/MM/YYYY");
      return newDate;
    },
    formatAmount(amount) {
      let newAmount = amount / 100;
      return newAmount.toLocaleString('pt-BR', {minimumFractionDigits: 2});
    },
    sortChanged(e) {
      this.sortBy = e.sortBy;
      if (e.sortDesc) this.sortBy = e.sortBy;
      this.refreshPayments();
    },
    changePerPage(perPage) {
      this.perPage = perPage;
      this.refreshPayments();
    },
    refreshLastPage() {
      if (this.currentPage != this.lastPage) {
        this.lastPage = this.currentPage;
        this.refreshPayments();
      }
    },
    async searchByDateFilter(days) {
      this.loader = true;
      let searchDate = moment().subtract(days, "days");
      searchDate = searchDate.toISOString().split("T")[0]
      let response = null;
      const payload = {
        filter: { after_date: searchDate },
      };
      response = await this.$refs.PlgPaymentsApi.getPaymentsApi(
        payload
      );
      if (response.data.status != "success") {
        this.$refs.Toasts.showToast(
          response.data.status,
          response.data.message
        );
      }
      this.rows = response.data.payments_total_count;
      this.items = response.data.payments;
      this.loader = false;
    },
    async filterPaymentsApi() {
      this.filterPayments.limit = this.perPage;
      this.filterPayments.sort = this.sortBy;
      const payload = {
        filter: { 
          scheduled_date: this.filterPayments.scheduledDate || null,
          receiver_federal_id: this.filterPayments.receiverFederalId,
          amount: this.filterPayments.petName * 100 || null,
          description: this.filterPayments.description,
        },
      };
      let response = await this.$refs.PlgPaymentsApi.getPaymentsApi(payload);
      if (response.data.status != "success") {
        this.$refs.Toasts.showToast(
          response.data.status,
          response.data.message
        );
      }
      this.items = response.data.payments;
      this.rows = response.data.payments_total_count;
      this.submitted = false;
    },
    async refreshPayments() {
      this.loading = true;
      let filter = this.$refs.PlgPaymentsApi.getFilterForPaymentsApi();
      filter.limit = this.perPage;
      filter.sort = this.sortBy;
      const payload = {
        filter: filter,
      };
      let response = await this.$refs.PlgPaymentsApi.getPaymentsApi(payload);
      if (response.data.status != "success") {
        this.$refs.Toasts.showToast(
          response.data.status,
          response.data.message
        );
      }
      this.items = response.data.payments;
      this.rows = response.data.payments_total_count;
      this.loading = false;
    },
    async confirmOrCancelPayment(paymentId, paymentAction, pay_on_schedule) {
      let response = null;
      const payload = {
        workspace: {
          id: localStorage.getItem("workspace")
        },
        new_payment_data: {
          approved: paymentAction === "confirm" ? "approved" : "declined",
          pay_on_schedule: paymentAction === "confirm" ? pay_on_schedule : null,
        },
      };
      response = pay_on_schedule ? await this.$refs.PlgPaymentsApi.updatePaymentApi(paymentId, payload) : await this.$refs.PlgPaymentsApi.payPaymentApi(paymentId, payload);
      this.$refs.Toasts.showToast(response.data.status, response.data.message);
      this.refreshPayments()
    },
    executePaymentsActions(action, pay_on_schedule) {
      this.selectedPayments.forEach((entry) => {
        this.confirmOrCancelPayment(entry, action, pay_on_schedule);
      });
    },
  },
  mounted() {
    this.refreshPayments();
  },
};
</script>

<style>
.cancel-button {
  color: white;
}
.table-font {
  font-size: .9rem;
}
</style>
