<template>
  <section class="tables">
    <div class="row">
      <div class="col-lg-12 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">
            <h4 class="card-title">Logs De Api</h4>
            <b-table
              :items="items"
              id="table-list"
              responsive
              :per-page="perPage"
              :current-page="currentPage"
              :fields="fields"
              :sort-by.sync="sortBy"
              :sort-desc.sync="sortDesc"
              small
            >
              <template v-slot:cell(acoes)>
                <router-link class="btn btn-warning btn-sm mr-2 btn-fw" to="" v-b-tooltip.html.left title="Abrir">
                  * <i class="fa fa-search"></i>
                </router-link>
              </template>
            </b-table>

            <div class="row">
              <div class="col" align="left">
                <h6 class="col-12">
                  <small class="text-muted ml-2 mr-2">Itens por Página</small>
                  <div class="btn-group" role="group" aria-label="Basic example">
                    <button type="button" class="btn btn-outline-primary btn-sm">10</button>
                    <button type="button" class="btn btn-outline-primary btn-sm">25</button>
                    <button type="button" class="btn btn-outline-primary btn-sm">50</button>
                    <button type="button" class="btn btn-outline-primary btn-sm">100</button>
                  </div>
                </h6>
              </div>
              <div class="col">
                <b-pagination
                  v-model="currentPage"
                  :total-rows="rows"
                  :per-page="perPage"
                  aria-controls="table-list"
                  align="center"
                ></b-pagination>
              </div>
              <div class="col" align="right">
                <b-btn variant="primary" class="btn btn-success btn-rounded btn-icon btn-sm text-white mr-3" v-b-tooltip.html.left title="Exportar para Excel">
                  <i class="fa fa-download"></i>
                </b-btn>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div></div>
  </section>
</template>
<script>

const fields=
[
  { key: "chamadoRecebido", label: "Chamado | Recebido", sortable: true },
  { key: "endereçoDaAPI", label: "Endereço da API", sortable: true },
  { key: "iniciadoEm", label: "Iniciado em", sortable: true },
  { key: "finalizadoEm", label: "Finalizado em", sortable: true },
  { key: "acoes", label: "Ações", sortable: false }
];

const items=
[
  {
    logDeAPI: -839,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53191202421421013795551370001598131454559772\".\"invoice_series\":\"137\".\"invoice_number\":\"000159813\".\"tracking_code\":900545.\"order_number\":\"000159813-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:24:22.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=d2c7e83c-882d-41fd-8b8c-8348ba9beb32\".\"processing_hash\":\"d2c7e83c-882d-41fd-8b8c-8348ba9beb32\"}.\"time\":\"123.6 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"d2c7e83c-882d-41fd-8b8c-8348ba9beb32\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:24:22 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -838,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"52191202421421023910552390000725381999815042\".\"invoice_series\":\"239\".\"invoice_number\":\"72538\".\"tracking_code\":807577.\"order_number\":\"000072538-239\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:23:09.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=8c0334d0-3e0c-4c72-8741-b7874b1579cc\".\"processing_hash\":\"8c0334d0-3e0c-4c72-8741-b7874b1579cc\"}.\"time\":\"125.6 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"8c0334d0-3e0c-4c72-8741-b7874b1579cc\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:23:09 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -837,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001632401066018444\".\"invoice_series\":\"137\".\"invoice_number\":\"163240\".\"tracking_code\":null.\"order_number\":\"000163240-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:41.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=7c91b075-365a-4b97-9fef-87adc50df170\".\"processing_hash\":\"7c91b075-365a-4b97-9fef-87adc50df170\"}.\"time\":\"126.0 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"7c91b075-365a-4b97-9fef-87adc50df170\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:41 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -836,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001632391065485676\".\"invoice_series\":\"137\".\"invoice_number\":\"163239\".\"tracking_code\":null.\"order_number\":\"000163239-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=1522187e-b600-4764-94fb-8614f02893b8\".\"processing_hash\":\"1522187e-b600-4764-94fb-8614f02893b8\"}.\"time\":\"131.1 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"1522187e-b600-4764-94fb-8614f02893b8\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -835,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001632241018539150\".\"invoice_series\":\"137\".\"invoice_number\":\"163224\".\"tracking_code\":null.\"order_number\":\"000163224-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=02bdc9bc-e321-483a-b67e-e58b375a63a8\".\"processing_hash\":\"02bdc9bc-e321-483a-b67e-e58b375a63a8\"}.\"time\":\"129.2 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"02bdc9bc-e321-483a-b67e-e58b375a63a8\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -834,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001632031141230154\".\"invoice_series\":\"137\".\"invoice_number\":\"163203\".\"tracking_code\":188125.\"order_number\":\"000163203-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=31c8df1d-0605-46c9-a947-e51e4a184229\".\"processing_hash\":\"31c8df1d-0605-46c9-a947-e51e4a184229\"}.\"time\":\"128.3 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"31c8df1d-0605-46c9-a947-e51e4a184229\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -833,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001632011959793312\".\"invoice_series\":\"137\".\"invoice_number\":\"163201\".\"tracking_code\":188125.\"order_number\":\"000163201-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=3ecca8b1-9645-4502-959b-803bd13e9cff\".\"processing_hash\":\"3ecca8b1-9645-4502-959b-803bd13e9cff\"}.\"time\":\"128.7 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"3ecca8b1-9645-4502-959b-803bd13e9cff\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -832,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001632001957850265\".\"invoice_series\":\"137\".\"invoice_number\":\"163200\".\"tracking_code\":null.\"order_number\":\"000163200-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=6f60479d-e981-44ea-9a9d-c418ffdacc72\".\"processing_hash\":\"6f60479d-e981-44ea-9a9d-c418ffdacc72\"}.\"time\":\"126.4 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"6f60479d-e981-44ea-9a9d-c418ffdacc72\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -831,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001631431007151768\".\"invoice_series\":\"137\".\"invoice_number\":\"163143\".\"tracking_code\":188125.\"order_number\":\"000163143-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=e75bcb25-a4d6-453a-b811-3678e361450a\".\"processing_hash\":\"e75bcb25-a4d6-453a-b811-3678e361450a\"}.\"time\":\"128.4 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"e75bcb25-a4d6-453a-b811-3678e361450a\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -830,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001631141971440435\".\"invoice_series\":\"137\".\"invoice_number\":\"163114\".\"tracking_code\":188125.\"order_number\":\"000163114-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=ca462d13-df24-4487-a99f-c959bb94a03a\".\"processing_hash\":\"ca462d13-df24-4487-a99f-c959bb94a03a\"}.\"time\":\"127.0 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"ca462d13-df24-4487-a99f-c959bb94a03a\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Chamado",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
  {
    logDeAPI: -829,
    iniciadoEm: "2020-01-07 21:00:00 -0300",
    finalizadoEm: "2020-01-07 21:00:00 -0300",
    requisição: "{\"logistic_provider\":\"VIA_REVERSA\".\"logistic_provider_id\":\"1040\".\"logistic_provider_federal_tax_id\":\"18410130000168\".\"shipper\":\"TIM\".\"shipper_federal_tax_id\":\"11425989900109\".\"invoice_key\":\"53200102421421013795551370001630891784047593\".\"invoice_series\":\"137\".\"invoice_number\":\"163089\".\"tracking_code\":188125.\"order_number\":\"000163089-137\".\"volume_number\":\"1\".\"events\":[{\"event_date\":\"2020-01-08T14:03:40.000-03:00\".\"original_code\":\"35\".\"original_message\":\"Entrega ao destinatario realizada com sucesso\"}]}",
    retorno: "{\"status\":\"OK\".\"messages\":[{\"type\":\"SUCCESS\".\"text\":\"Operação realizada com sucesso.\".\"key\":\"success.message\"}].\"content\":{\"monitoring_url\":\"https://api.intelipost.com.br/api/v1/tracking/event_monitorings?hash=e6058fc2-f2d2-4798-b0bb-17cfba1e3221\".\"processing_hash\":\"e6058fc2-f2d2-4798-b0bb-17cfba1e3221\"}.\"time\":\"126.0 ms\".\"timezone\":\"America/Sao_Paulo\".\"locale\":\"pt_BR\".\"hash\":\"e6058fc2-f2d2-4798-b0bb-17cfba1e3221\"}",
    endereçoDaAPI: "https://api.intelipost.com.br/api/v1/tracking/add/events",
    chamadoRecebido: "Recebido",
    criadoEm: "2020-01-08 14:03:40 -0300",
    alteradoEm: "2020-03-26 10:58:02 -0300",
    url: "http://www.upiara.com"
  },
];

import Vue from "vue";
import SortedTablePlugin from "vue-sorted-table";

Vue.use(SortedTablePlugin, {
  ascIcon: '<i class="ti-arrow-down"></i>',
  descIcon: '<i class="ti-arrow-up"></i>'
});

export default {

  name: 'plg-api-logs',

  data: function() {
    return {
      sortBy: "iniciadoEm",
      perPage: 10,
      currentPage: 1,
      sortDesc: false,
      sortByFormatted: true,
      filterByFormatted: true,
      sortable: true,
      fields: fields,
      items: items,
    };
  },
  computed: {
    rows() {
      return this.items.length;
    }
  }
};
</script>
