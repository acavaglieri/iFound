<!-- <template>
  <div class="card">
    <div class="card-body">
      <h4 class="card-title">Endereço</h4>
      <div class="container-fluid">
        <div class="row">
          <div class="col-4 text-right"><strong>Logradouro</strong></div>
          <div class="col-8 text-left">{{logradouroAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Número</strong></div>
          <div class="col-8 text-left">{{numeroAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Bairro</strong></div>
          <div class="col-8 text-left">{{bairroAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Cidade</strong></div>
          <div class="col-8 text-left">{{cidadeAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>CEP</strong></div>
          <div class="col-8 text-left">{{cepAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Estado</strong></div>
          <div class="col-8 text-left">{{estadoAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Referencia</strong></div>
          <div class="col-8 text-left">{{referenciaAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Informação adicional</strong></div>
          <div class="col-8 text-left">{{InformacaoAdicionalAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Latitude</strong></div>
          <div class="col-8 text-left">{{latitudeAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Longitude</strong></div>
          <div class="col-8 text-left">{{longitudeAtual}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {

  name: "plg-account-address",

   props: {
            items_account: {
              type: Array,
              required: true,
            }
          },

  data() {
    return {

      logradouroAtual: '',
      numeroAtual: '',
      bairroAtual: '',
      cidadeAtual: '',
      cepAtual: '',
      estadoAtual: '',
      referenciaAtual: '',
      InformacaoAdicionalAtual: '',
      latitudeAtual: '',
      longitudeAtual: '',

    }
  },

  filters: {
    booleanParaSimNao(dado) {
      return dado == false ? 'Não': dado == true ? 'Sim': 'notBool';
    },
  },

  methods: {

    setup(){

      this.logradouroAtual = this.items_account[0].logradouro;
      this.numeroAtual = this.items_account[0].numero;
      this.bairroAtual = this.items_account[0].bairro;
      this.cidadeAtual = this.items_account[0].cidade;
      this.cepAtual = this.items_account[0].cep;
      this.estadoAtual = this.items_account[0].estado;
      this.referenciaAtual = this.items_account[0].referencia;
      this.InformacaoAdicionalAtual = this.items_account[0].InformacaoAdicional;
      this.latitudeAtual = this.items_account[0].latitude;
      this.longitudeAtual = this.items_account[0].longitude;

      // eslint-disable-next-line
      // console.log(this.items_user[0]);
    },

  },

  mounted() {

    this.setup();
    
  }
}
</script>
-->