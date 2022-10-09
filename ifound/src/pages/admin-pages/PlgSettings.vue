<!--<template>
  <div>
    <div class="card border rounded">
      <h3 class="text-muted p-4">Configurações</h3>
      <div class="p-4">
        <b-row class="d-flex align-items-center">
          <b-col cols="12" md="10">
            <b-form-select v-model="selectedTask" :options="tasks" />
          </b-col>
          <b-col cols="12" md="auto">
            <b-button
              variant="primary"
              @click="runTask"
            >
              Rodar Task
            </b-button>
          </b-col>
        </b-row>
        <div v-if="loading || taskData">
          <hr>
          <b-row class="p-3">
            <b-col v-if="loading" cols="12">
              <b-skeleton></b-skeleton>
              <b-skeleton width="75%"></b-skeleton>
              <b-skeleton width="68%"></b-skeleton>
            </b-col>
            <b-col v-else-if="taskData">
                <span v-for="string in taskData" :key="string">
                  {{ string }} <br>
                </span>
            </b-col>
          </b-row>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import PlgPaymentsApi from "../../apis/PlgPaymentsApi.vue";
export default {
  name: "Settings",
  mixins: [PlgPaymentsApi],
  data() {
    return {
      tasks: [
        {
          text: "Realizar pagamentos agendados", value: "scheduledPayments",
        }
      ],
      taskData: null,
      loading: false,
      selectedTask: "scheduledPayments",
    }
  },
  methods: {
    async runTask() {
      this.loading = true;
      const response = this.selectedTask == "scheduledPayments" ? await this.payScheduledPayments() : null;
      this.taskData = response?.data.split("\n\n");
      this.taskData = this.taskData.filter(el => el)
      this.loading = false;
    }
  },
};
</script>