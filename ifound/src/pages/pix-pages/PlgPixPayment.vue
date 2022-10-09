<template>
  <div>
    <transition name="slide-up" appear mode="out-in">
      <section>
        <div class="row">
          <div class="col-12">
            <div class="card border rounded">
              <div class="card-body">
                <b-row>
                  <b-col lg="11">
                    <h3 class="my-3 mx-3 text-center">Encontrou um animal?</h3>
                    <h4 class="my-3 mx-3 text-center">Escaneie o codigo e descubra mais informações sobre ele</h4>
                  </b-col>
                  <b-col lg="1" class="py-3 d-none d-lg-block">
                    <router-link :to="{ name: 'home' }" style="color: black;">
                    <h3><i class="mdi mdi-arrow-left"></i></h3>
                    </router-link>
                  </b-col>
                </b-row>
                <hr>
              </div>
              <div class="row">
                <div class="col-md-11 col-12 text-center my-5">
                  <router-link :to="{name: 'pix_qrcode_scan'}" style="text-decoration: none; color: black;">
                    <div>
                      <i class="fa fa-qrcode icon-lg"></i>
                      <p class="mt-2 font-weight-bold">Escanear QRCode</p>
                    </div>
                  </router-link>
                </div>
                <!--
                <div class="col-md-6 col-12 text-center my-5">
                  <router-link :to="{name: 'pix_copy_paste'}" style="text-decoration: none; color: black;">
                    <div>
                      <i class="fa fa-copy icon-lg"></i>
                      <p class="mt-2 font-weight-bold">PIX Copia e Cola</p>
                    </div>
                  </router-link>
                </div> 
                -->
              </div>
            </div>
          </div>
        </div>
      </section>
    </transition>
  </div>
</template>