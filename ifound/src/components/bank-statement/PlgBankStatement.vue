<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Pets</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.pet-modal>Add Pet</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Nome</th>
              <th scope="col">Raça</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(pet, index) in pets" :key="index">
              <td>{{ pet.name }}</td>
              <td>{{ pet.raca }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.pet-update-modal
                          @click="editPet(pet)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeletePet(pet)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
   </div>
  <b-modal ref="addPetModal"
            id="pet-modal"
            name="Add a new pet"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addPetForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-raca-group"
                      label="Raça:"
                      label-for="form-raca-input">
            <b-form-input id="form-raca-input"
                          type="text"
                          v-model="addPetForm.raca"
                          required
                          placeholder="Enter raca">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  <b-modal ref="editPetModal"
       id="pet-update-modal"
       name="Update"
       hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                          type="text"
                          v-model="editForm.name"
                          required
                          placeholder="Enter name">
          </b-form-input>
          </b-form-group>
          <b-form-group id="form-raca-edit-group"
                      label="Raça:"
                      label-for="form-raca-edit-input">
              <b-form-input id="form-raca-edit-input"
                          type="text"
                          v-model="editForm.raca"
                          required
                          placeholder="Enter raca">
              </b-form-input>
          </b-form-group>
          <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
          </b-button-group>
      </b-form>
  </b-modal>
  <template v-slot:cell(actions)="data">
                  <router-link
                    class="btn btn-warning btn-sm text-white mr-2 btn-fw"
                    :to="{
                      name: 'pets_info',
                      params: {
                        id: data.item.id,
                        account_type: 'user',
                      },
                    }"
                    v-b-tooltip.html.left
                    title="Abrir"
                  >
                    <i class="fa fa-search"></i>
                  </router-link>
                </template>


  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';


export default {
  name: "Pets",
  data() {
    return {
      pets: [],
      addPetForm: {
        name: '',
        raca: '',
        read: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
  alert: Alert,
  },
  methods: {
    getPets() {
      const path = 'http://localhost:8000/pets';
      axios.get(path)
        .then((res) => {
          this.pets = res.data.pets;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addPet(payload) {
      const path = 'http://localhost:8000/pets';
      axios.post(path, payload)
          .then(() => {
          this.getPets();
          this.message = 'Pet added!';
          this.showMessage = true;
          })
          .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getPets();
      });
    },
    initForm() {
      this.addPetForm.name = '';
      this.addPetForm.raca = '';
      this.editForm.id = '';
      this.editForm.name = '';
      this.editForm.raca = '';
    },
    editPet(pet) {
      this.editForm = pet;
    },
    editForm: {
      id: '',
      name: '',
      raca: '',
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addPetModal.hide();
      this.addPet(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editPetModal.hide();
      this.updatePet(payload, this.editForm.id);
    },
    updatePet(payload, petID) {
      const path = `http://localhost:8000/pets/${petID}`;
      axios.put(path, payload)
          .then(() => {
          this.getPets();
          this.message = 'Pet updated!';
          this.showMessage = true;
          })
          .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPets();
          });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editPetModal.hide();
      this.initForm();
      this.getPets(); // why?
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addPetModal.hide();
      this.initForm();
    },
  created() {
    this.getPets();
  },
  removePet(petID) {
      const path = `http://localhost:8000/pets/${petID}`;
      axios.delete(path)
      .then(() => {
          this.getPets();
          this.message = 'Pet removed!';
          this.showMessage = true;
      })
      .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getPets();
      });
  },
  onDeletePet(pet) {
      this.removePet(pet.id);
  },
},
};
</script>


<!--<template>
  <div>
    <Toasts ref="Toasts"></Toasts>
    <section v-show="seeData" class="tables">
      <div class="row">
        <div class="col">
          <div class="card border-0">
            <slot name="header"></slot>
            <div class="mx-md-3">
              <slot name="filter"></slot>
              <b-table
                class="text-center"
                :items="items"
                id="table-list"
                responsive
                :busy="loader"
                :fields="fields"
                :per-page="perPage"
                :current-page="currentPage"
                :sort-by.sync="sortBy"
                :sort-desc.sync="sortDesc"
              > -->
                <!--<template #table-busy>
                  <div>
                    <b-skeleton-table
                      class="mt-2"
                      :columns="2"
                      :rows="2"
                    />
                  </div>
                </template> -->
                <!--<template #cell(amount)="data">
                  <b :class="formatTags(data.item.amount)['tagVariant']">{{
                    formatAmount(data.item.amount)
                  }}</b>
                </template> 
                <template #cell(description)="data">
                  <b :class="formatTags(data.item.amount)['tagVariant']">{{
                    data.item.description
                  }}</b>
                </template>
                <template #cell(created)="data">
                  <b :class="formatTags(data.item.amount)['tagVariant']">{{
                    formatDate(data.item.created)
                  }}</b>
                </template>-->
                <!--
                <template v-slot:cell(actions)="data">
                  <router-link
                    class="btn btn-warning btn-sm text-white mr-2 btn-fw"
                    :to="{
                      name: 'animais_info',
                      params: {
                        id: data.item.id,
                        account_type: 'user',
                      },
                    }"
                    v-b-tooltip.html.left
                    title="Abrir"
                  >
                    <i class="fa fa-search"></i>
                  </router-link>
                </template>
              </b-table>
            </div>
            <div v-if="rows > 20" class="row">
              <div class="col">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  align="center"
                  :per-page="perPage"
                ></b-pagination>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section v-if="!seeData && !loader" class="tables">
      <div class="row">
        <div class="col">
          <div class="card border-0" style="text-align: center">
            <i class="mdi mdi-eye-off text-muted" style="font-size: 50px"></i>
            <h3 class="text-muted">Animais ocultados</h3>
          </div>
        </div>
      </div>
    </section>
    <section v-if="!rows && seeData && !loader" class="tables">
      <div class="row">
        <div class="col">
          <div class="card border-0 my-5" style="text-align: center">
            <i class="mdi mdi-note-outline text-muted" style="font-size: 50px">!</i>
            <h3 class="text-muted">Não há nenhum registro!</h3>
            <h4 class="text-muted">Cheque os filtros ou faça uma transação.</h4>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import PlgBankServicesApi from "../../apis/PlgBankServicesApi.vue";
import Toasts from "../../components/Toasts.vue";
import moment from "moment";

export default {
  name: "plg-bank-statement",
  props: {
    seeData: {
      type: Boolean,
      default: true,
    },
    defaultWorkspace: {
      type: Boolean,
      default: false,
    }
  },
  components: {
    Toasts,
  },
  mixins: [PlgBankServicesApi],
  computed: {
    totalOuts() {
      if (this.outsArray.length) {
        return this.outsArray.reduce((previousValue, currentValue) => {
          return parseFloat(previousValue) + parseFloat(currentValue);
        }) / 100;
      } else {
        return 0;
      }
    },
    totalIns() {
      if (this.insArray.length) {
        return this.insArray.reduce((previousValue, currentValue) => {
          return parseFloat(previousValue) + parseFloat(currentValue);
        }) / 100;
      } else {
        return 0;
      }
    }
  },
  data() {
    const now = new Date();
    const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    return {
      sortBy: "created",
      sortDesc: true,
      perPage: 20,
      currentPage: 1,
      today: today,
      outsArray: [],
      insArray: [],
      loader: false,
      fields: [],
      items: [],
      rows: 0,
    };
  },
  methods: {
    refreshLastPage() {
      if (this.currentPage != this.lastPage) {
        this.currentPage = this.lastPage;
      }
    },
    separateValues(amount) {
      if (amount < 0) {
        let positiveAmount = amount * -1;
        this.outsArray.push(positiveAmount);
      } else {
        this.insArray.push(amount);
      }
    },
    /*formatTags(amount) {
      let tagVariant, formatedTag;
      if (amount < 0) {
        tagVariant = "text-dark";
        formatedTag = "Saíram";
      } else {
        tagVariant = "text-success";
        formatedTag = "Você recebeu";
      }
      return { formatedTag, tagVariant };
    }, */
    formatDate(date) {
      let newDate = moment(date, "YYYY-MM-DDTHH:mm:ssZ").format("DD/MM/YYYY");
      return newDate;
    },
    formatAmount(amount) {
      let newAmount = amount / 100;
      let sign = "+";
      if (newAmount < 0) {
        newAmount = newAmount * -1;
        sign = "-";
      }
      return `${sign} R$ ${newAmount.toLocaleString('pt-BR', {minimumFractionDigits: 2})}`;
    },
    async refreshTransactions() {
      this.loader = true;
      const payload = {
        request_payload: [],
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
      this.fields = [
        { key: "petName", label: "PetName" },
        { key: "description", label: "Raça" },
      ]
      if (!this.defaultWorkspace) {
        this.items.forEach((item) => {
          this.separateValues(item.amount);
        });
        const emit = {
          totalOuts: this.totalOuts,
          totalIns: this.totalIns,
        };
        this.$emit("putTotals", emit);
      }
      this.loader = false;
    },
  },
  mounted() {
    this.refreshTransactions();
  },
};
</script>