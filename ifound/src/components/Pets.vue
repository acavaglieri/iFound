<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-12">
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
              <th scope="col">Vacinado contra raiva?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(pet, index) in pets" :key="index">
              <td>{{ pet.nome }}</td>
              <td>{{ pet.raca }}</td>   
              <td>
                <span v-if="pet.vacinado">Yes</span>
                <span v-else>No</span>
              </td>
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
            nome="Add a new pet"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-nome-group"
                    label="Nome:"
                    label-for="form-nome-input">
          <b-form-input id="form-nome-input"
                        type="text"
                        v-model="addPetForm.nome"
                        required
                        placeholder="Enter nome">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-raca-group"
                      label="Raça:"
                      label-for="form-raca-input">
            <b-form-input id="form-raca-input"
                          type="text"
                          v-model="addPetForm.raca"
                          required
                          placeholder="Enter raça">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-vacinado-group">
          <b-form-checkbox-group v-model="addPetForm.vacinado" id="form-checks">
            <b-form-checkbox value="true">Vacinado?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  <b-modal ref="editPetModal"
       id="pet-update-modal"
       nome="Update"
       hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-nome-edit-group"
                      label="Nome:"
                      label-for="form-nome-edit-input">
          <b-form-input id="form-nome-edit-input"
                          type="text"
                          v-model="editForm.nome"
                          required
                          placeholder="Enter nome">
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
          <b-form-group id="form-vacinado-edit-group">
          <b-form-checkbox-group v-model="editForm.vacinado" id="form-checks">
              <b-form-checkbox value="true">Vacinado?</b-form-checkbox>
          </b-form-checkbox-group>
          </b-form-group>
          <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
          </b-button-group>
      </b-form>
  </b-modal>


  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      pets: [],
      addPetForm: {
        nome: '',
        raca: '',
        vacinado: [],
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
      //this.addPetForm.nome = '';
      //this.addPetForm.raca = '';
      //this.addPetForm.vacinado = [];
      this.editForm.id = '';
      this.editForm.nome = '';
      this.editForm.raca = '';
      this.editForm.vacinado = [];
    },
    editPet(pet) {
      this.editForm = pet;
    },
    editForm: {
      id: '',
      nome: '',
      raca: '',
      vacinado: [],
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addPetModal.hide();
      let vacinado = false;
      if (this.addPetForm.vacinado[0]) vacinado = true;
      const payload = {
        nome: this.addPetForm.nome,
        raca: this.addPetForm.raca,
        vacinado, // property shorthand
      };
      this.addPet(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editPetModal.hide();
      let vacinado = false;
      if (this.editForm.vacinado[0]) vacinado = true;
      const payload = {
          nome: this.editForm.nome,
          raca: this.editForm.raca,
          vacinado,
      };
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