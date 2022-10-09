<template>
  <div>

    <!--crud = read -->
    <div class="row" v-if="crud=='read'">
      <!--DETALHES-->
      <div class="col-xl-6 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Detalhes</h4>
            <div class="container-fluid">
              <div class="row">
                <div class="col-5 text-right"><strong>Nome</strong></div>
                <div class="col-7 text-left">{{items_account_local.nome}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Conta</strong></div>
                <div class="col-7 text-left">{{items_account_local.conta}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Telefone</strong></div>
                <div class="col-7 text-left">{{items_account_local.telefone}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Celular</strong></div>
                <div class="col-7 text-left">{{items_account_local.celular}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Email</strong></div>
                <div class="col-7 text-left">{{items_account_local.email}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>PJ?</strong></div>
                <div class="col-7 text-left">{{items_account_local.PJ | booleanParaSimNao}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>CPF/CNPJ</strong></div>
                <div class="col-7 text-left">{{items_account_local.CpfCnpj}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Criado em</strong></div>
                <div class="col-7 text-left">{{items_account_local.criadoEm}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Alterado em</strong></div>
                <div class="col-7 text-left">{{items_account_local.alteradoEm}}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--DADOS BANCÁRIOS--> <!--
      <div class="col-xl-6 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Dados Bancários</h4>
            <div class="container-fluid">
              <div class="row">
                <div class="col-5 text-right"><strong>Banco</strong></div>
                <div class="col-7 text-left">{{items_account_local.banco}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Agência</strong></div>
                <div class="col-7 text-left">{{items_account_local.agencia}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Díg. Agência</strong></div>
                <div class="col-7 text-left">{{items_account_local.agenciaDigito}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Conta</strong></div>
                <div class="col-7 text-left">{{items_account_local.conta}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Díg. Conta</strong></div>
                <div class="col-7 text-left">{{items_account_local.contaDigito}}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      --> 
      <!--ENDEREÇO DA CONTA--> <!--
      <div class="col-xl-6 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Endereço</h4>
            <div class="container-fluid">
              <div class="row">
                <div class="col-5 text-right"><strong>Logradouro</strong></div>
                <div class="col-7 text-left">{{items_account_local.logradouro}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Número</strong></div>
                <div class="col-7 text-left">{{items_account_local.numero}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Bairro</strong></div>
                <div class="col-7 text-left">{{items_account_local.bairro}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Cidade</strong></div>
                <div class="col-7 text-left">{{items_account_local.cidade}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>CEP</strong></div>
                <div class="col-7 text-left">{{items_account_local.cep}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Estado</strong></div>
                <div class="col-7 text-left">{{items_account_local.estado}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Referencia</strong></div>
                <div class="col-7 text-left">{{items_account_local.referencia}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Informação adicional</strong></div>
                <div class="col-7 text-left">{{items_account_local.InformacaoAdicional}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Latitude</strong></div>
                <div class="col-7 text-left">{{items_account_local.latitude}}</div>
              </div>
              <div class="row">
                <div class="col-5 text-right"><strong>Longitude</strong></div>
                <div class="col-7 text-left">{{items_account_local.longitude}}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
      --> 
      <!--SERVIÇOS--> <!--
      <div class="col-xl-6 grid-margin stretch-card">
        <plg-account-services :items_account = items_account_local></plg-account-services>
      </div> --> 
    </div>

    <!--crud = create ou update --> 
    <div  v-if="crud=='create' || crud=='update'" class="card">
      <div class="card-body">
        <form @submit.prevent="onSubmit" @reset.prevent="onReset" class="forms-sample mt-3">
          <div class="row">
            <!--DETALHES-->
            <div class="col-xl-6 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Detalhes
                  </h4>
                  <div class="container-fluid">
                    <b-form-group label="Nome" label-for="input1">
                      <b-form-input v-model="items_account_local.nome" type="text" id="input1" placeholder="Nome" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Email" label-for="input2">
                      <b-form-input v-model="items_account_local.email" type="text" id="input2" placeholder="Email" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Telefone" label-for="input3">
                      <b-form-input v-model="items_account_local.telefone" type="text" id="input3" placeholder="Telefone" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Celular" label-for="input4">
                      <b-form-input v-model="items_account_local.celular" type="text" id="input4" placeholder="Celular" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Email" label-for="input5">
                      <b-form-input v-model="items_account_local.email" type="text" id="input5" placeholder="Email" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-checkbox
                      id="checkbox-1"
                      v-model="items_account_local.PJ"
                      name="checkbox-1"
                      value=true
                      unchecked-value=false
                      class="mb-2"
                    >PJ?
                    </b-form-checkbox>
                    <b-form-group label="CPF/CNPJ" label-for="input6">
                      <b-form-input v-model="items_account_local.CpfCnpj" type="text" id="input6" placeholder="CPF/CNPJ" size="sm"></b-form-input>
                    </b-form-group>
                    <div v-if="crud=='update'" class="row mt-3">
                      <div class="col-12 text-left">Criado em {{items_account_local.criadoEm}}</div>
                    </div>
                    <div v-if="crud=='update'" class="row mt-3">
                      <div class="col-12 text-left">Alterado em {{items_account_local.alteradoEm}}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--DADOS BANCÁRIOS--> <!--
            <div class="col-xl-6 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Dados Bancários
                  </h4>
                  <div class="container-fluid">
                    <b-form-group label="Banco" label-for="input7">
                      <b-form-select v-model="bank_selected"  :options="banks"  size="sm"/>
                    </b-form-group>
                    <b-form-group label="Agência" label-for="input8">
                      <b-form-input v-model="items_account_local.agencia" type="number" id="input8" placeholder="Agência" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Díg. Agência" label-for="input9">
                      <b-form-input v-model="items_account_local.agenciaDigito" type="number" id="input9" placeholder="Díg. Agência" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Conta" label-for="input10">
                      <b-form-input v-model="items_account_local.conta" type="number" id="input10" placeholder="Conta" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Díg. Conta" >
                      <b-form-input v-model="items_account_local.contaDigito" type="text" placeholder="Díg. Conta" size="sm"></b-form-input>
                    </b-form-group>
                  </div>
                </div>
              </div>
            </div>
            --> 
            <!--ENDEREÇO DA CONTA--> <!--
            <div class="col-xl-6 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Endereço da Conta
                  </h4>
                  <div class="container-fluid">
                    <b-form-group label="Logradouro" label-for="input12">
                      <b-form-input v-model="items_account_local.logradouro" type="text" id="input12" placeholder="Logradouro" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Número" label-for="input13">
                      <b-form-input v-model="items_account_local.numero" type="text" id="input13" placeholder="Número" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Bairro" label-for="input14">
                      <b-form-input v-model="items_account_local.bairro" type="text" id="input14" placeholder="Bairro" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Cidade" label-for="input15">
                      <b-form-input v-model="items_account_local.cidade" type="text" id="input15" placeholder="Cidade" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="CEP" label-for="input16">
                      <b-form-input v-model="items_account_local.cep" type="text" id="input16" placeholder="CEP" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Estado" label-for="input17">
                      <b-form-input v-model="items_account_local.estado" type="text" id="input17" placeholder="Estado" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Referencia" label-for="input18">
                      <b-form-input v-model="items_account_local.referencia" type="text" id="input18" placeholder="Referencia" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Informação adicional" label-for="input19">
                      <b-form-input v-model="items_account_local.InformacaoAdicional" type="text" id="input19" placeholder="Informação adicional" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Latitude" label-for="input20">
                      <b-form-input v-model="items_account_local.latitude" type="text" id="input20" placeholder="Latitude" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Longitude" label-for="input21">
                      <b-form-input v-model="items_account_local.longitude" type="text" id="input21" placeholder="Longitude" size="sm"></b-form-input>
                    </b-form-group>
                  </div>
                </div>
              </div>
            </div>
            --> 
            <!--INTELLIPOST--> <!--
            <div class="col-xl-6 grid-margin stretch-card">
              <div class="card">
                <div class="card-body">
                  <h4 class="card-title">Intellipost
                  </h4>
                  <div class="container-fluid">
                    <b-form-checkbox
                      id="checkbox-2"
                      v-model="items_account_local.enviaOcorrênciasParaIntelipost"
                      name="checkbox-2"
                      value=true
                      unchecked-value=false
                      class="mb-2"
                    >Envia Ocorrências para Intelipost
                    </b-form-checkbox>
                    <b-form-group label="Logistic Provider" label-for="input22">
                      <b-form-input v-model="items_account_local.logisticProvider" type="text" id="input22" placeholder="Logistic Provider" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Logistic Provider ID" label-for="input23">
                      <b-form-input v-model="items_account_local.logisticProviderID" type="text" id="input23" placeholder="Logistic Provider ID" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Logistic Provider Federal Tax ID" label-for="input24">
                      <b-form-input v-model="items_account_local.logisticProviderFederalTaxID" type="text" id="input24" placeholder="Logistic Provider Federal Tax ID" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Shipper" label-for="input25">
                      <b-form-input v-model="items_account_local.shipper" type="text" id="input25" placeholder="Shipper" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Shipper Federal Tax ID" label-for="input26">
                      <b-form-input v-model="items_account_local.shipperFederalTaxID" type="text" id="input26" placeholder="Shipper Federal Tax ID" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Logistic Provider API KEY PRD" label-for="input27">
                      <b-form-input v-model="items_account_local.logisticProviderApiKeyPRD" type="text" id="input27" placeholder="Logistic Provider API KEY PRD" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Logistic Provider API KEY HML" label-for="input28">
                      <b-form-input v-model="items_account_local.logisticProviderApiKeyHML" type="text" id="input28" placeholder="Logistic Provider API KEY HML" size="sm"></b-form-input>
                    </b-form-group>
                    <b-form-group label="Intelipost platform" label-for="input29">
                      <b-form-input v-model="items_account_local.plataformaIntelipost" type="text" id="input29" placeholder="Intelipost platform" size="sm"></b-form-input>
                    </b-form-group>
                  </div>
                </div>
              </div>
            </div> --> 
          </div> 

          <div class="row">
            <div class="col-12">
              <b-button type="submit" variant="danger" class="mb-2 mr-2 btn-sm"><i class="fa fa-check" v-b-tooltip.html.top title="Atualizar"></i></b-button>
              <b-button type="reset" variant="light" class="mb-2 btn-sm"><i class="fa fa-eraser" v-b-tooltip.html.top title="Limpar"></i></b-button>
            </div>
          </div>
          
        </form>
      </div>
    </div>

  </div>
</template>

<script>
/*
const banks = [
  {value:'246',text: 'Banco ABC Brasil S.A.'},
  {value:'075',text: 'Banco ABN AMRO S.A.'},
  {value:'121',text: 'Banco Agibank S.A.'},
  {value:'025',text: 'Banco Alfa S.A.'},
  {value:'641',text: 'Banco Alvorada S.A.'},
  {value:'065',text: 'Banco Andbank (Brasil) S.A.'},
  {value:'096',text: 'Banco B3 S.A.'},
  {value:'024',text: 'Banco BANDEPE S.A.'},
  {value:'318',text: 'Banco BMG S.A.'},
  {value:'752',text: 'Banco BNP Paribas Brasil S.A.'},
  {value:'107',text: 'Banco BOCOM BBM S.A.'},
  {value:'063',text: 'Banco Bradescard S.A.'},
  {value:'036',text: 'Banco Bradesco BBI S.A.'},
  {value:'204',text: 'Banco Bradesco Cartões S.A.'},
  {value:'394',text: 'Banco Bradesco Financiamentos S.A.'},
  {value:'237',text: 'Banco Bradesco S.A.'},
  {value:'218',text: 'Banco BS2 S.A.'},
  {value:'208',text: 'Banco BTG Pactual S.A.'},
  {value:'473',text: 'Banco Caixa Geral - Brasil S.A.'},
  {value:'040',text: 'Banco Cargill S.A.'},
  {value:'739',text: 'Banco Cetelem S.A.'},
  {value:'233',text: 'Banco Cifra S.A.'},
  {value:'745',text: 'Banco Citibank S.A.'},
  {value:'756',text: 'Banco Cooperativo do Brasil S.A. - BANCOOB'},
  {value:'748',text: 'Banco Cooperativo Sicredi S.A.'},
  {value:'222',text: 'Banco Credit Agricole Brasil S.A.'},
  {value:'505',text: 'Banco Credit Suisse (Brasil) S.A.'},
  {value:'003',text: 'Banco da Amazônia S.A.'},
  {value:'083',text: 'Banco da China Brasil S.A.'},
  {value:'707',text: 'Banco Daycoval S.A.'},
  {value:'001',text: 'Banco do Brasil S.A.'},
  {value:'047',text: 'Banco do Estado de Sergipe S.A.'},
  {value:'037',text: 'Banco do Estado do Pará S.A.'},
  {value:'041',text: 'Banco do Estado do Rio Grande do Sul S.A.'},
  {value:'004',text: 'Banco do Nordeste do Brasil S.A.'},
  {value:'265',text: 'Banco Fator S.A.'},
  {value:'224',text: 'Banco Fibra S.A.'},
  {value:'626',text: 'Banco Ficsa S.A.'},
  {value:'094',text: 'Banco Finaxis S.A.'},
  {value:'612',text: 'Banco Guanabara S.A.'},
  {value:'012',text: 'Banco Inbursa S.A.'},
  {value:'604',text: 'Banco Industrial do Brasil S.A.'},
  {value:'653',text: 'Banco Indusval S.A.'},
  {value:'077',text: 'Banco Inter S.A.'},
  {value:'249',text: 'Banco Investcred Unibanco S.A.'},
  {value:'184',text: 'Banco Itaú BBA S.A.'},
  {value:'029',text: 'Banco Itaú Consignado S.A.'},
  {value:'479',text: 'Banco ItauBank S.A'},
  {value:'376',text: 'Banco J. P. Morgan S.A.'},
  {value:'074',text: 'Banco J. Safra S.A.'},
  {value:'217',text: 'Banco John Deere S.A.'},
  {value:'600',text: 'Banco Luso Brasileiro S.A.'},
  {value:'389',text: 'Banco Mercantil do Brasil S.A.'},
  {value:'370',text: 'Banco Mizuho do Brasil S.A.'},
  {value:'746',text: 'Banco Modal S.A.'},
  {value:'456',text: 'Banco MUFG Brasil S.A.'},
  {value:'169',text: 'Banco Olé Bonsucesso Consignado S.A.'},
  {value:'212',text: 'Banco Original S.A.'},
  {value:'623',text: 'Banco PAN S.A.'},
  {value:'611',text: 'Banco Paulista S.A.'},
  {value:'643',text: 'Banco Pine S.A.'},
  {value:'747',text: 'Banco Rabobank International Brasil S.A.'},
  {value:'633',text: 'Banco Rendimento S.A.'},
  {value:'120',text: 'Banco Rodobens S.A.'},
  {value:'422',text: 'Banco Safra S.A.'},
  {value:'033',text: 'Banco Santander (Brasil) S.A.'},
  {value:'743',text: 'Banco Semear S.A.'},
  {value:'630',text: 'Banco Smartbank S.A.'},
  {value:'366',text: 'Banco Société Générale Brasil S.A.'},
  {value:'464',text: 'Banco Sumitomo Mitsui Brasileiro S.A.'},
  {value:'082',text: 'Banco Topázio S.A.'},
  {value:'634',text: 'Banco Triângulo S.A.'},
  {value:'655',text: 'Banco Votorantim S.A.'},
  {value:'610',text: 'Banco VR S.A.'},
  {value:'119',text: 'Banco Western Union do Brasil S.A.'},
  {value:'102',text: 'Banco XP S.A.'},
  {value:'081',text: 'BancoSeguro S.A.'},
  {value:'021',text: 'BANESTES S.A. Banco do Estado do Espírito Santo'},
  {value:'755',text: 'Bank of America Merrill Lynch Banco Múltiplo S.A.'},
  {value:'250',text: 'BCV - Banco de Crédito e Varejo S.A.'},
  {value:'144',text: 'BEXS Banco de Câmbio S.A.'},
  {value:'017',text: 'BNY Mellon Banco S.A.'},
  {value:'070',text: 'BRB - Banco de Brasília S.A.'},
  {value:'104',text: 'Caixa Econômica Federal'},
  {value:'320',text: 'China Construction Bank (Brasil) Banco Múltiplo S.A.'},
  {value:'477',text: 'Citibank N.A.'},
  {value:'487',text: 'Deutsche Bank S.A. - Banco Alemão'},
  {value:'064',text: 'Goldman Sachs do Brasil Banco Múltiplo S.A.'},
  {value:'062',text: 'Hipercard Banco Múltiplo S.A.'},
  {value:'269',text: 'HSBC Brasil S.A. - Banco de Investimento'},
  {value:'492',text: 'ING Bank N.V.'},
  {value:'652',text: 'Itaú Unibanco Holding S.A.'},
  {value:'341',text: 'Itaú Unibanco S.A.'},
  {value:'488',text: 'JPMorgan Chase Bank, National Association'},
  {value:'399',text: 'Kirton Bank S.A. - Banco Múltiplo'},
  {value:'128',text: 'MS Bank S.A. Banco de Câmbio'},
  {value:'254',text: 'Paraná Banco S.A.'},
  {value:'125',text: 'Plural S.A. - Banco Múltiplo'},
  {value:'751',text: 'Scotiabank Brasil S.A. Banco Múltiplo'},
  {value:'095',text: 'Travelex Banco de Câmbio S.A.'},
  {value:'129',text: 'UBS Brasil Banco de Investimento S.A.'},
]
*/
//import PlgAccountServices from './PlgAccountServices.vue';

export default {

  name: "plg-account-details",

  components: {
    //PlgAccountServices,
  },

   props: {
            items_account: {
              type: Array,
              required: true,
            },
            crud: {
              type: String,
              required: true,
            }
          },

  data() {
    return {

      items_account_local: [],
      
      //banks: banks,
      //bank_selected: '104'

    }
  },

  filters: {
    booleanParaSimNao(dado) {
      return dado == false ? 'Não': dado == true ? 'Sim': 'notBool';
    },
  },

  methods: {

    onSubmit(){

      const actualDate = new Date(Date.now());
      if(this.crud=='create'){this.items_account_local.criadoEm = actualDate;}
      this.items_account_local.alteradoEm = actualDate;
      alert("Vai fazer validações e ligar essa info ao banco de dados!")

    },

    onReset(){

      this.resetItemsAccountLocal();

    },

    resetItemsAccountLocal(){

      this.items_account_local={
        'arquivado': false,
        'tipo': '',
        'nome': '',
        'email': '',
        'telefone': '',
        'celular': '',
        'PJ': false,
        'CpfCnpj': '',
        'logradouro': '',
        'numero': '',
        'bairro': '',
        'cidade': '',
        'cep': '',
        'estado': '',
        'pais': '',
        'referencia': '',
        'InformacaoAdicional': '',
        'latitude': '',
        'longitude': '',
        'banco': '',
        'agencia': '',
        'agenciaDigito': '',
        'conta': '',
        'contaDigito': '',
        'enviaOcorrênciasParaIntelipost': '',
        'logisticProvider': '',
        'logisticProviderID': '',
        'logisticProviderFederalTaxID': '',
        'shipper': '',
        'shipperFederalTaxID': '',
        'logisticProviderApiKeyPRD': '',
        'logisticProviderApiKeyHML': '',
        'plataformaIntelipost': '',
      };

    },

    setup(crud){

      if(crud!='create'){
        
        this.items_account_local={
          'IdDaConta': this.items_account[0].IdDaConta,
          'arquivado': this.items_account[0].arquivado,
          'tipo': this.items_account[0].tipo,
          'nome': this.items_account[0].nome,
          'email': this.items_account[0].email,
          'telefone': this.items_account[0].telefone,
          'celular': this.items_account[0].celular,
          'PJ': this.items_account[0].PJ,
          'CpfCnpj': this.items_account[0].CpfCnpj,
          'logradouro': this.items_account[0].logradouro,
          'numero': this.items_account[0].numero,
          'bairro': this.items_account[0].bairro,
          'cidade': this.items_account[0].cidade,
          'cep': this.items_account[0].cep,
          'estado': this.items_account[0].estado,
          'pais': this.items_account[0].pais,
          'referencia': this.items_account[0].referencia,
          'InformacaoAdicional': this.items_account[0].InformacaoAdicional,
          'latitude': this.items_account[0].latitude,
          'longitude': this.items_account[0].longitude,
          'banco': this.items_account[0].banco,
          'agencia': this.items_account[0].agencia,
          'agenciaDigito': this.items_account[0].agenciaDigito,
          'conta': this.items_account[0].conta,
          'contaDigito': this.items_account[0].contaDigito,
          'criadoEm': this.items_account[0].criadoEm,
          'alteradoEm': this.items_account[0].alteradoEm,
          'enviaOcorrênciasParaIntelipost': this.items_account[0].enviaOcorrênciasParaIntelipost,
          'logisticProvider': this.items_account[0].logisticProvider,
          'logisticProviderID': this.items_account[0].logisticProviderID,
          'logisticProviderFederalTaxID': this.items_account[0].logisticProviderFederalTaxID,
          'shipper': this.items_account[0].shipper,
          'shipperFederalTaxID': this.items_account[0].shipperFederalTaxID,
          'logisticProviderApiKeyPRD': this.items_account[0].logisticProviderApiKeyPRD,
          'logisticProviderApiKeyHML': this.items_account[0].logisticProviderApiKeyHML,
          'plataformaIntelipost': this.items_account[0].plataformaIntelipost,
        };
      }else{
        this.resetItemsAccountLocal();
      }

    },

  },

  mounted() {

    this.setup(this.crud);
    
  }
}
</script>