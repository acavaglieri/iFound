<!--<template>
  <div>
    <section v-if="$can('view', 'defaultWorkspace')">
      <transition name="slide-up" appear mode="out-in">
        <div class="row">
          <div class="col-12">
            <div class="card rounded border">
              <div class="card-body">
                <b-row>
                  <b-col lg="1" class="d-none pt-2 d-lg-flex align-items-center">
                    <router-link :to="{ name: 'home' }" class="text-dark">
                      <h3><i class="mdi mdi-arrow-left"></i></h3>
                    </router-link>
                  </b-col>
                  <b-col lg="11">
                    <h3 class="my-3 mx-3 text-center">Workspace Padrão</h3>
                  </b-col>
                </b-row>
                <hr />
              </div>
              <template>
                <div class="row">
                  <div class="col-md-12 grid-margin stretch-card">
                    <div class="card border-0">
                      <div class="card-body">
                        <plg-bank-statement
                          :defaultWorkspace="true"
                        >
                          <template v-slot:header>
                            <div class="row">
                              <b-col cols="4" lg="9">
                                <div class="my-3 mr-3">
                                <b-button @click="goToReceive" size="sm" variant="primary">
                                  Depositar
                                </b-button>
                                </div>
                              </b-col>
                              <b-col cols="5" lg="2">
                                <div class="mt-3">
                                  <div class="d-flex justify-centent-center text-center ml-4">
                                    <PlgAccountBalance class="pb-2" :isDefaultWorkspace="true" />
                                  </div>
                                </div>
                              </b-col>
                              <b-col cols="3" lg="1">
                                <div>
                                  <div class="text-right my-3 mr-3">
                                    <b-button
                                      v-b-toggle.accordion_filter
                                      variant="primary"
                                      size="sm"
                                    >
                                      <i class="fa fa-filter"></i>
                                    </b-button>
                                  </div>
                                </div>
                              </b-col>
                            </div>
                          </template>
                          <template v-slot:filter>
                            <plg-bank-statement-filter :collapseId="'accordion_filter'"></plg-bank-statement-filter>
                          </template>
                        </plg-bank-statement>
                      </div>
                    </div>
                  </div>
                </div>
              </template>
            </div>
          </div>
        </div>
      </transition>
    </section>
  </div>
</template>

<script>
import PlgBankStatement from "../../components/bank-statement/PlgBankStatement.vue";
import PlgBankStatementFilter from "../../components/bank-statement/PlgBankStatementFilter.vue";
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";
import PlgAccountBalance from "../../components/accounts/PlgAccountBalance.vue";

export default {
  name: "PlgDefaultWorkspaceBalance",
  components: {
    PlgBankStatement,
    PlgBankStatementFilter,
    PlgAccountBalance,
  },
  mixins: [PlgBankServicesApi],
  computed: {
    userRole() {
      return localStorage.getItem("role");
    }
  },
  data() {
    return {
      balance: null,
    }
  },
  methods: {
    async getDefaultWorkspaceBalance() {
      let response = await this.seeDefaultWorkspaceBalance();
      this.balance = response.data.balance / 100;
      this.balance = this.balance.toLocaleString('pt-BR', {minimumFractionDigits: 2})
    },
    goToReceive() {
      this.$router.replace({name: 'pix_generate_charge', params: {toDefaultWorkspace: true}})
    },
    checkIfUserIsAdmin() {
      if (this.userRole != "admin") {
        this.$router.replace({ name: "home" });
      }
    },
  },
  mounted() {
    this.checkIfUserIsAdmin();
  },
};
</script>