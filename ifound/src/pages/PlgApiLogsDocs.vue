<template>
  <section class="tables">
    <div class="row">
      <div class="col-lg-12 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">documentacao de APIs</h4>
            <b-table striped hover responsive :items="items" :fields="fields">
              <template v-slot:cell(documentacao)="data">
                <a v-if="data.value.documento01.url" :href=data.value.documento01.url class="btn btn-info btn-sm btn-block btn-fw mr-2">{{ data.value.documento01.descricao }}</a>
              </template>
              <template v-slot:cell(exemplo)="data">
                <div v-if="data.value.documento01">
                  <a v-if="data.value.documento01.url" :href=data.value.documento01.url class="btn btn-info btn-sm btn-block btn-fw mr-2">{{ data.value.documento01.descricao }}</a>
                </div>
                <div v-if="data.value.documento02">
                  <a v-if="data.value.documento02.url" :href=data.value.documento02.url class="btn btn-info btn-sm btn-block btn-fw mt-2 mr-2">{{ data.value.documento02.descricao }}</a>
                </div>
                <div v-if="data.value.documento03">
                  <a v-if="data.value.documento03.url" :href=data.value.documento03.url class="btn btn-info btn-sm btn-block btn-fw mt-2 mr-2">{{ data.value.documento03.descricao }}</a>
                </div>
                <div v-if="data.value.documento04">
                  <a v-if="data.value.documento04.url" :href=data.value.documento04.url class="btn btn-info btn-sm btn-block btn-fw mt-2 mr-2">{{ data.value.documento04.descricao }}</a>
                </div>
              </template>
            </b-table>
          </div>
        </div>
      </div>
      <div class="col-lg-12 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">documentacao APIs Customizadas</h4>
            <p class="card-description">
              <code>Utilização desse modelo deve ser evitada, existe apenas para legado.</code>
            </p>
            <b-table striped hover responsive :items="items2" :fields="fields">
              <template v-slot:cell(documentacao)="data">
                <a v-if="data.value.documento01.url" :href=data.value.documento01.url class="btn btn-info btn-sm btn-block btn-fw mr-2">{{ data.value.documento01.descricao }}</a>
              </template>
              <template v-slot:cell(exemplo)="data">
                <div v-if="data.value.documento01">
                  <a v-if="data.value.documento01.url" :href=data.value.documento01.url class="btn btn-info btn-sm btn-block btn-fw mr-2">{{ data.value.documento01.descricao }}</a>
                </div>
                <div v-if="data.value.documento02">
                  <a v-if="data.value.documento02.url" :href=data.value.documento02.url class="btn btn-info btn-sm btn-block btn-fw mt-2 mr-2">{{ data.value.documento02.descricao }}</a>
                </div>
                <div v-if="data.value.documento03">
                  <a v-if="data.value.documento03.url" :href=data.value.documento03.url class="btn btn-info btn-sm btn-block btn-fw mt-2 mr-2">{{ data.value.documento03.descricao }}</a>
                </div>
                <div v-if="data.value.documento04">
                  <a v-if="data.value.documento04.url" :href=data.value.documento04.url class="btn btn-info btn-sm btn-block btn-fw mt-2 mr-2">{{ data.value.documento04.descricao }}</a>
                </div>
              </template>
            </b-table>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
const items = [
  {
    api: "POST /api/v1/lots/complex",
    descricao: "Cria vários pedidos a partir da mesma origem em lote, usando o máximo de campos possíveis. (Compatível com Intelipost)",
    documentacao:
      {
        documento01:
          {
            descricao: "api_doc_POST_lots_complex.pdf",
            url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_complex-fbe00316c9179e1efbd04d9cf9cc329c9b2770fe2fa959dfc5799a31b01799fe.pdf"
          },
      },
    exemplo:
    {
      documento01:
        {
          descricao: "api_doc_POST_lots_complex_request.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_complex_request-8cb369c6b3deb528295b3f8c5dffba70d80ed94944b3b09835a1b399770fb14f.json"
        },
    },
  },
  {
    api: "POST /api/v1/lots/simple",
    descricao: "Cria vários pedidos a partir da mesma origem em lote, usando o mínimo de campos possíveis. (Compatível com Ezconet)",
    documentacao: {
        documento01:
          {
            descricao: "",
            url: ""
          },
      },
    exemplo:
    {
      documento01:
        {
          descricao: "api_doc_POST_lots_simple_request.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_simple_request-f0f7fbe1d59b66fe7072bfd0d7f24dfd99e8612d2c45aca1d5c27e53ca5a19a2.json"
        },
      documento02:
        {
          descricao: "api_doc_POST_lots_simple_response.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_simple_response-7023525f19c9821862a6a0cf25a478d8a43d63bd802fd2f5e7127fb2605e4184.json"
        },
    },
  },
  {
    api: "POST /api/v1/lots/history",
    descricao: "Mostra o histórico de todos os pedidos de um lote. (Compatível com Ezconet)",
    documentacao: {
        documento01:
          {
            descricao: "",
            url: ""
          },
      },
    exemplo:
    {
      documento01:
        {
          descricao: "api_doc_POST_lots_history_request.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_history_request-81a055a8bced8b9823f4601e9db043e005facf83a1347695f3ab86b01f602447.json"
        },
      documento02:
        {
          descricao: "api_doc_POST_lots_history_response.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_history_response-a1476034fc2d12fd23c11ef5ccd5b27de0efd0d7d3074762cd50db42a662cd0d.json"
        },
    },
  },
];

const items2 = [
  {
    api: "POST /api/v1/lots/intelipost_tim_lote",
    descricao: "Específica: conta TIM para entrega em lote. Cria vários pedidos a partir da mesma origem em lote, usando o máximo de campos possíveis. (Compatível com Intelipost)",
    documentacao:
      {
        documento01:
          {
            descricao: "api_doc_POST_lots_complex.pdf",
            url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_complex-fbe00316c9179e1efbd04d9cf9cc329c9b2770fe2fa959dfc5799a31b01799fe.pdf"
          },
      },
    exemplo:
    {
      documento01:
        {
          descricao: "api_doc_POST_lots_complex_request.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_complex_request-8cb369c6b3deb528295b3f8c5dffba70d80ed94944b3b09835a1b399770fb14f.json"
        },
    },
  },
  {
    api: "POST /api/v1/lots/ezconet_oi_lote",
    descricao: "Específica: conta OI para entrega em lote. Cria vários pedidos a partir da mesma origem em lote, usando o mínimo de campos possíveis. (Compatível com Ezconet)",
    documentacao: {
        documento01:
          {
            descricao: "",
            url: ""
          },
      },
    exemplo:
    {
      documento01:
        {
          descricao: "api_doc_POST_lots_simple_request.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_simple_request-f0f7fbe1d59b66fe7072bfd0d7f24dfd99e8612d2c45aca1d5c27e53ca5a19a2.json"
        },
      documento02:
        {
          descricao: "api_doc_POST_lots_simple_response.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_simple_response-7023525f19c9821862a6a0cf25a478d8a43d63bd802fd2f5e7127fb2605e4184.json"
        },
    },
  },
  {
    api: "POST /api/v1/lots/ezconet_oi_cancela",
    descricao: "Específica: conta OI para cancelar pedidos de lote. Não existe cancelamento então na prática coloca em estoque. (Compatível com Ezconet)",
    documentacao: {
        documento01:
          {
            descricao: "",
            url: ""
          },
      },
    exemplo:
    {
      documento01:
        {
          descricao: "api_doc_POST_ezconet_oi_cancela_request.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_ezconet_oi_cancela_request-cbe4ea52f204dc0d4818df2f317f40e11833a4b942fcf296cad8d30235708d5a.json"
        },
      documento02:
        {
          descricao: "api_doc_POST_ezconet_oi_cancela_response.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_ezconet_oi_cancela_response-2dbd6c130969ce17056c05e39e3f7149991359139da0aff36dbba72bea6e9cbd.json"
        },
    },
  },
  {
    api: "POST /api/v1/lots/ezconet_oi_status",
    descricao: "Mostra o status de um pedido ou todos os lote. (Compatível com Ezconet)	",
    documentacao: {
        documento01:
          {
            descricao: "",
            url: ""
          },
      },
    exemplo:
    {
      documento01:
        {
          descricao: "api_doc_POST_lots_ezconet_oi_status_request_by_lot.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_ezconet_oi_status_request_by_lot-e81b4cea9ebd9d4c0fcca21ac5a3a1c001d84ec4caa3bd97dc340ce7bb60f9c3.json"
        },
      documento02:
        {
          descricao: "api_doc_POST_lots_ezconet_oi_status_response_by_lot.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_ezconet_oi_status_response_by_lot-c595c52d5758f4edd32e1b977e57027e674af5e0244b5844b29fac8198d98e2e.json"
        },
      documento03:
        {
          descricao: "api_doc_POST_lots_ezconet_oi_status_request_by_order.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_ezconet_oi_status_request_by_order-dab89d7b18fd77eda70a22f2c8fccaa1dcd340083b1a16130730a390bd533559.json"
        },
      documento04:
        {
          descricao: "api_doc_POST_lots_ezconet_oi_status_response_by_order.json",
          url: "https://portalviareversahml.csssolutions.com.br/assets/api_doc_POST_lots_ezconet_oi_status_response_by_order-5cde69116d6a2539dfa5023ca9e07dd90d17884728ed95cc6ffd86b7d7802750.json"
        },
    },
  },
];

const fields= 
[
  { key: "api", label: "API", sortable: true },
  { key: "descricao", label: "Descrição", sortable: true },
  { key: "documentacao", label: "Documentação", sortable: true },
  { key: "exemplo", label: "Exemplo", sortable: true },
];

export default {

  name: 'plg-api-logs-docs',
  
data() {
    return {
      items: items,
      items2: items2,
      fields: fields,
    };
  }
};
</script>