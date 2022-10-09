<!--<template>
  <b-collapse :id="collapseId" accordion="inputFilter">
    <b-card-body class="m-0 p-0">
      <div class="row">
        <div class="col-md-12">
          <section>
            <form class="forms-sample mt-3">
              <div class="row">
                <div class="col-md-6">
                  <b-form-group label="De:">
                    <b-form-datepicker
                      v-model="fromDate"
                      locale="pt-br"
                      :date-format-options="{
                        year: 'numeric',
                        month: 'numeric',
                        day: 'numeric',
                      }"
                      :max="beforeDate"
                      :hide-header=true
                      selected-variant="primary"
                      label-help="Use as setas para navegar"
                      label-no-date-selected
                    />
                  </b-form-group>
                </div>
                <div class="col-md-6">
                  <b-form-group label="Até:">
                    <b-form-datepicker
                      v-model="beforeDate"
                      locale="pt-br"
                      :date-format-options="{
                        year: 'numeric',
                        month: 'numeric',
                        day: 'numeric',
                      }"
                      :min="fromDate"
                      :hide-header=true
                      selected-variant="primary"
                      label-help="Use as setas para navegar"
                      label-no-date-selected
                    />
                  </b-form-group>
                </div>
              </div>
            </form>
          </section>
          <b-row>
            <b-col>
              <b-button-toolbar>
                <b-button-group size="sm" class="mt-lg-3 ml-lg-2">
                  <b-button
                    @click="searchByDateFilter(7)"
                    class="border-right text-decoration-none text-dark"
                    variant="link"
                    >7 dias</b-button
                  >
                  <b-button
                    @click="searchByDateFilter(15)"
                    class="border-right text-decoration-none text-dark"
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
            <b-col>
              <div class="text-right mt-lg-3">
                <b-button
                  class="ml-5"
                  @click="searchBetweenDates()"
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
</template>

<script>
import moment from "moment";
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";

export default {
  name: "PlgBankStatementFilter",
  props: {
    collapseId: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      fromDate: null,
      beforeDate: null,
    }
  },
  computed: {
    fromDateObj() {
      return new Date(this.fromDate) || "Invalid Date";
    },
    beforeDateObj() {
      return new Date(this.beforeDate) || "Invalid Date";
    }
  },
  mixins: [PlgBankServicesApi],
  methods: {
    async searchByDateFilter(days) {
      this.noData = false;
      this.loader = true;
      let searchDate = moment().subtract(days, "days");
      const payload = {
        request_payload: { after: searchDate },
      };
      const response = this.defaultWorkspace ? await this.seeDefaultWorkspaceStatement(payload) : await this.seeAccountStatement(payload);
      if (response.data.status != "success") {
        this.$refs.Toasts.showToast(
          response.data.status,
          response.data.message
        );
      }
      this.rows = response.data.transactions_total_count;
      this.items = response.data.transactions;
      if (!this.rows) {
        this.noData = true;
        this.fields = [];
      } else {
        this.fields = [
          { key: "tags", label: "Movimento" },
          { key: "amount", label: "R$" },
          { key: "created", label: "Data" },
          { key: "actions", label: "Ações" },
        ]
      }
      this.loader = false;
    },
    async searchBetweenDates() {
      if (this.from && this.before) {
        if (this.fromDateObj == "Invalid Date" || this.beforeDateObj == "Invalid Date") {
          this.$refs.Toasts.showToast("error", "Existem datas inválidas!")
        } 
        else {
          this.loader = true;
          const payload = {
            request_payload: { after: this.fromDateObj, before: this.beforeDateObj },
          };
          const response = this.defaultWorkspace ? await this.seeDefaultWorkspaceStatement(payload) : await this.seeAccountStatement(payload);
          if (response.data.status != "success") {
            this.$refs.Toasts.showToast(
              response.data.status,
              response.data.message
            );
          }
          this.rows = response.data.transactions_total_count;
          this.items = response.data.transactions;
          if (!this.rows) {
            this.noData = true;
            this.fields = [];
          } else {
            this.fields = [
              { key: "tags", label: "Movimento" },
              { key: "amount", label: "R$" },
              { key: "created", label: "Data" },
              { key: "actions", label: "Ações" },
            ]
          }
          this.loader = false;
        }
      }
    },
  }
}
</script>
-->