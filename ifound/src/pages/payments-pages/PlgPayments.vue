<!--<template>
  <div>
    <transition name="slide-up" appear mode="out-in">
      <div>
        <section class="text-center">
          <plg-payments-table :search="search" ref="PlgPaymentsTable">
            <template v-slot:header>
              <div class="row p-3">
                <div class="col-md-12">
                  <h3 class="m-0">
                    <span class="pull-left mt-2 text-muted">Pagamentos</span>
                  </h3>
                </div>
              </div>
            </template>
          </plg-payments-table>
        </section>
      </div>
    </transition>
  </div>
</template>

<script>
import PlgPaymentsTable from "../../components/payments/PlgPaymentsTable.vue";


export default {
  name: 'via-payments',
  components: {
    PlgPaymentsTable,
  },
  data: function() {
    return {
      search: null,
    };
  },
  methods: {
    onFilter(){
      this.$refs.PlgPaymentsTable.refreshPayments();
    },
  },
  mounted() {
    if(!this.$can('view', 'apis')) {
      this.$router.push({name: 'home'})
    }
  }
};
</script>
