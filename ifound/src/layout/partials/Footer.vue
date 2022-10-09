<template>
  <section class="app-footer">
    <footer class="footer">
      <div>
        <div class="d-flex flex-column flex-md-row justify-content-around">
          <b-col cols="auto">
            <span class="text-center">
              <div>
                <i class="mdi mdi-code-greater-than text-primary"></i>
                <span class="text-secondary">&nbsp;{{ version }}</span>
              </div>
            </span>
          </b-col>
          <b-col cols="auto">
            <span v-if="environment != 'production'" class="text-center text-success">
              <div>
                <strong>{{ environment }}</strong>
              </div>
            </span>
          </b-col>
          <b-col cols="auto">
            <span class="text-center text-muted">
              <div>
                {{ email }}
              </div>
            </span>
          </b-col>
          <b-col cols="auto" class="text-center">
            <span class="">
              <span class="text text-secondary">&nbsp;{{ workspace }}</span>
            </span>
          </b-col>
        </div>
      </div>
    </footer>
  </section>
</template>

<script>
export default {
  name: "app-footer",
  data() {
    return {
      version: null,
      environment: null,
      workspace: localStorage.getItem("workspace"),
      role: localStorage.getItem("role"),
      email: localStorage.getItem("email"),
    };
  },
  mounted() {
    this.environment = process.env.VUE_APP_ENVIRONMENT
    this.version = process.env.VUE_APP_VERSION
  },
};
</script>
