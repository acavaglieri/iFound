<template>
  <div>
    <section>
      <div class="row">
        <div class="col-12">
          <div class="card border rounded">
            <div class="card-body">
              <b-row>
                <b-col lg="11">
                  <h3 class="my-3 mx-3 text-center">Cadastro concluido</h3>
                </b-col>
                <b-col lg="1" class="py-3 d-none d-lg-block">
                  <router-link :to="{ name: 'home' }" style="color: black;">
                    <h3><i class="mdi mdi-arrow-left"></i></h3>
                  </router-link>
                </b-col>
              </b-row>
              <hr>
              <b-row>
                <b-col>
                  <div class="text-center">
                    <h4>
                      Quantia Cobrada: R$ {{ amount }}</h4>
                  </div>
                </b-col>
              </b-row>
              <hr>
              <b-row align-v="center">
                <b-col lg="6" cols="12">
                  <div class="text-center">
                    <h4>
                      Código da Transação:
                    </h4>
                    <input v-model="brCode" class="form-control-plaintext" readonly>
                  </div>
                </b-col>
                <b-col lg="6" cols="12">
                  <br>
                  <div class="text-center">
                    <h4>
                      QRCode:
                    </h4>
                    <vue-qrcode :value="brCode" :options="{ width: 200 }"></vue-qrcode>
                  </div>
                </b-col>
              </b-row>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import VueQrcode from '@chenfengyuan/vue-qrcode';


export default {
  name: "PlgPixChargeInfo",
  props: {
    amount: String,
    brCode: String,
  },
  components: {
    VueQrcode,
  },
}
</script>