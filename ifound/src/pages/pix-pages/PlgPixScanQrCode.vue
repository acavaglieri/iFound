<template>
  <div>
    <PlgBankServicesApi ref="PlgBankServicesApi"></PlgBankServicesApi>
    <Toasts ref="Toasts"></Toasts>
   
    <b-row>
      <b-col cols="0" lg="4" class="mt-5">
        <div class="text-center d-none d-lg-inline mt-5 ml-5">
          <h1>Coloque o código no leitor</h1>
          <h4 class="text-muted">Você pode querer usar um celular para isso.</h4>
          <div class="icon is-large mt-5">
            <i class="mdi mdi-qrcode-scan mdi-48px"></i>
          </div>
        </div>
        <div class="d-block d-lg-none">
          <h4 class="text-muted text-center">Use o celular na horizontal para melhor leitura.</h4>
        </div>
      </b-col>
      <b-col cols="12" lg="7" class="d-lg-inline mt-3">
        <div class="my-5">
          <StreamBarcodeReader
            @decode="(a) => onDecode(a)"
            @loaded="() => onLoaded()"
          ></StreamBarcodeReader>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
//import customValidators from "../plugins/vuelidateValidators";
import PlgBankServicesApi from '../../apis/PlgBankServicesApi.vue';
import { StreamBarcodeReader } from "vue-barcode-reader";
import Toasts from '../../components/Toasts.vue';


export default {
  data() {
    return {
      code: null,
      submitted: false,
      isLoading: false,
    }
  },
  components: {
    PlgBankServicesApi,
    Toasts,
    StreamBarcodeReader,
  },
  methods: {
    onDecode(a) {
      this.code = a;
      if (this.id) clearTimeout(this.id);
      this.id = setTimeout(() => {
        if (this.code === a) {
          this.code = "";
        }
      }, 5000);
    },
    onLoaded() {
      console.log("load");
    },
  },
  watch: {
    code() {
      this.$router.push({name: 'pix_preview_payment', params: {brCode: this.code}})
    }
  }
}
</script>