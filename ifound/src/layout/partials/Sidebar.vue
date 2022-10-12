<template>
  <section class="app-sidebar">
    <nav class="sidebar sidebar-offcanvas" id="sidebar">
      <ul class="nav">
        <li class="nav-item" v-on:click="collapseAll">
          <router-link class="nav-link" :to="{name: 'home'}">
            <i class="ti-home menu-icon"></i>
            <span class="menu-title">Inicial</span>
          </router-link>
        </li>

        <li class="nav-item" v-on:click="collapseAll">
          <router-link class="nav-link" :to="{name: 'animais'}">
            <i class="mdi mdi-paw menu-icon"></i>
            <span class="menu-title">Animais</span>
          </router-link>
        </li>

        <!-- <li class="nav-item" v-on:click="collapseAll">
          <router-link class="nav-link" :to="{name: 'home'}">
            <i class="ti-clipboard menu-icon"></i>
            <span class="menu-title">Saldo</span>
          </router-link>
        </li> -->
        <!-- <li class="nav-item" v-if="$can('view', 'defaultWorkspace')" v-on:click="collapseAll">
          <router-link class="nav-link" :to="{name: 'default_workspace'}">
            <i class="mdi mdi-domain menu-icon"></i>
            <span class="menu-title">Workspace Padrão</span>
          </router-link>
        </li>

        <li class="nav-item" v-if="$can('view', 'defaultWorkspace')" v-on:click="collapseAll">
          <router-link class="nav-link" :to="{name: 'payments_table'}">
            <i class="mdi mdi-account-cash menu-icon"></i>
            <span class="menu-title">Pagamentos</span>
          </router-link>
        </li>

        <li class="nav-item" v-if="$can('view', 'defaultWorkspace')" v-on:click="collapseAll">
          <router-link class="nav-link" :to="{name: 'settings'}">
            <i class="mdi mdi-settings menu-icon"></i>
            <span class="menu-title">Configurações</span>
          </router-link>
        </li> -->

        <!-- <li class="nav-item" v-on:click="collapseAll">
          <router-link class="nav-link" :to="{name: 'home'}">
            <i class="ti-layout menu-icon"></i>
            <span class="menu-title">Comprovantes</span>
          </router-link>
        </li> -->

        <!-- <li class="nav-item">
          <span class="nav-link" v-b-toggle="'ui-operacao'">
            <i class="ti-layout menu-icon"></i>
            <span class="menu-title">Operação</span>
            <i class="menu-arrow"></i>
          </span>
          <b-collapse accordion="sidebar-accordion" id="ui-operacao">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item">
                <router-link class="nav-link" to="/site/accounts/">Aprovações</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/site/users/">Auditoria</router-link>
              </li>
            </ul>
          </b-collapse>
        </li> -->
<!-- 
        <li v-if="$can('view', 'users')" class="nav-item">
          <span class="nav-link" v-b-toggle="'ui-cadastros'">
            <i class="ti-layout menu-icon"></i>
            <span class="menu-title">Cadastros</span>
            <i class="menu-arrow"></i>
          </span>
          <b-collapse accordion="sidebar-accordion" id="ui-cadastros">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item">
                <router-link class="nav-link" to="/site/accounts/">Contas</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/site/users/">Usuários</router-link>
              </li>
            </ul>
          </b-collapse>
        </li>

        <li v-if="$can('view', 'apis')" class="nav-item">
          <span class="nav-link" v-b-toggle="'ui-apis'">
            <i class="ti-view-list menu-icon"></i>
            <span class="menu-title">APIs</span>
            <i class="menu-arrow"></i>
          </span>
          <b-collapse accordion="sidebar-accordion" id="ui-apis">
            <ul class="nav flex-column sub-menu">
              <li class="nav-item">
                <router-link class="nav-link" to="/site/api_logs_docs/">Documentação</router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="https://portalviareversa.csssolutions.com.br/swagger">Endereços</a>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/site/api_logs/">Logs</router-link>
              </li>
            </ul>
          </b-collapse>
        </li> -->
      </ul>
    </nav>
  </section>
</template>

<script>
export default {
  
  name: "sidebar",
  data: function()  {
    return {
      collapses: [{ show: false }, { show: false }, { show: false }],
      viewRoadmap: false,
      mockAccount: '',
    };
  },
  methods: {
    collapseAll() {
      var exp_elm = document.getElementsByClassName("show");
      if (exp_elm.length > 0) {
        var elm_id = exp_elm[0].id;
        this.$root.$emit("bv::toggle::collapse", elm_id);
      }
    },

    setLocalStorage(authenticated,email,name){
      localStorage.setItem('authenticated',authenticated);
      localStorage.setItem('email',email);
      localStorage.setItem('name',name);
    },

    getLocalStorageAndInjectOnmockAccount(){
      var mockAccount = {
        email: localStorage.getItem('email'),
        name: localStorage.getItem('name'),
      }
      this.mockAccount = mockAccount;
    }

  },
  created() {
    this.getLocalStorageAndInjectOnmockAccount();
  },
  mounted() {
    const body = document.querySelector("body");
    // add class 'hover-open' to sidebar navitem while hover in sidebar-icon-only menu
    document.querySelectorAll(".sidebar .nav-item").forEach(function(el) {
      el.addEventListener("mouseover", function() {
        if (body.classList.contains("sidebar-icon-only")) {
          el.classList.add("hover-open");
        }
      });
      el.addEventListener("mouseout", function() {
        if (body.classList.contains("sidebar-icon-only")) {
          el.classList.remove("hover-open");
        }
      });
    });
  },
  watch: {
    $listenSidebar() {
      document.querySelector("#sidebar").classList.toggle("active");
    }
  }
};
</script>
