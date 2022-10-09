<!--<template>
  <div>
    <Toasts ref="Toasts"></Toasts>
    <PlgBankServicesApi ref="PlgBankServicesApi"></PlgBankServicesApi>
    <transition name="slide-up" appear mode="out-in">
      <section class="tables">
        <div class="row">
          <div class="col">
            <div class="card rounded border">
              <plg-bank-statement>
                <template v-slot:header>
                  <div class="row">
                    <b-col cols="6" lg="10">
                      <div class="card-title ml-4 mt-4">
                        <h4>Animais</h4>
                      </div>
                    </b-col>
                    <b-col lg="1" class="pt-2 d-none d-md-flex justify-content-end align-items-center">
                      <router-link :to="{ name: 'home' }" style="color: black">
                        <h3><i class="mdi mdi-lg mdi-arrow-left" /></h3>
                      </router-link>
                    </b-col>
                    <b-col cols="6" lg="1">
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
                  <plg-bank-statement-filter :collapseId="'accordion_filter'" />
                </template>
              </plg-bank-statement>
            </div>
          </div>
        </div>
      </section>
    </transition>
  </div>
</template>

<script>
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";
import PlgBankStatement from "../../components/bank-statement/PlgBankStatement.vue";
import PlgBankStatementFilter from "../../components/bank-statement/PlgBankStatementFilter.vue";
import Toasts from "../../components/Toasts.vue";


export default {
  components: {
    Toasts,
    PlgBankServicesApi,
    PlgBankStatement,
    PlgBankStatementFilter
  },
};
</script>