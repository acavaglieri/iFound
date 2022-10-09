<template>
  <div>
    <div>
      <b-navbar toggleable="md" :class="{ 'onScroll': !view.topOfPage, 'navbar-dark': view.topOfPage }" fixed="top">
        <b-navbar-brand href="#"
          ><img src="../../../public/img/website/images/logo.png" alt=""
        /></b-navbar-brand>
        <b-navbar-toggle target="navbar-toggle-collapse" @click="changeNavClass()">
        </b-navbar-toggle>
        <b-collapse id="navbar-toggle-collapse" is-nav>
          <!-- <b-navbar-nav class="ml-md-auto">
            <b-nav-item class="item-mobile" href="#home">Home</b-nav-item>
            <b-nav-item class="item-mobile" href="#about">Sobre</b-nav-item>
            <b-nav-item class="item-mobile" href="#portfolio">Galeria</b-nav-item> --><!--
            <b-nav-item class="item-mobile" @click="goToLogin()"
              >Login</b-nav-item
            >
            <b-nav-item class="item-mobile" @click="goToRegister()"
              >Cadastre-se</b-nav-item
            >
          </b-navbar-nav>-->
        </b-collapse>
      </b-navbar>
    </div>

    <section id="home" class="align-items-center main-banner "> <!-- main-banner-img -->
      <b-row>
        <b-col cols="12">
          <div class="text-center mx-2">
            <div class="heading">
              <h1 class="">Bem vindo ao iFound</h1>
              <br />
              <h3 class="">
                <span style="font-size: 2rem">A solução perfeita para </span>
                <span class="cd-words-wrapper"><br>
                  <span class="typity d-inline-block" style="font-size: 1.8rem"></span>
                </span>
              </h3>
              <div class="fixed-buttons">
                <b-row>
                  <b-col lg="5" cols="2"></b-col>
                  <b-col lg="1" cols="4">
                    <div class="btn-ber">
                      <router-link
                        class="get_btn hvr-bounce-to-top"
                        :to="{name: 'login'}"
                        >Login</router-link
                      >
                    </div>
                  </b-col>
                  <b-col lg="1" cols="4">
                    <div class="btn-ber">
                      <router-link
                        class="get_btn hvr-bounce-to-top"
                        :to="{name: 'register'}"
                        >Cadastro</router-link
                      >
                    </div>
                  </b-col>
                  <b-col lg="5" cols="2"></b-col>
                </b-row>
              </div>
            </div>
          </div>
        </b-col>
      </b-row>
    </section>
    <!-- <section id="about">
      <div class="container about">
        <div class="row">
          <div class="col-md-6">
            <div class="my-5 pt-5">
              <div class="heading text-center">
              <h2 class="my-5">Bem vindo ao iFound</h2>
              <p>
                Uma solução que resolve problemas de fluxo de dinheiro para o
                PA, garantindo fluxos seguros e autorizados de antecipação com
                controle rápido.
              </p>
              <p>Afinal, quando se trata de antecipação,</p>
              <h4>ANTES É MELHOR!</h4>
              </div>
            </div>
          </div>

          <div class="col-md-6"></div>
        </div>
      </div>
    </section> -->
    <!-- end section -->
    <!-- <section id="portfolio" class="section gallery lb">
      <div class="container">
        <div class="section-title text-center">
          <div>
            <h3 class="pt-5">Gráficos</h3>
            <p class="mb-5">Galeria de gráficos do projeto.</p>
          </div>
        </div>
        <div class="col-md-4 col-sm-6 gallery-grid gal_a">
          <div class="gallery-single fix">
            <img
              src="../../../public/img/website/uploads/mockup1.png"
              class="img-fluid"
              alt="Image"
            />
            <div class="img-overlay">
              <a
                href="../../../public/img/website/uploads/mockup1.png"
                data-rel="prettyPhoto[gal]"
                class="hoverbutton global-radius"
                ><i class="fa fa-picture-o"></i
              ></a>
            </div>
          </div>
        </div>

        <div class="col-md-4 col-sm-6 gallery-grid gal_a">
          <div class="gallery-single fix">
            <img
              src="../../../public/img/website/uploads/mockup2.png"
              class="img-fluid"
              alt="Image"
            />
            <div class="img-overlay">
              <a
                href="../../../public/img/website/uploads/mockup2.png"
                data-rel="prettyPhoto[gal]"
                class="hoverbutton global-radius"
                ><i class="fa fa-picture-o"></i
              ></a>
            </div>
          </div>
        </div>

        <div class="col-md-4 col-sm-6 gallery-grid gal_a">
          <div class="gallery-single fix">
            <img
              src="../../../public/img/website/uploads/mockup3.png"
              class="img-fluid"
              alt="Image"
            />
            <div class="img-overlay">
              <a
                href="../../../public/img/website/uploads/mockup3.png"
                data-rel="prettyPhoto[gal]"
                class="hoverbutton global-radius"
                ><i class="fa fa-picture-o"></i
              ></a>
            </div>
          </div>
        </div>
      </div>
    </section> -->
    <!-- <div class="copyrights">
      <div class="container">
        <div class="footer-distributed">
          <div class="footer-logo">
            <a href="#"
              ><img src="../../../public/img/website/images/logo.png" alt=""
            /></a>
          </div>
          <div>
            <div class="">
              <p class="footer-company-name footer-copyright">
                All Rights Reserved. &copy; 2022
                <a href="http://www.upiara.com" target="_blank">Upiara</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      view: {
        topOfPage: true
      },
      index: 0,
      typed: "",
      expanded: false
    }
  },
  beforeMount() {
    window.addEventListener('scroll', this.handleScroll)
  },
  methods: {
    goToLogin(){
      this.$router.replace({ name: 'login' })
    },
    goToRegister(){
      this.$router.replace({ name: 'register' })
    },
    handleScroll(){
      if(window.pageYOffset>0 && !this.expanded){
        if(this.view.topOfPage) this.view.topOfPage = false
      } else if (!this.expanded) {
        if(!this.view.topOfPage) this.view.topOfPage = true
      }
    },
    changeNavClass(){
      this.expanded = !this.expanded
      if(window.pageYOffset == 0) {
        if(this.view.topOfPage) {
          this.view.topOfPage = false
        } else {
          this.view.topOfPage = true
        }
      }
    },
    getRandomPhrase() {
      const phrases = [
        "IDENTIFICAR SEU PET",
        "FACILITAR O ENCONTRO DE SEU BICHINHO",
      ];
      this.index = (this.index + 1) % phrases.length;
      return phrases[this.index];
    },
    startType(phrase, index) {
      let ref = this;
      let element = document.querySelector(".typity");
      if(index < phrase.length){
        this.typed += phrase.charAt(index);
        element.innerHTML = this.typed;
        index++
        setTimeout(function () {
          ref.startType(phrase, index);
        }, 50);
      } else {
        this.typed = "";
        setTimeout(function () {
          element.classList.add("highlight");
        }, 4000);
        setTimeout(function () {
          element.classList.remove("highlight");
          element.innerHTML = this.typed;
          ref.startType(ref.getRandomPhrase(), 0);
        }, 5000);
      }
    },
  },
  mounted() {
    // TO-DO: Tratar esse redirect no navigation guard
    var authenticated = localStorage.getItem('authenticated');
    if (authenticated=="true"){
      this.$router.replace({name: 'home'});
    }
    this.startType(this.getRandomPhrase(), 0);
  },
};
</script>

<style scoped lang="scss">
  @import url('../../../public/img/website/style/style.scss');
  @media screen and (min-width: 600px) {
    .fixed-buttons {
     min-width: 100vw;
    }
  }
  @media screen and (max-width: 600px) {
    .item-mobile {
      font-size: 2rem;
    }
  }
  #home, #about{
    height: 100vh;
    width: 100vw;
  }
  .typity::after {
    background-color: transparent;
    content: "";
    display: block;
    height: 2rem;
    position: absolute;
    right: 0;
    bottom: 0;
    width: 2px;
    animation: blink-cursor 0.95s step-end infinite;
  }
  @keyframes blink-cursor {
    0% {
      background-color: transparent;
    }
    50% {
      background-color: white;
    }
  }
</style>