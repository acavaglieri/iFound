<!--<template>
  <div class="card">
    <div class="card-body">
      <h4 class="card-title">Detalhes</h4>
      <div class="container-fluid">
        <div class="row">
          <div class="col-4 text-right"><strong>Nome</strong></div>
          <div class="col-8 text-left">{{nomeAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Tipo</strong></div>
          <div class="col-8 text-left">{{tipoAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Conta</strong></div>
          <div class="col-8 text-left">{{contaAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Telefone</strong></div>
          <div class="col-8 text-left">{{telefoneAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Celular</strong></div>
          <div class="col-8 text-left">{{celularAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Email</strong></div>
          <div class="col-8 text-left">{{emailAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>PJ?</strong></div>
          <div class="col-8 text-left">{{pjAtual | booleanParaSimNao}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>CPF/CNPJ</strong></div>
          <div class="col-8 text-left">{{cpfCnpj}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Criado em</strong></div>
          <div class="col-8 text-left">{{criadoEmAtual}}</div>
        </div>
        <div class="row">
          <div class="col-4 text-right"><strong>Alterado em</strong></div>
          <div class="col-8 text-left">{{alteradoEmAtual}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {

  name: "plg-account-address-details",

   props: {
            items_account: {
              type: Array,
              required: true,
            }
          },

  data() {
    return {

      nomeAtual: '',
      tipoAtual: '',
      contaAtual: '',
      telefoneAtual: '',
      celularAtual: '',
      emailAtual: '',
      pjAtual: '',
      cpfCnpj: '',
      criadoEmAtual: '',
      alteradoEmAtual: '',

    }
  },

  filters: {
    booleanParaSimNao(dado) {
      return dado == false ? 'Não': dado == true ? 'Sim': 'notBool';
    },
  },

  methods: {

    setup(){

      this.nomeAtual = this.items_account[0].nomeEndereco;
      this.tipoAtual = this.items_account[0].tipo;
      this.contaAtual = this.items_account[0].IdDoEndereco;
      this.telefoneAtual = this.items_account[0].telefone;
      this.celularAtual = this.items_account[0].celular;
      this.emailAtual = this.items_account[0].email;
      this.pjAtual = this.items_account[0].PJ;
      this.cpfCnpj = this.items_account[0].CpfCnpj;
      this.criadoEmAtual = this.items_account[0].criadoEm;
      this.alteradoEmAtual = this.items_account[0].alteradoEm;

      // eslint-disable-next-line
      // console.log(this.items_user[0]);
    },

  },

  mounted() {

    this.setup();
    
  }
}
</script>