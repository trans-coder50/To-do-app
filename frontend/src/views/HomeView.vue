<template>
  <div class="home">
    <logout/>
  </div>
  
<container/>
</template>

<script>
// @ is an alias to /src
import logout from '@/components/LogOut.vue'
import container from '@/components/Container.vue'
export default {
  name: 'HomeView',
  components: {
logout,container
  }
}
</script>
