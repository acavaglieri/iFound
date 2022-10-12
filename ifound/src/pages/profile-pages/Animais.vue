<template>
    <div id="app" >
      <Pets/>
    </div>
  </template>

<script>

import Pets from '../../components/Pets.vue'

export default {
  name: "dashboard",
  components: {

    Pets,
  },
}
  
</script>
